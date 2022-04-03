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

    # TODO testear
    def subtract(self, sorted_providers_available, filter_data):
        return [provider for provider in sorted_providers_available if
                provider not in filter_data]
