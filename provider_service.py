class ProviderService:
    def __init__(self):
        return

    # #
    # It always returns the provider that reach the higher position
    # #
    def find_best_of(self, providers):
        new_provider = providers.pop()
        for provider in providers:
            if provider.higher_position() > new_provider.higher_position():
                new_provider = provider
        return new_provider

    def subtract(self, providers, providers_to_subtract):
        for provider_to_subtract in providers_to_subtract:
            if provider_to_subtract in providers:
                providers.remove(provider_to_subtract)
        return providers
