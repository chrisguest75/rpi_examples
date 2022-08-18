#!/usr/bin/env python3
"""
A skeleton OpenApi v2 interface and service.  Useful for using with Google Endpoints. 
"""

import argparse
import io
import logging
import logging.config
import os
import sys
import traceback
import ptvsd
import yaml
import platform
import time
from send import send
from ip import get_ip_address

def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.critical("Exception", exc_info=(exc_type, exc_value, exc_traceback))
    logging.critical('Unhandled Exception {0}: {1}'.format(exc_type, exc_value), extra={'exception': ''.join(traceback.format_tb(exc_traceback))})


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

if __name__ == "__main__":
    print(f"Enter {__name__}")
    with io.open("./logging_config.yaml") as f:
        logging_config = yaml.load(f, Loader=yaml.SafeLoader)

    logging.config.dictConfig(logging_config)
    logger = logging.getLogger()

    sys.excepthook = log_uncaught_exceptions

    parser = argparse.ArgumentParser(description='Temperature Monitor')
    parser.add_argument('--debugger', dest='debugger', action='store_true')
    parser.add_argument('--wait', dest='wait', action='store_true')
    parser.add_argument('--prometheus', default="http://0.0.0.0:9090", dest='prometheus', type=str, help='')
    parser.add_argument('--nic', default="en0", dest='nic', type=str, help='')
    parser.add_argument('--placement', default="frontroom", dest='placement', type=str, help='')
    parser.add_argument('--plugin', default="plugin_random", dest='plugin', type=str, help='')

    args = parser.parse_args()

    debugger = False
    if 'DEBUGGER' in os.environ:
        debugger = str2bool(os.environ['DEBUGGER'])
        logger.info(f"DEBUGGER found in environment {debugger}", extra={"debugger": debugger})
    if args.debugger:
        debugger = True

    wait = False
    if 'WAIT' in os.environ:
        wait = str2bool(os.environ['WAIT'])
        logger.info(f"WAIT found in environment {wait}", extra={"wait": wait})
    if args.wait:
        wait = True

    if debugger:
        # 5678 is the default attach port in the VS Code debug configurations
        print("Debugger activated")
        ptvsd.enable_attach(address=('0.0.0.0', 5678), redirect_output=True)
        if wait:
            logger.info("Waiting for debugger attach")
            ptvsd.wait_for_attach()
            breakpoint()

    base_url = args.prometheus 
    if 'PROMETHEUS' in os.environ:
        base_url = os.environ['PROMETHEUS']

    hostname = platform.node()
    ip = get_ip_address(args.nic)  
    placement = args.placement  
    labels = {
        "hostname": hostname,
        "ip": ip,
        "placement": placement,        
    }
    logger.info(labels)
    send = send(args.prometheus, labels)

    if args.plugin == "plugin_random":
        from plugin_random import plugin_random
        sensors = plugin_random()
    else:        
        from plugin_rainbowhat import plugin_rainbowhat
        sensors = plugin_rainbowhat()

    while True:
        readings = sensors.retrieve_values()
        temperature = readings["temperature"]
        pressure = readings["pressure"]
        send.send("temperature", f"{temperature:.2f}")
        send.send("pressure", f"{pressure:.2f}" )
        time.sleep(2)

    print(f"Exit {__name__}")
    exit(0)