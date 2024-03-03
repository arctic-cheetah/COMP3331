# Lab03

## Exercise 3

### Output

```
dig www.princeton.edu

; <<>> DiG 9.18.24-1-Debian <<>> www.princeton.edu
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 44238
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 017ddb898186eea50100000065e40d3efb793d49814e9dc8 (good)
;; QUESTION SECTION:
;www.princeton.edu.             IN      A

;; ANSWER SECTION:
www.princeton.edu.      2501    IN      CNAME   www.princeton.edu.cdn.cloudflare.net.
www.princeton.edu.cdn.cloudflare.net. 300 IN A  104.18.4.101
www.princeton.edu.cdn.cloudflare.net. 300 IN A  104.18.5.101

;; Query time: 12 msec
;; SERVER: 129.94.242.2#53(129.94.242.2) (UDP)
;; WHEN: Sun Mar 03 16:40:14 AEDT 2024
;; MSG SIZE  rcvd: 156
```

### 3.1) What is the IP address of [www.princeton.edu](www.princeton.edu) ? What type of DNS query is sent to get this answer?

The primary IP address of [www.princeton.edu](www.princeton.edu) is 104.18.4.101. It also has a secondary IP address with: 104.18.5.101.

The DNS query is of type 'A' record.

### 3.2) What is the canonical name for the Princeton webserver (i.e., <www.princeton.edu> )? Suggest a reason for having an alias for this server

The canonical name is [www.princeton.edu.cdn.cloudflare.net.](www.princeton.edu.cdn.cloudflare.net.)
Benefits for Princeton University for using CNAME(alias):

- allows the creation of subdomains. Such as net.princeton.edu or oit.princton.edu
- enables the use of external services such as cloudflare to prevent network attacks
- Makes it easier to remember the url by exluding the trailing cloudflare.net

### 3.3) What can you make of the rest of the response/what is it used for (i.e., the details available in the DNS response (cookies and other fields))?

On my current VLAB machine, the rest of the response shows that:

- I had 1 query
- I received 3 answers, 0 from authority and 1 from additional
- I also see an optional section for (Extension Mechanisms for DNS) EDNS. Under these include the EDNS version used, flags, the size of the opt record and cookie which is used for security reasons.
- Followed by the answer question to my DNS query
- Lastly, the query time, server IP and date and message size of the query are at the end.

However, on my personal machine, we the additional and authority section included:

```
; <<>> DiG 9.19.17-2~kali1-Kali <<>> www.princeton.edu
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 8290
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 5, ADDITIONAL: 11

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 0ca7b547b54524e7e9fe9a4665e4050df8ff1e218da6fcc5 (good)
;; QUESTION SECTION:
;www.princeton.edu.             IN      A

;; ANSWER SECTION:
www.princeton.edu.      3600    IN      CNAME   www.princeton.edu.cdn.cloudflare.net.
www.princeton.edu.cdn.cloudflare.net. 300 IN A  104.18.4.101
www.princeton.edu.cdn.cloudflare.net. 300 IN A  104.18.5.101

;; AUTHORITY SECTION:
cloudflare.net.         111793  IN      NS      ns2.cloudflare.net.
cloudflare.net.         111793  IN      NS      ns4.cloudflare.net.
cloudflare.net.         111793  IN      NS      ns5.cloudflare.net.
cloudflare.net.         111793  IN      NS      ns1.cloudflare.net.
cloudflare.net.         111793  IN      NS      ns3.cloudflare.net.

;; ADDITIONAL SECTION:
ns1.cloudflare.net.     491     IN      A       173.245.59.31
ns2.cloudflare.net.     491     IN      A       198.41.222.131
ns3.cloudflare.net.     491     IN      A       198.41.222.31
ns4.cloudflare.net.     491     IN      A       198.41.223.131
ns5.cloudflare.net.     491     IN      A       198.41.223.31
ns1.cloudflare.net.     111793  IN      AAAA    2400:cb00:2049:1::adf5:3b1f
ns2.cloudflare.net.     111793  IN      AAAA    2400:cb00:2049:1::c629:de83
ns3.cloudflare.net.     111793  IN      AAAA    2400:cb00:2049:1::c629:de1f
ns4.cloudflare.net.     111793  IN      AAAA    2400:cb00:2049:1::c629:df83
ns5.cloudflare.net.     111793  IN      AAAA    2400:cb00:2049:1::c629:df1f

;; Query time: 16 msec
;; SERVER: 192.168.0.1#53(192.168.0.1) (UDP)
;; WHEN: Sun Mar 03 16:05:17 AEDT 2024
;; MSG SIZE  rcvd: 466
```

And the Authority section shows the available resource records (RR) to available authoritative name servers to the query. While the additional section shows RR's that relate to the query on my home-machine.

### 3.4) What is the IP address of the local nameserver for your machine?

At the end of the dig output, I can see that my server IP address of the local name server for my VLAB machine is: 129.94.242.2

### 3.5) What are the DNS nameservers for the " princeton.edu ” domain (note: the domain name is princeton.edu and not <www.princeton.edu> . This is an example of what is referred to as the apex/naked domain)? Find their IP addresses. Which DNS query type is used to obtain this information?

Running the command:

```
dig princeton.edu ns
; <<>> DiG 9.18.24-1 <<>> princeton.edu ns
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 31163
;; flags: qr rd ra; QUERY: 1, ANSWER: 9, AUTHORITY: 0, ADDITIONAL: 19

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: e40d59a49b2266290100000065e41e55d563f83f099a1e23 (good)
;; QUESTION SECTION:
;princeton.edu.   IN NS

;; ANSWER SECTION:
princeton.edu.  15615 IN NS a3-67.akam.net.
princeton.edu.  15615 IN NS a24-66.akam.net.
princeton.edu.  15615 IN NS a20-65.akam.net.
princeton.edu.  15615 IN NS a1-158.akam.net.
princeton.edu.  15615 IN NS ns5.dnsmadeeasy.com.
princeton.edu.  15615 IN NS ns6.dnsmadeeasy.com.
princeton.edu.  15615 IN NS a6-64.akam.net.
princeton.edu.  15615 IN NS a7-65.akam.net.
princeton.edu.  15615 IN NS ns7.dnsmadeeasy.com.

;; ADDITIONAL SECTION:
ns5.dnsmadeeasy.com. 41968 IN A 208.94.148.13
ns6.dnsmadeeasy.com. 77983 IN A 208.80.124.13
ns7.dnsmadeeasy.com. 36492 IN A 208.80.126.13
a3-67.akam.net.  22264 IN A 96.7.49.67
a6-64.akam.net.  28430 IN A 23.211.133.64
a7-65.akam.net.  1756 IN A 23.61.199.65
a1-158.akam.net. 15037 IN A 193.108.91.158
a20-65.akam.net. 69875 IN A 95.100.175.65
a24-66.akam.net. 19060 IN A 2.16.130.66
ns5.dnsmadeeasy.com. 41968 IN AAAA 2600:1800:5::1
ns6.dnsmadeeasy.com. 84062 IN AAAA 2600:1801:6::1
ns7.dnsmadeeasy.com. 53220 IN AAAA 2600:1802:7::1
a3-67.akam.net.  64478 IN AAAA 2600:1408:1c::43
a6-64.akam.net.  28430 IN AAAA 2600:1401:1::40
a7-65.akam.net.  62739 IN AAAA 2600:1406:32::41
a1-158.akam.net. 43798 IN AAAA 2600:1401:2::9e
a20-65.akam.net. 69875 IN AAAA 2a02:26f0:67::41
a24-66.akam.net. 19060 IN AAAA 2600:1480:9800::42

;; Query time: 0 msec
;; SERVER: 129.94.242.2#53(129.94.242.2) (UDP)
;; WHEN: Sun Mar 03 17:53:09 AEDT 2024
;; MSG SIZE  rcvd: 666
```

The DNS namesevers for princeton.edu are:

```
princeton.edu.  15615 IN NS ns5.dnsmadeeasy.com.
princeton.edu.  15615 IN NS ns6.dnsmadeeasy.com.
princeton.edu.  15615 IN NS ns7.dnsmadeeasy.com.
princeton.edu.  15615 IN NS a3-67.akam.net.
princeton.edu.  15615 IN NS a6-64.akam.net.
princeton.edu.  15615 IN NS a7-65.akam.net.
princeton.edu.  15615 IN NS a1-158.akam.net.
princeton.edu.  15615 IN NS a20-65.akam.net.
princeton.edu.  15615 IN NS a24-66.akam.net.
```

The corresponding IPv4 addresses of the name servers are found in the additional section which are:

```
;; ADDITIONAL SECTION:
ns5.dnsmadeeasy.com. 41968 IN A 208.94.148.13
ns6.dnsmadeeasy.com. 77983 IN A 208.80.124.13
ns7.dnsmadeeasy.com. 36492 IN A 208.80.126.13
a3-67.akam.net.  22264 IN A 96.7.49.67
a6-64.akam.net.  28430 IN A 23.211.133.64
a7-65.akam.net.  1756 IN A 23.61.199.65
a1-158.akam.net. 15037 IN A 193.108.91.158
a20-65.akam.net. 69875 IN A 95.100.175.65
a24-66.akam.net. 19060 IN A 2.16.130.66
```

This is an **NS (Name server) query**

### 3.6) What is the DNS name associated with the IP address 198.54.223.213 ? Which DNS query type is used to obtain this information?

Running the reverse lookup in dig with the '-x' flag:

```
dig -x 198.54.223.213

; <<>> DiG 9.18.24-1 <<>> -x 198.54.223.213
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 48310
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: c5fb69160411c7010100000065e422c5e387f3a71d81182a (good)
;; QUESTION SECTION:
;213.223.54.198.in-addr.arpa.   IN      PTR

;; ANSWER SECTION:
213.223.54.198.in-addr.arpa. 84458 IN   PTR     cput.ac.za.

;; Query time: 0 msec
;; SERVER: 129.94.242.2#53(129.94.242.2) (UDP)
;; WHEN: Sun Mar 03 18:12:05 AEDT 2024
;; MSG SIZE  rcvd: 108
```

The query type is a **PTR(Pointer Resource Record)** which points to a canonical name and can be used for reverse DNS lookups.

### 3.7) Run, dig and query the CSE nameserver (129.94.242.2) for the mail servers for google.com (again, the domain name is google.com, not <www.google.com> ). Did you get an authoritative answer? Why? (HINT: Just because a response contains information in the authoritative part of the DNS response message does not mean it came from an authoritative name server. You should examine the flags in the response message to determine the answer)

I did not receive an authoritative answer. This is because in the AA(authoritative answer) flag in the query is absent.

```
dig @129.94.242.2 google.com MX

; <<>> DiG 9.18.24-1 <<>> 
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 51500
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 0b15dd6d83bd8fa20100000065e4291f703fbd7ce3386cfe (good)
;; QUESTION SECTION:
;google.com.                    IN      MX

;; ANSWER SECTION:
google.com.             55      IN      MX      10 smtp.google.com.

;; Query time: 0 msec
;; SERVER: 129.94.242.2#53(129.94.242.2) (UDP)
;; WHEN: Sun Mar 03 18:39:11 AEDT 2024
;; MSG SIZE  rcvd: 88
```

### 3.8) Repeat the above (i.e. Question 7), but use one of the nameservers obtained in Question 5. What is the result?

Choose the name server ns5.dnsmadeeasy.com (208.94.148.13)

Again, there was no authoritative answer

```
dig @208.94.148.13 google.com MX
; <<>> DiG 9.18.24-1 <<>> 
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: REFUSED, id: 30904
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1280
;; QUESTION SECTION:
;google.com.   IN MX

;; Query time: 4 msec
;; SERVER: 208.94.148.13#53(208.94.148.13) (UDP)
;; WHEN: Sun Mar 03 19:57:55 AEDT 2024
;; MSG SIZE  rcvd: 39
```

### 3.9) Obtain the authoritative answer for the mail servers for google.com. What type of DNS query is sent to obtain this information?

First we get the Names servers for google.com:

```
dig google.com NS
; <<>> DiG 9.18.24-1 <<>> 
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 54825
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 9

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: e49c7d9d01be8c400100000065e43daf07b25d10ab441b7d (good)
;; QUESTION SECTION:
;google.com.   IN NS

;; ANSWER SECTION:
google.com.  137193 IN NS ns4.google.com.
google.com.  137193 IN NS ns1.google.com.
google.com.  137193 IN NS ns2.google.com.
google.com.  137193 IN NS ns3.google.com.

;; ADDITIONAL SECTION:
ns1.google.com.  313797 IN A 216.239.32.10
ns2.google.com.  228366 IN A 216.239.34.10
ns3.google.com.  677 IN A 216.239.36.10
ns4.google.com.  41022 IN A 216.239.38.10
ns1.google.com.  313797 IN AAAA 2001:4860:4802:32::a
ns2.google.com.  215136 IN AAAA 2001:4860:4802:34::a
ns3.google.com.  677 IN AAAA 2001:4860:4802:36::a
ns4.google.com.  43210 IN AAAA 2001:4860:4802:38::a

;; Query time: 0 msec
;; SERVER: 129.94.242.2#53(129.94.242.2) (UDP)
;; WHEN: Sun Mar 03 20:06:55 AEDT 2024
;; MSG SIZE  rcvd: 315

```

Next we dig from ns1.google.com for the google.com mail server and using the MX resource record query.

```
dig @ns1.google.com google.com MX

; <<>> DiG 9.18.24-1-Debian <<>> @ns1.google.com google.com MX
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 13801
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 10
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;google.com.   IN MX

;; ANSWER SECTION:
google.com.  300 IN MX 10 smtp.google.com.

;; ADDITIONAL SECTION:
smtp.google.com. 300 IN A 142.251.10.26
smtp.google.com. 300 IN A 142.251.12.27
smtp.google.com. 300 IN A 142.251.12.26
smtp.google.com. 300 IN A 172.217.194.27
smtp.google.com. 300 IN A 172.217.194.26
smtp.google.com. 300 IN AAAA 2404:6800:4003:c0f::1a
smtp.google.com. 300 IN AAAA 2404:6800:4003:c11::1b
smtp.google.com. 300 IN AAAA 2404:6800:4003:c11::1a
smtp.google.com. 300 IN AAAA 2404:6800:4003:c04::1b

;; Query time: 96 msec
;; SERVER: 216.239.32.10#53(ns1.google.com) (UDP)
;; WHEN: Sun Mar 03 20:08:16 AEDT 2024
;; MSG SIZE  rcvd: 252

```

### 3.10) In this exercise, you simulate the iterative DNS query process to find the IP address of your machine (e.g. lyre00.cse.unsw.edu.au). If you are using VLAB then find the IP address of one of the following: lyre00.cse.unsw.edu.au, lyre01.cse.unsw.edu.au, flute00.cse.unsw.edu.au or flute01.cse.unsw.edu.au. First, find the name server (query type NS) of the "." domain (root domain). Query this nameserver to find the authoritative name server for the "au." domain. Query this second server to find the authoritative nameserver for the "edu.au." domain. Now query this nameserver to find the authoritative nameserver for "unsw.edu.au". Next, query the nameserver of unsw.edu.au to find the authoritative name server of cse.unsw.edu.au. Now, query the nameserver of cse.unsw.edu.au to find your host's IP address. How many DNS servers do you have to query for an authoritative answer?

Using lyre00.cse.unsw.edu.au, I queried:

1) j.root-servers.net
2) q.au
3) r.au
4) ns1.unsw.edu.au
5) maestro.orchestra.cse.unsw.edu.au

So it took 5 DNS server queries to get an authoratitve answer  for lyre00.cse.unsw.edu.au

1) Get the root name server:

```
dig . NS
; <<>> DiG 9.18.24-1 <<>> 
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 24288
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 13, AUTHORITY: 0, ADDITIONAL: 27

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 66f0d05d85bda2a80100000065e4474abb4308f57c844c2d (good)
;; QUESTION SECTION:
;.    IN NS

;; ANSWER SECTION:
.   193492 IN NS j.root-servers.net.
.   193492 IN NS l.root-servers.net.
.   193492 IN NS i.root-servers.net.
.   193492 IN NS f.root-servers.net.
.   193492 IN NS c.root-servers.net.
.   193492 IN NS b.root-servers.net.
.   193492 IN NS h.root-servers.net.
.   193492 IN NS d.root-servers.net.
.   193492 IN NS k.root-servers.net.
.   193492 IN NS g.root-servers.net.
.   193492 IN NS a.root-servers.net.
.   193492 IN NS e.root-servers.net.
.   193492 IN NS m.root-servers.net.
....
;; Query time: 0 msec
;; SERVER: 129.94.242.2#53(129.94.242.2) (UDP)
;; WHEN: Sun Mar 03 20:47:54 AEDT 2024
;; MSG SIZE  rcvd: 851

```

2) Query the "j.root-servers.net" name server for ".au":

```
dig @j.root-servers.net au

; <<>> DiG 9.18.24-1 <<>> 
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 60149
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 4, ADDITIONAL: 9
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1472
;; QUESTION SECTION:
;au.    IN A

;; AUTHORITY SECTION:
au.   172800 IN NS q.au.
au.   172800 IN NS r.au.
au.   172800 IN NS s.au.
au.   172800 IN NS t.au.

;; ADDITIONAL SECTION:
q.au.   172800 IN A 65.22.196.1
r.au.   172800 IN A 65.22.197.1
s.au.   172800 IN A 65.22.198.1
t.au.   172800 IN A 65.22.199.1
q.au.   172800 IN AAAA 2a01:8840:be::1
r.au.   172800 IN AAAA 2a01:8840:bf::1
s.au.   172800 IN AAAA 2a01:8840:c0::1
t.au.   172800 IN AAAA 2a01:8840:c1::1

;; Query time: 16 msec
;; SERVER: 192.58.128.30#53(j.root-servers.net) (UDP)
;; WHEN: Sun Mar 03 20:53:19 AEDT 2024
;; MSG SIZE  rcvd: 271
```

3) Query the "q.au" name server for "edu.au":

```
dig @q.au edu.au. NS

; <<>> DiG 9.18.24-1 <<>>
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 7108
;; flags: qr aa rd; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;edu.au.    IN NS

;; ANSWER SECTION:
edu.au.   900 IN NS r.au.
edu.au.   900 IN NS s.au.
edu.au.   900 IN NS t.au.
edu.au.   900 IN NS q.au.
edu.au.   900 IN NS a.au.

;; Query time: 24 msec
;; SERVER: 65.22.196.1#53(q.au) (UDP)
;; WHEN: Sun Mar 03 21:05:50 AEDT 2024
;; MSG SIZE  rcvd: 115
```

4) Query "r.au" for "unsw.edu.au" :

```
dig @r.au unsw.edu.au NS

; <<>> DiG 9.18.24-1 <<>>
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 48570
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 3, ADDITIONAL: 6
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;unsw.edu.au.   IN NS

;; AUTHORITY SECTION:
unsw.edu.au.  900 IN NS ns1.unsw.edu.au.
unsw.edu.au.  900 IN NS ns3.unsw.edu.au.
unsw.edu.au.  900 IN NS ns2.unsw.edu.au.

;; ADDITIONAL SECTION:
ns1.unsw.edu.au. 900 IN A 129.94.0.192
ns2.unsw.edu.au. 900 IN A 129.94.0.193
ns3.unsw.edu.au. 900 IN A 192.155.82.178
ns1.unsw.edu.au. 900 IN AAAA 2001:388:c:35::1
ns2.unsw.edu.au. 900 IN AAAA 2001:388:c:35::2

;; Query time: 24 msec
;; SERVER: 65.22.197.1#53(r.au) (UDP)
;; WHEN: Sun Mar 03 21:09:35 AEDT 2024
;; MSG SIZE  rcvd: 198

```

5) Query "ns1.unsw.edu.au" name server for "cse.unsw.edu.au"

```
dig @ns1.unsw.edu.au cse.unsw.edu.au NS

; <<>> DiG 9.18.24-1-Debian <<>> @ns1.unsw.edu.au cse.unsw.edu.au NS
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 13986
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 2, ADDITIONAL: 5
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;cse.unsw.edu.au.  IN NS

;; AUTHORITY SECTION:
cse.unsw.edu.au. 300 IN NS maestro.orchestra.cse.unsw.edu.au.
cse.unsw.edu.au. 300 IN NS beethoven.orchestra.cse.unsw.edu.au.

;; ADDITIONAL SECTION:
beethoven.orchestra.cse.unsw.edu.au. 300 IN A 129.94.172.11
beethoven.orchestra.cse.unsw.edu.au. 300 IN A 129.94.208.3
beethoven.orchestra.cse.unsw.edu.au. 300 IN A 129.94.242.2
maestro.orchestra.cse.unsw.edu.au. 300 IN A 129.94.242.33

;; Query time: 8 msec
;; SERVER: 129.94.0.192#53(ns1.unsw.edu.au) (UDP)
;; WHEN: Sun Mar 03 21:12:59 AEDT 2024
;; MSG SIZE  rcvd: 164
```

6) Query "maestro.orchestra.cse.unsw.edu.au."

```
 dig  maestro.orchestra.cse.unsw.edu.au. NS

; <<>> DiG 9.18.24-1-Debian <<>> maestro.orchestra.cse.unsw.edu.au. NS
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 2704
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: f72b6c5ca4dd9f2a0100000065e44dd0a2c238bb24700598 (good)
;; QUESTION SECTION:
;maestro.orchestra.cse.unsw.edu.au. IN NS

;; AUTHORITY SECTION:
orchestra.cse.unsw.EDU.AU. 3600 IN SOA maestro.orchestra.cse.unsw.EDU.AU. hostmaster.cse.unsw.edu.au. 2024022900 3600 300 1209600 3600

;; Query time: 0 msec
;; SERVER: 129.94.242.2#53(129.94.242.2) (UDP)
;; WHEN: Sun Mar 03 21:15:44 AEDT 2024
;; MSG SIZE  rcvd: 185

```

### 3.11) Can one physical machine have several names and/or IP addresses associated with it?

Yes, one machine can have several names and IP addresses. For example, in the above an IP address can map to multiple names. Also, a computer may have multiple network cards and in turn, will have several IP addresses.
