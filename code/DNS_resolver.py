from urllib3.util import connection


_orig_create_connection = connection.create_connection


def patched_create_connection(address, *args, **kwargs):
    """Wrap urllib3's create_connection to resolve the name elsewhere"""
    # resolve hostname to an ip address; use your own
    # resolver here, as otherwise the system resolver will be used.
    host, port = address
    hostname = dns_resolver(host)

    return _orig_create_connection((hostname, port), *args, **kwargs)


def dsn_resolver(host):
    return ''



connection.create_connection = patched_create_connection
