import threading
from typing import Counter

from checkip.exceptions import IPUnresolvedError, InvalidProviderError
from checkip.providers import providers

def get_provider_instance(provider_code):
    if provider_code not in providers.keys():
        raise InvalidProviderError(provider_code)
    return providers[provider_code]()


def get_ip(provider):
    provider = get_provider_instance(provider)
    return provider.get_ip()


def get_ip_thread(provider, results):
    ip = get_ip(provider)
    results[provider] = ip


def resolve_ip(providers):  # TODO add strict mode where number of most commong IP is same sa len(providers)
    results = {}
    all_threads = []
    for provider in providers:
        t = threading.Thread(target=get_ip_thread, args=(provider, results))
        t.start()
        all_threads.append(t)

    for t in all_threads:
        t.join()
    
    ip_counts = Counter(results.values())
    if not ip_counts:
        raise IPUnresolvedError

    return ip_counts.most_common()[0][0]
