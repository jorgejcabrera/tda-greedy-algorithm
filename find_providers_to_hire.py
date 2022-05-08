from provider_service import ProviderService, SolutionNotFound


class FindProvidersToHireUseCase:

    def __init__(self):
        self.service = ProviderService()

    def invoke(self, providers, target_position):
        sorted_providers = self.service.sort(providers)
        coverage = 0
        providers_to_hire = []

        while coverage < target_position and len(sorted_providers) > 0:
            best_provider = sorted_providers.pop(0)
            if not best_provider.is_below(coverage):
                print("There isn't an available provider between positions:", coverage, "and",
                      best_provider.lower_position())
                raise SolutionNotFound()
            while len(sorted_providers) > 0 and sorted_providers[0].is_below(coverage):
                next_provider = sorted_providers.pop(0)
                if next_provider.higher_position() >= best_provider.higher_position():
                    best_provider = next_provider
            coverage = best_provider.higher_position()
            providers_to_hire.append(best_provider)

        if coverage < target_position:
            print("There aren't enough providers to cover the expected area.")
            raise SolutionNotFound()

        return providers_to_hire
