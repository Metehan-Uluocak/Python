import scapy.all as scapy
import subprocess as sb
import optparse


def user_input():
    parse_object = optparse.OptionParser(usage="Usage: python3 network_scanner.py -i [ip]")
    parse_object.add_option("-i", "--ipaddress", dest="ip", help="Ip range")
    (user_input, _) = parse_object.parse_args()

    if not user_input.ip:
        parse_object.error("[-] Please specify an IP range. Use python3 NetworkScanner.py -h for help.")
    
    return user_input


def scan(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_request_packet
    answered_list, _ = scapy.srp(combined_packet, timeout=3, verbose=0)

    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)



if __name__ == "__main__":
    
    print("NetScanner")

    
    input_ip = user_input()
    scan(input_ip.ip)
