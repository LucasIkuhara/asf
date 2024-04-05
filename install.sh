#!/bin/sh
echo '''
export ASF_HOME=$(pwd)
asf() {
  TARGET=/tmp/asf_target
  python3 $ASF_HOME/path_resolver.py "$@" && cd $(cat "$TARGET")
}
'''