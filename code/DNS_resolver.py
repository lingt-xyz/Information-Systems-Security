import dns.resolver
from pprint import pprint

my_resolver = dns.resolver.Resolver(configure=False)
# 8.8.8.8 is Google's public DNS server
my_resolver.nameservers = ['8.8.8.8']

answer = my_resolver.query('baidu.com')

pprint(vars(answer))

for mx in answer.rrset.items:
    print(mx)
    