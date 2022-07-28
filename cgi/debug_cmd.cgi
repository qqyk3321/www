#!/bin/sh
echo -e "Content-type: text/plaintext"
echo -e "Cache-Control: no-cache\n"
source /home/qqyk321/work/thttpd/www/cgi/buildenv
cmd="`cat cmd_log`"
echo -e "#################################################################"
echo -e "######################### ${cmd} #################################"
echo -e "#################################################################"
${cmd}
