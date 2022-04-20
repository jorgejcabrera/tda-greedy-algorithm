from provider import Provider
import random


def instance_one():
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


def instance_two():
    return [
        Provider(radius=100, position=500, provider_id=2),
        Provider(radius=150, position=600, provider_id=3),
        Provider(radius=300, position=850, provider_id=4),
        Provider(radius=80, position=270, provider_id=5),
        Provider(radius=100, position=100, provider_id=6),
        Provider(radius=200, position=300, provider_id=7),
        Provider(radius=120, position=400, provider_id=8),
        Provider(radius=220, position=680, provider_id=9)
    ]


def instance_three():
    return [
        Provider(radius=50, position=44, provider_id=1),
        Provider(radius=150, position=402, provider_id=2),
        Provider(radius=35, position=219, provider_id=3),
        Provider(radius=80, position=100, provider_id=4),
        Provider(radius=80, position=80, provider_id=5),
        Provider(radius=160, position=300, provider_id=6),
        Provider(radius=30, position=150, provider_id=7)
    ]


def instance_four():
    return [
        Provider(radius=150, position=50, provider_id=1),
        Provider(radius=100, position=100, provider_id=2),
        Provider(radius=150, position=300, provider_id=3),
        Provider(radius=100, position=200, provider_id=4),
        Provider(radius=275, position=450, provider_id=5),
        Provider(radius=50, position=650, provider_id=6),
        Provider(radius=150, position=850, provider_id=7)
    ]


def sample_of(amount_of_providers, kilometers):
    segments = int(kilometers / amount_of_providers)
    providers = []
    for i in range(amount_of_providers):
        position = random.randint(segments * (i + 1), segments * (i + 2))
        radius = random.randint(1, kilometers)
        providers.append(Provider(provider_id=i, position=position, radius=radius))
    return providers
