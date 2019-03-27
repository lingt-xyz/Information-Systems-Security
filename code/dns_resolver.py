# https://stackoverflow.com/questions/22609385/python-requests-library-define-specific-dns

from dns.resolver import Resolver
from dns.resolver import NoNameservers
from dns.resolver import NXDOMAIN
from dns.resolver import NoAnswer
from dns.exception import Timeout
from pprint import pprint
from urllib3.util import connection
import threading


class dns_resolver:
    def __init__(self, *args, **kwargs):
        pass

    def get_host(self, ns, host):
        r = Resolver(configure=False)
        r.nameservers = ns
        # 8.8.8.8 is Google's public DNS server
        # 1.2.4.8
        # r.nameservers = ['210.22.66.253']
        try:
            answers = r.query(host, 'A')
            for rdata in answers:
                return str(rdata)
        except NoNameservers:
            return "NoNameservers"
        except NXDOMAIN:
            return "NonExist"
        except NoAnswer:
            return "NoAnswer"
        except Timeout:
            return "timeout"
            # dns.exception.Timeout

    def get_response(self, ns, host_list):
        pass


class multithread_dns_resolver (threading.Thread):
    def __init__(self, lock, feedback, ns, des, domain):
        threading.Thread.__init__(self)
        self.lock = lock
        self.feedback = feedback
        self.ns = ns
        self.des = des
        self.domain = domain

    def run(self):
        print("Start querying " + self.domain + " from " + self.ns)
        resolver = dns_resolver()
        ip = resolver.get_host([self.ns], self.domain)
        print("Querying reuslt: " + ip)
        # Get lock to synchronize threads
        self.lock.acquire()
        # Free lock to release next thread
        self.feedback.append([self.domain, self.ns, self.des, ip])
        self.lock.release()
