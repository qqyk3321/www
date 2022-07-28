#!/bin/sh
###1. 检测check 5G_config 中是不是有 SerialOk=OK 
###2. 检测是否插入sim卡
###3  检测其他项
###var 列表
	
####列表：["AT_CCID","AT_
####
####
var_list='AT_CCID AT_CIMI AT_CLCK AT_QINISTAT AT_QSIMDET_enable AT_QSIMDET_insert_level AT_QUIMSLOT'
###读入config文件
while read line;do
    eval "$line"
done < 5G_config
####定义全局变量用于承接log
at_log=
uart="/dev/${USB_serial}"

####定义函数读取返回值
function uart(){
cmd=$1
for i in {1,2,3,4}
do

	echo -e "${cmd}\r\n" >> $uart
   	at_log=`cat $uart`
	 
    if [ "`echo ${at_log} |grep OK`" != "" ];then
		break
	fi
done
}
####检测串口设置是否正确(检查配置文件，检查是否包含串口设备)
if [ "${SerialOk}" != "OK" ] || [ "`ls $uart`" == "" ];then
    #put all var "串口设置失败”
    for i in ${var_list}
    do
        echo "var ${i}=\"串口设置失败\";"       
    done
    exit 0
fi

##设置tty读取断开时间，否则cat无法自动退出
stty  -F ${uart} min 0 time 1
##设置关闭回显，并检查是否能够成功配置
uart "ATE0"
if [ "`echo "{$at_log}"|grep "OK"`" == "" ];then
    for i in ${var_list}
    do
        echo "var ${i}=\"串口无法正常打开使用\";"       
    done
    exit 0

fi

#### 检测sim卡是否插入,并检测CCID
uart "at+ccid"
re="`echo ${at_log}|grep "+CME ERROR: 10"`"

if [ "${re}" != ""  ];then
	for i in ${var_list}
	do 
		echo "var ${i}=\"SIM 卡未插入\";"
	done
	exit 0
fi
AT_CCID="`echo "$at_log"|awk '{gsub(/ /,"")}1'|tr -s '\n'|sed 's/\r$//'|grep "+CCID:"|cut -d : -f 2`"
echo 'var AT_CCID="'${AT_CCID}'";'
#### 检测IMIS
uart "at+cimi"

echo $at_log > at_log_cimi
AT_CIMI="`echo "$at_log"|awk '{gsub(/ /,"")}1'|tr -s '\n'|sed 's/\r$//'|sed -n '1,1p'`"
echo $AT_CIMI > AT_CIMI
echo "var AT_SIMI=\"${AT_CIMI}\";"
####锁定问题 
uart "at+clck=\"SC\",2"
if [ "`echo ${at_log}|awk '{gsub(/ /,"")}1'|grep "+CLCK:0"`" == "" ];then
	echo var AT_CLCK=\"锁定\"\;
else
	echo var AT_CLCK=\"未锁定\"\;
fi
####SIM 卡准备情况
uart "at+qinistat"
re="`echo "${at_log}"|awk '{gsub(/ /,"")}1'|tr -s '\n'|sed 's/\r$//'|grep "+QINISTAT:"|cut -d : -f 2`"
echo -e "$re" > at_log
if [ "${re}" == "0" ];then
	echo var AT_QINISTAT=\"未初始状态\"\;
elif [ "${re}" == "1" ];then
	echo var AT_QINISTAT=\"CPN已就绪\"\;
elif [ "${re}" == "2" ];then
	echo var AT_QINISTAT=\"SMS初始化完成\"\;
elif [ "${re}" == "4" ];then
	echo var AT_QINISTAT=\"电话簿初始化完成\"\;
elif [ "${re}" == "7" ];then
	echo var AT_QINISTAT=\"CPN已就绪，SMS初始化完成，电话簿初始化完成\"\;
else
	echo var AT_QINISTAT=\"未知\"\;
fi
####SIm卡卡槽检测
uart "AT+QSIMDET?"
re="`echo "${at_log}"|awk '{gsub(/ /,"")}1'|tr -s '\n'|sed 's/\r$//'|grep "+QSIMDET:"|cut -d : -f 2`"
if [ "${re}" == "0,0" ];then
	echo "var AT_QSIMDET_enable=\"禁用\";"
	echo "var AT_QSIMDET_insert_level=\"低电平\";"
elif [ "${re}" == "1,0" ];then
	echo "var AT_QSIMDET_enable=\"启用\";"
    echo "var AT_QSIMDET_insert_level=\"低电平\";"

elif [ "${re}" == "0,1" ];then
	echo "var AT_QSIMDET_enable=\"禁用\";"
    echo "var AT_QSIMDET_insert_level=\"高电平\";"

elif [ "${re}" == "1,1" ];then
	echo "var AT_QSIMDET_enable=\"启用\";"
    echo "var AT_QSIMDET_insert_level=\"高电平\";"

else 
	echo "var AT_QSIMDET_enable=\"未知\";"
    echo "var AT_QSIMDET_insert_level=\"未知\";"
fi
####检查物理卡槽未知
uart "AT+QUIMSLOT?"
re="`echo "${at_log}"|awk '{gsub(/ /,"")}1'|tr -s '\n'|sed 's/\r$//'|grep "+QUIMSLOT:"|cut -d : -f 2`"
if [ "${re}" == "1" ];then
	echo "var AT_QUIMSLOT=\"卡槽1\";"
elif [ "${re}" == "2" ];then
    echo "var AT_QUIMSLOT=\"卡槽2\";"
else
    echo "var AT_QUIMSLTOT=\"未知\";"
fi
####
