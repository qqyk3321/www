#!/bin/sh




source /home/qqyk321/work/thttpd/www/cgi/buildenv


eval `/home/qqyk321/work/thttpd/www/cgi/proccgi.sh $*`

 


echo -e "${FORM_debug_cmd}" > cmd_log









cat << EOF
<!DOCTYPE html>
    <html lang="zh">
    <head>
        <meta charset="utf-8">
        <title>AS Syslog html</title>
        <meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatible">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">
        <link rel="stylesheet" type="text/css" href="lib/bootstrap/css/bootstrap.css">
        
        <link rel="stylesheet" type="text/css" href="stylesheets/theme.css">
        <link rel="stylesheet" href="lib/font-awesome/css/font-awesome.css">
        <script type="text/javascript" src="cgi/session.cgi"></script>
        <script src="lib/jquery-1.7.2.min.js" type="text/javascript"></script>
    <script type="text/javascript">
    function changeFrameHeight(that){
            \$(that).height(document.documentElement.clientHeight-80);
        }
    </script>
        </style>
    </head>

    <!--[if lt IE 7 ]> <body class="ie ie6"> <![endif]-->
    <!--[if IE 7 ]> <body class="ie ie7 "> <![endif]-->
    <!--[if IE 8 ]> <body class="ie ie8 "> <![endif]-->
    <!--[if IE 9 ]> <body class="ie ie9 "> <![endif]-->
    <!--[if (gt IE 9)|!(IE)]><!--> 
    <body style="background-color: #FFF"  class=""> 
    <!--<![endif]-->
        <div class="content">
            <div class="header">
                        <h1 class="page-title">CMD</h1>
            </div>
                <div class="container-fluid">
            <div class="row-fluid">
                        <iframe name="debug_show1" id="debug_show1"  width="100%" height="100%" style="background-color: #FFF" onload="changeFrameHeight(this)" scrolling="auto" frameborder="no" border="0" marginwidth="0" marginheight="0" allowtransparency="yes" src="debug_cmd.cgi"/></iframe>
                </div></div>
        </div>
    </body>
    </html>
EOF
