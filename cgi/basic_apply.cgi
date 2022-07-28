#!/bin/sh

./applylib head

./buildenv
eval `proccgi $*`

if [ "$FORM_doaction" = "apply" ] ; then
	echo -e "正在检查参数...."

	echo -e "检查完成<br/><br/>"

	echo -e	"正在应用设置...."

	nvram_set cert_cn "$FORM_cert_cn"
	nvram_set cert_dc "$FORM_cert_dc"
	nvram_set cert_c "$FORM_cert_c"
	nvram_set cert_o "$FORM_cert_o"
	nvram_set cert_ou "$FORM_cert_ou"

	buildas.sh 2>> /dev/null

	echo -e "设置成功"

elif [ "$FORM_doaction" = "restore" ] ; then
	ralink_init renew 
	echo -e "恢复成功"

elif [ "$FORM_doaction" = "reboot" ] ; then
	echo -e "设备正在重启，请稍后重新访问"
else
	echo -e "无效参数!"
fi

./applylib tail

if [ "$FORM_doaction" = "apply" ] ; then
	killall ASServer
	cd  $CERTPATH 2>> /dev/null
	nohup ASServer -d 2>> /dev/null &
fi





