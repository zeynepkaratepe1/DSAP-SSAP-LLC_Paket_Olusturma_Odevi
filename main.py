from scapy.all import *

target_mac = "ff:ff:ff:ff:ff:ff"
source_mac = "02:11:22:33:44:55"

eth = Ether(dst=target_mac, src=source_mac)

llc = LLC(dsap=0x04, ssap=0x04, ctrl=3)

payload = Raw(load="LLC DSAP SSAP test paketi")

packet = eth / llc / payload

sendp(packet, iface="Wi-Fi")
