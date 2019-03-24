from domain_loader import DomainLoader
from domain_loader import FileHandler


"""


domains = domain_loader.get_category_top_domain_from_alexa()

for domain in domains:
    print(domain)

"""

domain_loader = DomainLoader()
io = FileHandler()

if io.read('top-world'):
    pass
else:
    domains = domain_loader.get_top_domain_from_alexa()
    io.write('top-world', domains)

if io.read('top-categories'):
    pass
else:
    domains = domain_loader.get_category_top_domain_from_alexa()
    io.write('top-categories', domains)

