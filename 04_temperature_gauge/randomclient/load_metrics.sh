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
echo "Press (s) for show, (d) for delete or (q) to quit"

while true; do 
    # Check for keypress *waiting very briefly.
    read -t 0.01 -r -s -N 1 
    case "${REPLY}" in
        'q'|'Q')
            break
        ;;
        's'|'S')
            mode='s'
        ;;
        'd'|'D')
            mode='d'
        ;;
        *)
            mode=''
        ;;
    esac          

    # Loop command
    pressure=$(echo "scale=2; $RANDOM / 10.0" | bc)
    temperature=$(echo "scale=2; $RANDOM / 1000.0" | bc)

    case $mode in
        '')
            echo -n "."
        ;; 
        s)
            echo "temperature $temperature, pressure $pressure"
        ;;       
        d)
            echo "Deleting..."
            curl -X DELETE http://0.0.0.0:9091/metrics/job/rpi
        ;;       
    esac

    # write metrics
    echo "temperature $temperature" | curl --data-binary @- http://0.0.0.0:9091/metrics/job/rpi/instance/$(hostname)/ip/$(ipconfig getifaddr en0)
    echo "pressure $pressure" | curl --data-binary @- http://0.0.0.0:9091/metrics/job/rpi/instance/$(hostname)/ip/$(ipconfig getifaddr en0)
    sleep 2
done