#!/bin/sh
echo -e "Content-type: text/javascript"
echo -e "Cache-Control: no-cache\n"

source /home/qqyk321/work/thttpd/www/cgi/buildenv
./session

cat << EOF
var cert_cn = "qqyk3321"
var cert_dc = "qqyk3321"
var cert_c = "qqyk3321"
var cert_o = "qqyk3321"
var cert_ou = "qqyk3321"
EOF

