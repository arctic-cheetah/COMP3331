import os

q2Websites = [
    "www.google.co",
    "www.columbia.edu",
    "www.wikipedia.org",
    "ec.ho",
    "hhh.gs",
    "defence.gov.au",
    "yes.no",
    "one.one.one.one",
    "theguardian.com",
    "xn--i-7iq.ws"
]

q3bWebsites = [
    "jhu.edu",
    "usp.br ",
    "ed.ac.uk"
]
# os.system("ls -l")

def q2 ():
    i = 1
    for link in q2Websites:
        print(f"Testing Link #{i}: \n\n")
        os.system(f"ping -c 1 {link}")
        print("________________________________________________________________________________________")
        print("\n")
        i+=1

def q3a ():
    i = 0
    os.system(f"traceroute usi.ch")

def q3b():
    i = 1
    for link in q3bWebsites:
        print(f"Testing Link #{i}: \n\n")
        os.system(f"traceroute {link}")
        print("________________________________________________________________________________________")
        print("\n")
        i+=1

# q1()
q3b()