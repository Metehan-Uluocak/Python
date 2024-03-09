import scapy.all as scapy
from scapy.layers import http
import optparse

def user_input():
    parse_object = optparse.OptionParser(usage="python3 packet_listener.py -i [interface]")
    parse_object.add_option("-i","--interface",dest="interface",help="Interface")
    user_input , _ = parse_object.parse_args()
    if not user_input.interface:
        user_input.interface = input("Enter the interface:")
    return user_input


def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=analyze_packets)
    

def analyze_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

if __name__ == "__main__":
    user_in = user_input()
    interface = user_in.interface
    sniff(interface)