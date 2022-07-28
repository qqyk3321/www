#!/bin/sh

echo -e "Content-type: text/plaintext"
echo -e "Cache-Control: no-cache\n"

source /home/qqyk321/work/thttpd/www/cgi/buildenv
echo -e "#################################################################"
echo -e "######################### dmesg #################################"
echo -e "#################################################################"
dmesg
