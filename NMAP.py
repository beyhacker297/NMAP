nmap -sV -vvv -sC -T4 -A --script=vuln 192.168.33.161


Nmap scan report for 192.168.33.161
Host is up, received arp-response (0.22s latency).
Scanned at 2017-08-29 15:33:04 EDT for 1247s
Not shown: 988 closed ports
Reason: 988 resets
PORT      STATE SERVICE       REASON          VERSION
80/tcp    open  http          syn-ack ttl 128 iWeb
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
| http-csrf: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.33.161
|   Found the following possible CSRF vulnerabilities: 
|     
|     Path: http://192.168.33.161:80/
|     Form id: 
|     Form action: index_submit.html
|     
|     Path: http://192.168.33.161/index_submit.html
|     Form id: 
|_    Form action: index_submit.html
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-enum: 
|_  /robots.txt: Robots file
|_http-litespeed-sourcecode-download: Page: /index.php was not found. Try with an existing file.
|_http-server-header: iWeb
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
135/tcp   open  msrpc         syn-ack ttl 128 Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack ttl 128 Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds  syn-ack ttl 128 (workgroup: WORKGROUP)
3389/tcp  open  ms-wbt-server syn-ack ttl 128 Microsoft Terminal Service
|_sslv2-drown: 
5357/tcp  open  http          syn-ack ttl 128 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
49152/tcp open  msrpc         syn-ack ttl 128 Microsoft Windows RPC
49153/tcp open  msrpc         syn-ack ttl 128 Microsoft Windows RPC
49154/tcp open  msrpc         syn-ack ttl 128 Microsoft Windows RPC
49155/tcp open  msrpc         syn-ack ttl 128 Microsoft Windows RPC
49156/tcp open  msrpc         syn-ack ttl 128 Microsoft Windows RPC
49157/tcp open  msrpc         syn-ack ttl 128 Microsoft Windows RPC
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port80-TCP:V=7.25BETA2%I=7%D=8/29%Time=59A5C187%P=i686-pc-linux-gnu%r(G
SF:etRequest,32B,"HTTP/1\.1\x20200\x20OK\r\nLastModified:\x2010/3/2015\x20
SF:5:28:33\x20AM\r\nServer:\x20iWeb\r\nContent-Type:\x20text/html\r\nConte
SF:nt-Length:\x20696\r\n\r\n<!DOCTYPE\x20html>\r\n<html>\r\n<head>\r\n\t<t
SF:itle>HTML5\x20Login</title>\r\n\t<link\x20rel=\"stylesheet\"\x20href=\"
SF:normalize\.css\">\r\n\t<link\x20rel=\"stylesheet\"\x20href=\"style\.css
SF:\">\r\n</head>\r\n<body>\r\n\t<section\x20class=\"loginform\x20cf\">\r\
SF:n\t\t<form\x20name=\"login\"\x20action=\"index_submit\.html\"\x20method
SF:=\"get\"\x20accept-charset=\"utf-8\">\r\n\t\t\t<ul>\r\n\t\t\t\t<li>\r\n
SF:\t\t\t\t\t<label\x20for=\"usermail\">Email</label>\r\n\t\t\t\t\t<input\
SF:x20type=\"email\"\x20name=\"usermail\"\x20placeholder=\"yourname@email\
SF:.com\"\x20required>\r\n\t\t\t\t</li>\r\n\t\t\t\t<li>\r\n\t\t\t\t\t<labe
SF:l\x20for=\"password\">Password</label>\r\n\t\t\t\t\t<input\x20type=\"pa
SF:ssword\"\x20name=\"password\"\x20placeholder=\"password\"\x20required><
SF:/li>\r\n\t\t\t\t<li>\r\n\t\t\t\t\t<input\x20type=\"submit\"\x20value=\"
SF:Login\">\r\n\t\t\t\t</li>\r\n\t\t\t</ul>\r\n\t\t</form>\r\n\t</section>
SF:\r\n</body>\r\n</html>")%r(FourOhFourRequest,898,"HTTP/1\.1\x20404\x20N
SF:ot\x20Found\r\nServer:\x20iWeb\r\nContent-Type:\x20text/html\r\nContent
SF:-Length:\x202113\r\n\r\n<html>\r\n\r\n<head>\r\n<meta\x20http-equiv=\"C
SF:ontent-Type\"\x20content=\"text/html;\x20charset=windows-1252\">\r\n<ti
SF:tle>iWeb\x20Server\x20Error</title>\r\n<style>\r\n<!--\r\n\x20\x20\x20\
SF:x20p,\x20body,\x20td,\x20th,\x20a,\x20input,\x20select,\x20input\x20{fo
SF:nt-family:\x20Tahoma,\x20Verdana,\x20Arial,\x20Helvetica,\x20sans-serif
SF:;\x20font-size:\x2011pt}\r\n\x20\x20\x20\x20p,\x20body,\x20td,\x20a,\x2
SF:0th\x20{color:black\x20}\x20\x20\x20\x20\r\n\x20\x20\x20\x20H1\x20{\x20
SF:font-size:\x2018pt;\x20color:\x20#6699CC\x20}\r\n\x20\x20\x20\x20H2\x20
SF:{\x20font-size:\x2016pt;\x20color:\x20#6699CC\x20}\r\n\x20\x20\x20\x20H
SF:3\x20{\x20font-size:\x2014pt;\x20color:\x20black\x20}\r\n\x20\x20\x20\x
SF:20a\x20{color:#0000CC;\x20text-decoration:\x20none\x20}\r\n\x20\x20\x20
SF:\x20a:link\x20{color:#0033CC;\x20text-decoration:\x20none\x20}\r\n\x20\
SF:x20\x20\x20a:visited\x20{color:#0000AA;\x20text-decoration:\x20none\x20
SF:}\r\n\x20\x20\x20\x20a:hover\x20{color:#6666FF;\x20text-decoration:\x20
SF:underline;\x20cursor:\x20hand\x20}\r\n\t\ta:active\x20{color:#6666FF;\x
SF:20text-decoration:\x20underline\x20}\r\n\x20\x20\x20\.copyright\x20{\x2
SF:0font-size:\x208pt}\r\n-->\r\n</style>\r\n</head>\r\n\r\n<body\x20topma
SF:rgin=\"0\"\x20leftmargin=");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port445-TCP:V=7.25BETA2%I=7%D=8/29%Time=59A5C18C%P=i686-pc-linux-gnu%r(
SF:SMBProgNeg,85,"\0\0\0\x81\xffSMBr\0\0\0\0\x88\x01@\0\0\0\0\0\0\0\0\0\0\
SF:0\0\0\0@\x06\0\0\x01\0\x11\x07\0\x032\0\x01\0\x04A\0\0\0\0\x01\0\0\0\0\
SF:0\xfd\xe3\x01\0'\xc9\x1afE!\xd3\x01\xa4\x01\x08<\0\x83\[\xa3\xa5\xc7\x8
SF:8\xe6\x11W\0O\0R\0K\0G\0R\0O\0U\0P\0\0\0W\0I\0N\0-\0P\0A\0Q\0J\0G\x003\
SF:0G\0R\x004\x003\0J\0\0\0");
MAC Address: 00:50:56:89:11:A8 (VMware)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.25BETA2%E=4%D=8/29%OT=80%CT=1%CU=32517%PV=Y%DS=1%DC=D%G=Y%M=005
OS:056%TM=59A5C64F%P=i686-pc-linux-gnu)SEQ(SP=108%GCD=1%ISR=109%TI=I%II=I%S
OS:S=S%TS=7)OPS(O1=M529NW8ST11%O2=M529NW8ST11%O3=M529NW8NNT11%O4=M529NW8ST1
OS:1%O5=M529NW8ST11%O6=M529ST11)WIN(W1=2000%W2=2000%W3=2000%W4=2000%W5=2000
OS:%W6=2000)ECN(R=Y%DF=Y%T=80%W=2000%O=M529NW8NNS%CC=N%Q=)T1(R=Y%DF=Y%T=80%
OS:S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+
OS:%F=AR%O=%RD=0%Q=)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=
OS:G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=80%CD=Z)

Uptime guess: 0.045 days (since Tue Aug 29 14:48:50 2017)
Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=264 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: Host: WIN-PAQJG3GR43J; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED
|_smb-vuln-ms10-054: false
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED

TRACEROUTE
HOP RTT       ADDRESS
1   222.96 ms 192.168.33.161

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 15:53
Completed NSE at 15:53, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 15:53
Completed NSE at 15:53, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1257.93 seconds
           Raw packets sent: 2152 (99.450KB) | Rcvd: 1081 (46.754KB)