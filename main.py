from provider import Provider
from provider_service import ProviderService


def create_providers():
    return [
        Provider(radius=250, position=980, provider_id=1),
        Provider(radius=100, position=500, provider_id=2),
        Provider(radius=150, position=600, provider_id=3),
        Provider(radius=300, position=850, provider_id=4),
        Provider(radius=80, position=270, provider_id=5),
        Provider(radius=100, position=100, provider_id=6),
        Provider(radius=200, position=300, provider_id=7),
        Provider(radius=120, position=400, provider_id=8),
        Provider(radius=220, position=680, provider_id=9),
        Provider(radius=150, position=50, provider_id=10)
    ]


def providers_to_hire(final_position):
    providers_available = create_providers()
    provider_service = ProviderService()

    sorted_providers = provider_service.sort(providers_available)
    coverage = 0
    providers = []

    while coverage < final_position:
        filtered_providers = provider_service.find_all_with_coverage_below(sorted_providers, coverage)
        new_provider = provider_service.find_the_best_of(filtered_providers)
        providers.append(new_provider)
        coverage = new_provider.higher_position()
        sorted_providers = provider_service.subtract(sorted_providers, filtered_providers)
    return providers


if __name__ == '__main__':
    providers = providers_to_hire(1000)
    print(providers)
