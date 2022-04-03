

class ProviderService:
    def __init__(self):
        return

    # #
    # It always returns the provider that reach the higher position
    # #
    def get_best_provider_of(self, providers):
        new_provider = providers.pop()
        for provider in providers:
            if provider.higher_position() > new_provider.higher_position():
                new_provider = provider
        return new_provider

