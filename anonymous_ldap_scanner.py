from termcolor import colored
import argparse
import ldap3
import json

parser = argparse.ArgumentParser()
parser.add_argument("--server", help='The IP address of the LDAP server', required=True)
parser.add_argument("--port", help='The TCP port to connect to. (usually 389 or 636)', required=True)
parser.add_argument("--ssl", help='True for SSL/TLS or False for no SSL/TLS', required=True)

args = parser.parse_args()

ldap_server = args.server
port = int(args.port)
if (args.ssl == "False"):
        ssl = False
else:
        ssl = True

server = ldap3.Server(ldap_server, get_info=ldap3.ALL, port=port, use_ssl=ssl, connect_timeout=3)
connection=ldap3.Connection(server)

if (connection.bind()):
        print(colored("[*] Anonymous Bind Successful! " + ldap_server, "green"))
        server_info = json.loads(server.info.to_json())
        naming_context = server_info['raw']['defaultNamingContext']
        print("Default naming context = " + naming_context[0])
        if (connection.search(naming_context[0], '(objectclass=*)')):
                print(colored("[*] Directory contents readable!\n", "green"))
        else:
                print(colored("[-] Directory not readable\n", "red"))
else:
        print(colored("[-] Anonymous Bind Failed." + ldap_server + "\n", "red"))
