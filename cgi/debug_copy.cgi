#!/bin/sh





echo -e "Content-Type:text/html"
echo -e "Cache-Control: no-cache\n"

source /home/qqyk321/work/thttpd/www/cgi/buildenv


eval `/home/qqyk321/work/thttpd/www/cgi/proccgi.sh $*`

 
cat << AAA
    <html>
    <head>
        <title>CGI Test</title>
    </head>
    <body style="background-color: #FFF">
    <h2>${FORM_debug_cmd}</h2>
    <textarea  readonly style="border: none;min-height:600px;min-width:800px;max-height:600px;max-width:800px;">
AAA

${FORM_debug_cmd}








cat << AAA
    </textarea>
    </body>
    </html>
AAA
