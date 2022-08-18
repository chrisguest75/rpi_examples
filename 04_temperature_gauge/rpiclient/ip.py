import ifaddr
import logging

logger = logging.getLogger('rpiclient.ip')

def get_ip_address(ifname):
    adapters = ifaddr.get_adapters()

    for adapter in adapters:
        if adapter.nice_name == ifname:
            logger.info(f"Selected {adapter.nice_name}")
            for ip in adapter.ips:
                if isinstance(ip.ip, str):
                    #print("   %s/%s - %s" % (ip.ip, ip.network_prefix, type(ip.ip)))
                    return ip.ip
        else:
            logger.info(f"{adapter.nice_name}")
