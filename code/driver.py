import sys
import collections
import threading
from pprint import pprint

from domain_loader import domain_loader
from file_handler import file_handler
from dns_resolver import dns_resolver
from dns_resolver import multithread_dns_resolver

sys.stdout = open("console.log", "w")

"""
Step 1:

Get the list of target domains, and write to files.
If the files have been today, this step would do nothing.
"""
domain_loader = domain_loader()
io = file_handler()

if io.read('top-world') is not None:
    pass
else:
    domains = domain_loader.get_top_domain_from_alexa()
    io.write('top-world', domains)

if io.read('top-categories') is not None:
    pass
else:
    domains = domain_loader.get_category_top_domain_from_alexa()
    io.write('top-categories', domains)


"""
Some basic test

Get dns ip

resolver = dns_resolver()

### 2. Get ip from google dns
ip = resolver.get_host(["8.8.8.8"], "www.baidu.com")
print(ip)

### 3. Get ip from baidu dns (China)
# https://dudns.baidu.com/support/localdns/Address/
ip = resolver.get_host(["180.76.76.76"], "www.google.com")
print(ip)
"""

"""
Step 2:

Test repsonse using specific nameservers
"""


dnss = []
dnss.append(["8.8.8.8", "Google DNS"])
dnss.append(["208.67.222.222", "OpenDNS DNS"]) # resolver1.opendns.com
dnss.append(["1.1.1.1", "Cloudflare DNS"])

dnss.append(["89.148.14.227", "Bahrain DNS"]) # ns.bti.com.bh.
dnss.append(["93.85.92.171", "Belarus DNS"]) # smtp2.vtroitskaya.by.
dnss.append(["180.76.76.76", "China DNS"]) # Baidu DNS # https://dudns.baidu.com/support/localdns/Address/
dnss.append(["169.158.176.75", "Cuba1 DNS"]) # toxon.mnhnc.inf.cu timeout
dnss.append(["200.55.169.234", "Cuba2 DNS"]) # no name server
dnss.append(["213.55.96.166", "Ethiopia DNS"])
dnss.append(["202.134.52.105", "India DNS"]) # ns2.phillipcapital.in.
dnss.append(["94.232.174.194", "Iran DNS"]) # dns.shecan.ir.
dnss.append(["175.45.176.16", "North Korea DNS"]) # ns2.kptc.kp
dnss.append(["209.150.154.1", "Pakistan DNS"]) # pub-dns01.zong.com.pk.
dnss.append(["46.173.223.50", "Russia DNS"]) # ns03.parking.ru.
dnss.append(["185.51.204.11", "Saudi Arabia DNS"]) # ns2.wafai.net.sa.
dnss.append(["41.202.173.250", "Sudan DNS"])
dnss.append(["82.137.200.20", "Syria DNS"]) # ns3.tarassul.sy
dnss.append(["217.174.227.242", "Turkmenistan1 DNS"])
dnss.append(["217.174.227.102", "Turkmenistan2 DNS"])
dnss.append(["213.42.43.226", "United Arab Emirates DNS"])
dnss.append(["213.146.187.177", "United Kingdom DNS"]) # 
dnss.append(["208.180.2.244", "United States DNS"]) # 208-180-2-244.com.sta.suddenlink.net.
dnss.append(["80.80.218.218", "Uzbekistan DNS"]) # 80.80.218.218.static.ip.tps.uz.
dnss.append(["103.74.113.28", "Vietnam DNS"]) # vetc-public-dns-b.vetc.com.vn.

domains = []
domains.extend(io.read('top-world'))
domains.extend(io.read('top-categories'))
domains.append("www.soen321project.com")
domains = list(dict.fromkeys(domains))

threadLock = threading.Lock()
threads = []
feedback = []

for dns in dnss:
    for domain in domains:
        mns = multithread_dns_resolver(threadLock, feedback, dns[0], dns[1], domain)
        mns.start()
        threads.append(mns)


# Wait for all threads to complete
for t in threads:
    t.join()

io.writeArray("output", feedback, True)
print("Exiting Main Thread")