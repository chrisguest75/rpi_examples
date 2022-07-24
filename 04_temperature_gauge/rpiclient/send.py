import logging
import requests 

logger = logging.getLogger('rpiclient.send')

class send():
    def __init__(self, server, labels = {}):
        logger.info(f"Server {server}")
        self.server = server
        self.labels = labels

    def send(self, name, value):
        metric = f"{name} {value}"
        url = f"{self.server}/metrics/job/rpi"
        logger.info(f"metric {metric} url {url}")

        response = requests.post(url, data=metric, headers={'Content-Type': 'application/octet-stream'})
        if response.status_code != 200:
            print(response)
        else:
            print(response)


#http://0.0.0.0:9091/metrics/job/rpi/instance/$(hostname)/ip/$(ipconfig getifaddr en0)