import subprocess
import optparse
import re

def get_current_mac(interface):
    try:
        eth_text = subprocess.check_output(["sudo", "ifconfig", interface]).decode("utf-8")  
        current_mac = re.search(r"\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}", eth_text)
        if current_mac:
            return current_mac.group(0)
        else:
            print("Could not read MAC address.")
            return None
    except Exception as e:
        print(f"There was an error: {e}")
        return None

def change_mac(interface, new_mac):
    try:
        subprocess.call(["sudo", "ifconfig", interface, "down"])
        subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["sudo", "ifconfig", interface, "up"])
    except Exception as e:
        print(f"There was an error changing the MAC address: {e}")

def user_input():
    parse_object = optparse.OptionParser()
    parse_object = optparse.OptionParser(usage="Usage: python3 mac_changer.py -i [interface] -m [new_mac]")
    parse_object.add_option("-i", "--interface", dest="interface", help="Interface to change")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="New MAC address")
    (user_input, _) = parse_object.parse_args()
    return user_input.interface, user_input.mac_address

def control_mac_change(initial_mac, interface):
    current_mac = get_current_mac(interface)

    if current_mac and current_mac != initial_mac:
        print(f"MAC address changed successfully: {initial_mac} -> {current_mac}")
    else:
        print("Something went wrong.Please try different mac address.")

if __name__ == "__main__":
    print("Mac Changer")
    interface, new_mac = user_input()
    
    initial_mac = get_current_mac(interface)
    print(f"Current MAC address: {initial_mac}")

    change_mac(interface, new_mac)
    control_mac_change(initial_mac, interface)
