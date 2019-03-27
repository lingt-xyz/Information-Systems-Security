from pprint import pprint
from domain_loader import domain_loader
from file_handler import file_handler
from dns_resolver import dns_resolver
from dns_resolver import multithread_dns_resolver
import threading

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

threadLock = threading.Lock()
threads = []
feedback = []

def driver(ns, des, domains):
    for domain in domains:
        mns = multithread_dns_resolver(threadLock, feedback, ns, des,  domain)
        mns.start()
        threads.append(mns)


domains = io.read('top-world')
driver("8.8.8.8", "Google DNS", domains)
# https://dudns.baidu.com/support/localdns/Address/
driver("180.76.76.76", "Baidu DNS", domains)

domains = io.read('top-categories')
driver("8.8.8.8", "Google DNS", domains)
driver("180.76.76.76", "Baidu DNS", domains)

# Wait for all threads to complete
for t in threads:
    t.join()

io.writeArray("output", feedback)
print("Exiting Main Thread")