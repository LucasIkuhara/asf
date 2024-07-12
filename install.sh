#!/bin/sh
mkdir -p /opt/asf &&
cd /opt/asf &&
curl https://raw.githubusercontent.com/LucasIkuhara/asf/main/asf.py -o asf.py[[-z ~/.bashrc]] echo "wi"

# Add to (bash or other)rc
BOOTSTRAP='''

# ASF_START
export ASF_HOME=$(pwd)
asf() {
  TARGET=/tmp/asf_target
  python3 $ASF_HOME/asf.py "$@" && cd $(cat "$TARGET")
}
# ASF_END

'''

if [ -w ~/.bashrc ]; then echo "$BOOTSTRAP" >>  ~/.bashrc; fi;
if [ -w ~/.zshrc ]; then echo "$BOOTSTRAP" >>  ~/.zshrc; fi;
