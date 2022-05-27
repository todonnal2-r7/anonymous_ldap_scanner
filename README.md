# anonymous_ldap_scanner
A tool to check LDAP services for anonymous bind and directory readability

usage: anonymous-ldap-scan.py [-h] --server SERVER --port PORT --ssl SSL

options:

     -h, --help       show this help message and exit
  
     --server SERVER  The IP address of the LDAP server
  
     --port PORT      The TCP port to connect to. (usually 389 or 636)
  
     --ssl SSL        True for SSL/TLS or False for no SSL/TLS
  
