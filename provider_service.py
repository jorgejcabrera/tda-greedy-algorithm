class ProviderService:
    def __init__(self):
        return

    # #
    # It always returns the provider that reach the higher position
    # #
    def find_the_best_of(self, providers):
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

    # #
    # The providers must be sorted by their lower position
    # #
    def sort(self, providers):
        return sorted(providers, key=lambda x: x.lower_position())

    def find_all_with_coverage_below(self, providers, position):
        return list(
            filter(lambda provider: provider.lower_position() < position, providers))
