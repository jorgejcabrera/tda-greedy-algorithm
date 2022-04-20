from provider_service import ProviderService


class FindProvidersToHireUseCase:

    def __init__(self):
        self.service = ProviderService()

    def invoke_v1(self, providers, target_position):
        sorted_providers = self.service.sort(providers)
        coverage = 0
        providers_to_hire = []

        while coverage < target_position and len(sorted_providers) > 0:
            filtered_providers = self.service.find_all_with_coverage_below(sorted_providers, coverage)
            sorted_providers = self.service.subtract(sorted_providers, filtered_providers)
            new_provider = self.service.find_the_best_of(filtered_providers)
            providers_to_hire.append(new_provider)
            coverage = new_provider.higher_position()
        return providers_to_hire

    def invoke_v2(self, providers, target_position):
        sorted_providers = self.service.sort(providers)
        coverage = 0
        providers_to_hire = []

        while coverage < target_position and len(sorted_providers) > 0:
            best_provider = sorted_providers.pop(0)
            while len(sorted_providers) > 0 and sorted_providers[0].lower_position() <= coverage:
                next_provider = sorted_providers.pop(0)
                if next_provider.higher_position() >= best_provider.higher_position():
                    best_provider = next_provider
            coverage = best_provider.higher_position()
            providers_to_hire.append(best_provider)
        return providers_to_hire
