#!/bin/bash

python -m pip install atcoder-tools
python -m pip install markupsafe==2.0.1
WORK_DIR=$(cd $(dirname $0) && pwd)
ATCODER_DIR=$(python -m pip show atcoder-tools | grep Location: | sed -e 's/Location: //g')
cd ${ATCODER_DIR}/atcodertools/common
patch -p1 < ${WORK_DIR}/atcoder_tools.patch
