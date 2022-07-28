#!/bin/sh
uart="/dev/ttyUSB2"
if [ "`ls $uart`" == "" ]; then
  echo "no"
fi
