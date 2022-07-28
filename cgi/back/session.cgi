#!/bin/sh
echo -e "Content-type: text/javascript"
echo -e "Cache-Control: no-cache\n"

./buildenv

./session

