from checkip.exceptions import InvalidProviderError
from checkip.providers import providers_dict

def get_provider_instance(provider_code):
    if provider_code not in providers_dict.keys():
        raise InvalidProviderError(provider_code)
    return providers_dict[provider_code]()


def get_ip(provider):
    provider = get_provider_instance(provider)
    return provider.get_ip()
