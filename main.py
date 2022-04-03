from find_providers_to_hire import FindProvidersToHireUseCase
from provider import Provider


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


if __name__ == '__main__':
    providers = create_providers()
    use_case = FindProvidersToHireUseCase()
    providers_to_hire = use_case.invoke(providers, 1000)
    print(providers_to_hire)
