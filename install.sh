#!/bin/sh
mkdir -p /opt/asf &&
cd /opt/asf &&
if [ ! -e /opt/asf/asf.py ]; then 
curl https://raw.githubusercontent.com/LucasIkuhara/asf/main/asf.py -o asf.py;
fi;

# Add to (bash or other)rc
BOOTSTRAP='''
# ASF_START
export ASF_HOME=/opt/asf
asf() {
  TARGET=/tmp/asf_target
  python3 $ASF_HOME/asf.py "$@" && cd $(cat "$TARGET")
}
# ASF_END
'''

if [ -w ~/.bashrc ]; then echo "$BOOTSTRAP" >>  ~/.bashrc; fi;
if [ -w ~/.zshrc ]; then echo "$BOOTSTRAP" >>  ~/.zshrc; fi;
echo "asf installation successfull."
