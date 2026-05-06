from scapy.all import *

packets = rdpcap("wireshark.pcapng")

syn_count=0
ports=set()

for pkt in packets:
	if pkt.haslayer(TCP):
		tcp = pkt[TCP]

		if tcp.flags=="S":
			syn_count+=1
			ports.add(tcp.dport)
			print(f"[!] SYN PACKET -> Port: {tcp.dport}")
print ("\n---SUMMARY---")
print(f"Total SYN PACKETS: {syn_count}")
print(f"Unique Ports Scanned: {len(ports)}")
