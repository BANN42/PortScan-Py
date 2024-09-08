import scapy.all as scapy
import socket
import time
class PortScanner:
     def __init__(self, iface, ip):
         self.iface = iface
         self.ip = ip
     
     def s_ARP(self):
            arp_request = scapy.ARP(pdst=self.ip)
            broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast/arp_request
            answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
            return answered_list


