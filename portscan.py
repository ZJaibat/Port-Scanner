# importing socket for use of network communication.
# importing regular expressions to validate input.
# importing pyfiglet to print a banner.
import socket
import re
from tabnanny import verbose
import pyfiglet

# pattern to recognize IPv4 addresses.
ip_pat = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

# pattern to recognize port range.
port_pat = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535

banner = pyfiglet.figlet_format("ZSCANNER", font="war_of_w")
print(banner)

open_ports = []

# Validates the ip address syntax as well as stored the ip address
while True:
    entered_ip = input("\nWhat is the desired ip you would like to scan? ")
    if ip_pat.search(entered_ip):
        print(f"{entered_ip} is a valid IP address")
        break

# Validates the port number syntax
# multi threading is not yet implemented scanning all ports is not advised.
while True:
    print("Please enter the port range that you would like to scan. Please use the form ##-##")
    port_range = input("Enter the port range: ")
    valid_port_range = port_pat.search(port_range.replace(" ",""))
    if valid_port_range:
        port_min = int(valid_port_range.group(1))
        port_max = int(valid_port_range.group(2))
        break

# Basic socket port scanning
for port in range(port_min, port_max + 1):
    # Connect to a socket of target machine, we will need a port number and an ip address.
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Sets a time out so that we wont wait for too long on a single port.
            sock.settimeout(0.5)
            # Uses the socket object created to connect to the ip and port
            # that was entered
            sock.connect((entered_ip, port))
            # appends to the open ports list
            open_ports.append(port)
            sock.close()
    except:
        # We arent doing anything in here so just pass.
        pass
    
    # Since we only care about the open ports we will display those only
    for port in open_ports:
        # we can use f string to help with formatting.
        print(f"Port {port} is open on {entered_ip}")