import logging
import requests 

logger = logging.getLogger('rpiclient.send')

class send():
    def __init__(self, server, labels = {}):
        logger.info(f"Server {server}")
        self.server = server
        self.labels = labels

    def send(self, name, value):
        metric = f"{name} {value}\n"

        labels = ""
        for key in self.labels:
            labels += f"/{key}/{self.labels[key]}"

        url = f"{self.server}/metrics/job/rpi{labels}"
        logger.info(f"metric {metric} url {url}")

        response = requests.post(url, data=metric, headers={'Content-Type': 'application/octet-stream'})
        if response.status_code != 200:
            print(f"{response.reason} {response.text}")
        else:
            print(f"{response.reason} {response.text}")


#http://0.0.0.0:9091/metrics/job/rpi/instance/$(hostname)/ip/$(ipconfig getifaddr en0)