#!/bin/sh

./buildenv
eval `/home/qqyk321/work/thttpd/www/cgi/proccgi.sh $*`


#nvram commit
#php -f login.php


SESSIONDIR=/home/qqyk321/work/thttpd/www/cgi/log/run

mkdir -p $SESSIONDIR

USERMD5="`cat md5_check`"

eval `/home/qqyk321/work/thttpd/www/cgi/proccgi.sh $*`

if [ "$FORM_pass" == "$USERMD5" ] ; then
	find $SESSIONDIR/* -mmin +11 -exec rm -f {} \;
	SESSION=`printf "%04x%04x" $RANDOM $RANDOM`
	touch $SESSIONDIR/$SESSION
	GOTOURL="index.html"
else
	SESSION=""
	if [ -n "$FORM_user" ] ; then
		GOTOURL="sign-in.html?user=$FORM_user"
	else
		GOTOURL="sign-in.html"
	fi
fi

echo -e "Content-type: text/html"
echo -e "Set-Cookie: SESSION=$SESSION"
echo -e "Cache-Control: no-cache\n"



cat << EOF
<!DOCTYPE html>
<html lang="en">
  <head>
		<script>  
			top.location = "../$GOTOURL" 
		</script>  
  </head>
   <body>

   </body>
</html> 
EOF

