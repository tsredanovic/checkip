from checkip.providers import providers_dict

class InvalidProviderError(Exception):
    """Exception raised when provider is not supported.

    Attributes:
        provider -- unsupported provider
    """

    def __init__(self, provider):
        self.provider = provider
        self.message = 'Unsupported provider code - use one of: {}'.format(sorted([provider_code for provider_code in providers_dict.keys()]))
        super().__init__(self.message)

    def __str__(self):
        return '{} -> {}'.format(self.provider, self.message)