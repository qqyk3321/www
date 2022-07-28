#!/bin/sh
echo -e "Content-type: text/javascript"
echo -e "Cache-Control: no-cache\n"

source /home/qqyk321/work/thttpd/www/cgi/buildenv
./session

cat << EOF
var htmlversion = "V1.0"
var wapiversion = "V1.0"
EOF

