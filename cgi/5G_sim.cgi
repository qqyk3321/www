#!/bin/sh
echo -e "Content-type: text/javascript"
echo -e "Cache-Control: no-cache\n"

source /home/qqyk321/work/thttpd/www/cgi/buildenv
./session
./5G_basic

