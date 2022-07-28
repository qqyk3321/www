#!/bin/sh
cmd=$1
uart="/dev/$2"
stty -F $uart  min 0 time 5
for i in {1,2,3,4}
do

	echo -e "${cmd}\r\n" >> $uart
   	cat $uart > at_log
    if [ "`cat at_log |grep OK`" != "" ];then
        break
	fi
done
