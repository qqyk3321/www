#!/bin/sh
###1. 检测check 5G_config 中是不是有 SerialOk=OK 
###2. 检测是否插入sim卡
###3  检测其他项
###var 列表
	
####列表：["AT_CCID","AT_
####
####
var_list='ATI  AT_CLCK AT_QINISTAT AT_QSIMDET_enable AT_QSIMDET_insert_level AT_QUIMSLOT'
###读入config文件
while read line;do
    eval "$line"
done < 5G_config
####定义全局变量用于承接log
at_log=
uart=/dev/${USB_serial}

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
if [ "${SerialOk}" != "OK" ] || [ "`ls $uart`" == ""  ];then
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

#### 检测产品固件版本号
uart "ATI"
echo "$at_log" > at_log_ati
ATI="`echo "$at_log"|awk '{gsub(/ /,"")}1'|tr -s '\n'|sed 's/\r$//'`"
echo "$ATI" >ATI
ATI_manufacturer="`echo "$ATI"|sed -n '1,1p'`"
ATI_model="`echo "$ATI"|sed -n '2,2p'`"
ATI_firmware_revision="`echo "$ATI"|grep "Revision:"|cut -d : -f 2`"

echo 'var ATI_manufacturer="'${ATI_manufacturer}'";'
echo 'var ATI_model="'${ATI_model}'";'
echo 'var ATI_firmware_revision="'${ATI_firmware_revision}'";'
#### 检测IMEI
uart "AT+GSN"
echo "$at_log" > at_log_gsn
AT_GSN="`echo "$at_log"|awk '{gsub(/ /,"")}1'|sed 's/\r$//'|sed '/^$/d'|sed -n '1,1p'`"
echo "${AT_GSN}" > AT_GSN
echo var AT_GSN=\"${AT_GSN}\"\;
####检测网卡类型及驱动方式 
uart "at+qcfg=\"usbnet\""
re="`echo "${at_log}"|awk '{gsub(/ /,"")}1'|tr -s '\n'|sed 's/\r$//'|grep "+QCFG:"|cut -d : -f 2|cut -d , -f 2`"
if [ "${re}" == "1" ];then
	echo "var AT_QCFG_usbnet=\"ECM\";"
elif [ "${re}" == "3" ];then
	echo "var AT_QCFG_usbnet=\"RNDIS\";"
elif [ "${re}" == "5" ];then
	echo "var AT_QCFG_usbnet=\"NCM\";"
else
	echo "var AT_QCFG_usbnet=\"未知\";"
fi
####检测网卡拨号模式
uart "at+qcfg=\"nat\""
echo "${at_log}" >at_log_nat
re="`echo "${at_log}"|awk '{gsub(/ /,"")}1'|tr -s '\n'|sed 's/\r$//'|grep "+QCFG:"|cut -d : -f 2|cut -d , -f 2`"
echo "${re}" >RE
if [ "${re}" == "0" ];then
    echo "var AT_QCFG_nat=\"网卡模式\";"
elif [ "${re}" == "1" ];then
    echo "var AT_QCFG_nat=\"路由模式\";"
elif [ "${re}" == "2" ];then
    echo "var AT_QCFG_nat=\"网桥模式\";"
else
    echo "var AT_QCFG_nat=\"未知\";"
fi
####检查USB，VID，PID，开启端口
uart "at+qcfg=\"usbcfg\""
re="`echo "${at_log}"|awk '{gsub(/ /,"")}1'|tr -s '\n'|sed 's/\r$//'|grep "+QCFG:"|cut -d : -f 2`"
######修改环境变量分隔符
OLD_IFS="$IFS"
IFS=","
array=($re)
IFS="$OLD_IFS"
echo "var AT_QCFG_usbcfg_vid=\"${array[1]}\";"
echo "var AT_QCFG_usbcfg_pid=\"${array[2]}\";"
port_list=(1 1 1 1 "diag" "log" "at_port" "modem" "NMEA" "ADB" "uac")

echo -n "var AT_QCFG_USBCFG_port=\""

for i in {4..10}
do
	echo -n "${port_list[$i]}: "
	if [ "${array[$i]}" == "1" ];then
		echo -n "打开;  "
	else
		echo -n "关闭;  "
	fi
done
echo "\";"



