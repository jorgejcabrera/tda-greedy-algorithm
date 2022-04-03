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
    sorted_providers_available = sorted(providers_available, key=lambda x: x.lower_position())
    coverage = 0
    providers = []

    service = ProviderService()
    while coverage < final_position:
        filtered_providers = filter_data = list(
            filter(lambda provider: provider.lower_position() < coverage, sorted_providers_available))
        new_provider = service.get_best_provider_of(filtered_providers)
        providers.append(new_provider)
        coverage = new_provider.higher_position()

        # remove unnecessary providers
        sorted_providers_available = [provider for provider in sorted_providers_available if
                                      provider not in filter_data]
    return providers


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    providers = providers_to_hire(500)
    print(providers)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
