# anonymous_ldap_scanner
A tool to check LDAP services for anonymous bind and directory readability

usage: python anonymous-ldap-scan.py [-h] --server SERVER --port PORT --ssl SSL

options:

     -h, --help       show this help message and exit
  
     --server SERVER  The IP address of the LDAP server
  
     --port PORT      The TCP port to connect to. (usually 389 or 636)
  
     --ssl SSL        True for SSL/TLS or False for no SSL/TLS
  
NOTE:
   To check a list of servers, place the IP addresses in a file, one IP per line and run the tool like this:
     
          for i in $(cat <filename>); do python anonymous_ldap_scanner.py --server $i --port <port> --ssl <True or False>
