import ifaddr

def get_ip_address(ifname):
    adapters = ifaddr.get_adapters()

    for adapter in adapters:
        if adapter.nice_name == ifname:
            #print("IPs of network adapter " + adapter.nice_name)
            for ip in adapter.ips:
                if isinstance(ip.ip, str):
                    #print("   %s/%s - %s" % (ip.ip, ip.network_prefix, type(ip.ip)))
                    return ip.ip
        #else:
        #    print(f"NIC: {adapter.nice_name}")
