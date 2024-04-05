#!/bin/sh
echo '''
export ASF_HOME=$(pwd)
asf() {
  TARGET=/tmp/asf_target
  python3 $ASF_HOME/asf.py "$@" && cd $(cat "$TARGET")
}
'''