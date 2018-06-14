import socket
import argparse
import ipaddress

# Need python3 - does not run under python2

parser = argparse.ArgumentParser()
parser.add_argument("subnet", help="enter subnet to scan (192.168.0.0/24)")
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
subnet = args.subnet
network = ipaddress.ip_network(subnet)

for i in network.hosts():
    i = str(i)
    # I port 88 is open (Kerberos) then computer is most likely using Active Directory
    result = sock.connect_ex((i, 88))
    if result == 0:
       print("Active Directory server found: " + i)
    else:
       continue