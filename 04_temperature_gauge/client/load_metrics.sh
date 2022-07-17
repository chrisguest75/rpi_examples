#!/usr/bin/env bash
#Use !/bin/bash -x  for debugging 
set -f -o pipefail

readonly SCRIPT_NAME=$(basename "$0")
readonly SCRIPT_PATH=${0}
# shellcheck disable=SC2034
readonly HOME_DIR=~
if [[ $(command -v greadlink) ]]; then 
    # mac requires 'brew install coreutils'
    readonly SCRIPT_FULL_PATH="$(dirname "$(greadlink -f "$0")")/${SCRIPT_NAME}"
else
    readonly SCRIPT_FULL_PATH="$(dirname "$(readlink -f "$0")")/${SCRIPT_NAME}"
fi 
readonly SCRIPT_DIR=$(dirname "$SCRIPT_FULL_PATH")

mode=''
echo "Press (s) for show or (q) to quit"

while true; do 
    random=$RANDOM  
    # Check for keypress *waiting very briefly.
    read -t 0.01 -r -s -N 1 
    case "${REPLY}" in
        'q'|'Q')
            break
        ;;
        's'|'S')
            mode='s'
        ;;
        *)
            mode=''
        ;;
    esac          

    # Loop command
    if [[ "$mode" == '' ]];then
        echo -n "."
    elif  [[ "$mode" == 's' ]];then
        echo "--$random--"
    fi

    echo "some_metric $random" | curl --data-binary @- http://0.0.0.0:9091/metrics/job/some_job
    sleep 2
done