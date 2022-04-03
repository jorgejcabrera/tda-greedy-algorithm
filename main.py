from find_providers_to_hire import FindProvidersToHireUseCase
from provider_reader import ProviderReader

if __name__ == '__main__':
    reader = ProviderReader("contratos.txt")
    providers = reader.read()
    use_case = FindProvidersToHireUseCase()
    providers_to_hire = use_case.invoke(providers, 500)
    print(providers_to_hire)
