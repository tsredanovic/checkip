class InvalidProviderError(Exception):
    """Exception raised when provider is not supported.

    Attributes:
        provider -- unsupported provider
    """

    def __init__(self, provider):
        self.provider = provider
        self.message = 'Unsupported provider code'
        super().__init__(self.message)

    def __str__(self):
        return '{} -> {}'.format(self.provider, self.message)


class IPNotFoundError(Exception):
    """Exception raised when IP address is not found.

    Attributes:
        provider -- provider in who's response the IP address was not found
    """

    def __init__(self, provider):
        self.provider = provider
        self.message = 'IP not found in response'
        super().__init__(self.message)

    def __str__(self):
        return '{} -> {}'.format(self.provider, self.message)


class IPUnresolvedError(Exception):
    """Exception raised when IP address can't be resolved since non of the providers returned a valid IP address."""

    def __init__(self):
        self.message = 'None of the providers returned a valid IP'
        super().__init__(self.message)


class InvalidProviderError(Exception):
    """Exception raised when there is something wrong with provider class."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
