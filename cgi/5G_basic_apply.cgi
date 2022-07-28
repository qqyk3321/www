#!/bin/sh

./applylib head

source /home/qqyk321/work/thttpd/www/cgi/buildenv
eval `/home/qqyk321/work/thttpd/www/cgi/proccgi.sh $*`
fun_at(){

    stty -F /dev/$1 min 0 time 5
    for i in {1,2,3,4}
    do

        echo -e "$2\r\n" >> /dev/$1
        cat /dev/$1 > at_log
        if [ "`cat at_log|grep OK`" != "" ];then
            break
        fi
    done
}


if [ "$FORM_doaction" = "apply" ] ; then


	echo -e "执行检测<br/><br/>"
	
	echo -e "检测网卡名称有效性<br/><br/>"
	if [ "`ifconfig -a |grep ${FORM_USB_name}`" != "" ] ; then
		echo -e "网卡名称合法<br/><br/>"
		
		echo -e "网卡名称设置成功<br/><br/>"
		sed -i "s/^USB_name.*\+=.*/USB_name=${FORM_USB_name} /" 5G_config
		sed -i "s/^NameOk.*\+=.*/NameOk=OK /" 5G_config
	else 
		echo -e "网卡名称不存在，存在网卡名称如下<br/><br/>"
		echo -e "`ls /sys/class/net/`<br/><br/>"
		sed -i "s/^USB_name.*\+=.*/USB_name=${FORM_USB_name} /" 5G_config
		sed -i "s/^NameOk.*\+=.*/NameOk=FAILED /" 5G_config
		echo -e "请重新设置<br/><br/>"

	fi
	echo -e "检测网卡AT串口有效性<br/><br/>"
	if [ "`ls /dev/${FORM_USB_serial}`" == "" ];then
		echo -e "5G网卡at端口不存在<br/><br/>"
		sed -i "s/^USB_serial.*\+=.*/USB_serial=${FORM_USB_serial} /" 5G_config

		sed -i "s/^SerialOk.*\+=.*/SerialOk=FAILED/" 5G_config
	else 
		fun_at ${FORM_USB_serial} at
		sed -i "s/^USB_serial.*\+=.*/USB_serial=${FORM_USB_serial} /" 5G_config
		if [ "`cat at_log|grep OK`" != "" ];then
			echo -e "5G网卡at端口设置成功<br/><br/>"
			sed -i "s/^SerialOk.*\+=.*/SerialOk=OK/" 5G_config
		else
			echo -e "5G网卡at存在但是设置失败，请检查端口是否正确<br/><br/>"
			sed -i "s/^SerialOk.*\+=.*/SerialOk=FAILED/" 5G_config
		fi
	fi
	

	
	
		

		

	

	

	

	

	echo -e "已完成"
	echo -e "点击返回按钮回到上一页面"
	


elif [ "$FORM_doaction" = "restore" ] ; then
	ralink_init renew 
	echo -e "恢复成功"

elif [ "$FORM_doaction" = "reboot" ] ; then
	echo -e "设备正在重启，请稍后重新访问"
else
	echo -e "无效参数!"
fi

./applylib tail






