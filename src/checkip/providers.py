import inspect
import re
import sys

import requests

from checkip.exceptions import IPNotFoundError, InvalidProviderError

IP_REGEX = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'

providers = {}

def register_provider(provider):
    if not getattr(provider, 'code', None):
        raise InvalidProviderError('Provider is missing `code` attribute')
    if provider.code in providers.keys():
        raise InvalidProviderError('Provider\'s code `{}` is already registered'.format(provider.code))

    providers[provider.code] = provider


class BaseProvider:
    def get_ip(self):
        response = requests.get(self.url)
        response.raise_for_status()

        match = re.search(IP_REGEX, response.text)
        if not match:
            raise IPNotFoundError(self.code)

        result = match.group(0)

        return result


class DyndnsProvider(BaseProvider):
    code = 'dyndns'
    url = 'http://checkip.dyndns.org/'


class FreednsProvider(BaseProvider):
    code = 'freedns'
    url = 'https://freedns.afraid.org/dynamic/check.php'


class GoogledomainsProvider(BaseProvider):
    code = 'googledomains'
    url = 'https://domains.google.com/checkip'


class HeProvider(BaseProvider):
    code = 'he'
    url = 'http://checkip.dns.he.net/'


class Ip4onlyProvider(BaseProvider):
    code = 'ip4only'
    url = 'http://ip4only.me/api/'


class IpfyProvider(BaseProvider):
    code = 'ipfy'
    url = 'https://api.ipify.org/'


class LoopiaProvider(BaseProvider):
    code = 'loopia'
    url = 'http://dns.loopia.se/checkip/checkip.php'


class MyonlineportalProvider(BaseProvider):
    code = 'myonlineportal'
    url = 'https://myonlineportal.net/checkip'


class NoipProvider(BaseProvider):
    code = 'noip'
    url = 'http://ip1.dynupdate.no-ip.com/'


class NsupdateProvider(BaseProvider):
    code = 'nsupdate'
    url = 'http://ipv4.nsupdate.info/myip'


class ZoneeditProvider(BaseProvider):
    code = 'zoneedit'
    url = 'http://dynamic.zoneedit.com/checkip.html'


class CloudflareProvider(BaseProvider):
    code = 'cloudflare'
    url = 'https://cloudflare.com/cdn-cgi/trace'


class MyipProvider(BaseProvider):
    code = 'myip'
    url = 'https://api.myip.com'


class HttpbinProvider(BaseProvider):
    code = 'httpbin'
    url = 'https://httpbin.org/ip'


# Register providers
class_members = inspect.getmembers(sys.modules[__name__], inspect.isclass)
for name, klass in class_members:
    if issubclass(klass, BaseProvider) and klass != BaseProvider:
        register_provider(klass)
