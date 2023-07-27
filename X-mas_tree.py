from scapy.all import *
from scapy.layers.inet import IP, TCP

# Craft the IP and TCP layers with FIN, URG, and PSH flags set
target_ip = "10.0.2.4" #ip address of Ubuntu2
ip_packet = IP(dst=target_ip)
tcp = TCP(dport=80)

# Set the FIN, URG, ACK, RST, SYN and PSH flags in the TCP layer
tcp.flags |= "UAPRFS"  # Using the string representation for flags

# Assemble the packets
packet = ip_packet / tcp

# Send the packet
send(packet)
