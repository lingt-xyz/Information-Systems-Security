import dns.resolver
from pprint import pprint

my_resolver = dns.resolver.Resolver(configure=False)
# 8.8.8.8 is Google's public DNS server
my_resolver.nameservers = ['8.8.8.8']

answer = my_resolver.query('baidu.com')

pprint(vars(answer))

for mx in answer.rrset.items:
    print(mx)
    
    
    
    https://stackoverflow.com/questions/22609385/python-requests-library-define-specific-dns
    

    from urllib3.util import connection


_orig_create_connection = connection.create_connection


def patched_create_connection(address, *args, **kwargs):
    """Wrap urllib3's create_connection to resolve the name elsewhere"""
    # resolve hostname to an ip address; use your own
    # resolver here, as otherwise the system resolver will be used.
    host, port = address
    hostname = your_dns_resolver(host)

    return _orig_create_connection((hostname, port), *args, **kwargs)


connection.create_connection = patched_create_connection

def myResolver(host,dnssrv): r = dns.resolver.Resolver() r.nameservers = dnssrv answers = r.query(host, 'A') for rdata in answers: return str(rdata)
