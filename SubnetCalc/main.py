import ipaddress
import argparse
from os import system

# Create the parser
parser = argparse.ArgumentParser(description='IPv4 Network Subnet Calculator')

# Add the arguments
ip_help = "The IP address to calculate\nExample: 192.168.0.100/24 or 10.0.0.1/255.255.255.0\nSupports both CIDR and Subnet Mask after the slash"
parser.add_argument('-i', dest='ip', type=str, help=ip_help)
subnet_help = "The netmask to subnet (optional)\nExample: 255.255.255.0 or /24"
parser.add_argument('-s', dest='subnet', type=str, help=subnet_help)


#Function to get an IPv4 address from the user
def get_network(ip: str = None) -> (ipaddress.IPv4Network, str):
    """
    Get an IPv4 address from the user.
    """
    if ip:
        try:
            if ip.count("/") == 0: ip += "/24"
            net = ipaddress.IPv4Network(ip, strict=False)
            ip = ip.split("/")[0]
            return (net, ip)
        except ValueError:
            print("\n\033[36m[\033[31m!\033[36m]\033[0m Invalid IP Address!\n")
            exit(1)
    print()
    while True:
        try:
            in_ = input("\033[36m[\033[31m?\033[36m]\033[0m Enter an IP Address: \033[36m")
            if in_ == "": in_ = "192.168.0.100/24"
            if in_.count("/") == 0: in_ += "/24"
            net = ipaddress.IPv4Network(in_, strict=False)
            ip = in_.split("/")[0]
            return (net, ip)
        except ValueError:
            print("\n\033[36m[\033[31m!\033[36m]\033[0m Invalid IP Address!\n")
            continue



def is_ip_in_reserved_network(ip_address, reserved_network):
    try:
        # Parse the IP address and network
        ip_address = ipaddress.IPv4Address(ip_address)
        reserved_network = ipaddress.IPv4Network(reserved_network, strict=False)

        # Check if the IP address is within the reserved network
        return ip_address in reserved_network
    except ValueError:
        # Handle invalid IP address or network format
        return False



# Get user input for IP address and reserved network range
ip_address_to_check = input("Enter the IP address to check: ")
reserved_network_range = input("Enter the reserved network range (e.g., 192.168.0.0/16): ")


result = is_ip_in_reserved_network(ip_address_to_check, reserved_network_range)
print(result)

def calculate(network: (ipaddress.IPv4Network, str), subnet: str) -> None:
    """
    Calculate the network and other information.
    """

    ip = network[1]
    network = network[0]

   
    usable_hosts = list(network.hosts())

    usable_hosts = f"{usable_hosts[0]} - {usable_hosts[-1]}" if usable_hosts[0] != usable_hosts[-1] else "NA"
   
    print(f"\033[0mUsable IP Range:        \033[36m{usable_hosts}")


    print()


def main():
    system("") # Fix for ANSI escape codes on Windows
    
    args = parser.parse_args()
    
    ip = None
    if args.ip:
        ip = args.ip
    subnet = None
    if args.subnet:
        subnet = args.subnet

    network = get_network(ip)
    

    print()
    calculate(network, subnet)

if __name__ == "__main__":
    main()
