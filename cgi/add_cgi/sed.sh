#!/bin/sh
b="sed 's/\\r$//'|sed '/^$/d'"
a="tr -s '\\n'|sed 's/\\r$//'"
echo $a
echo $b
sed -i "s/${b}/${a}/g" firmware_analysis.sh_b 
