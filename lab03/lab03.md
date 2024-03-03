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

The DNS namesevers for princeton.edu
