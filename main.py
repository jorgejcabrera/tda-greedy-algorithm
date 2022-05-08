import sys

from src.use_case.find_providers_to_hire import FindProvidersToHireUseCase
from src.model.provider_reader import ProviderReader

if __name__ == '__main__':

    try:
        file_path = sys.argv[1]
        kilometers = sys.argv[2]
    except:
        print("Taking default values")
        file_path = "files/contratos_1.txt"
        kilometers = 200

    reader = ProviderReader(file_path)
    providers = reader.read()
    use_case = FindProvidersToHireUseCase()
    providers_to_hire = use_case.invoke(providers, int(kilometers))
    print(providers_to_hire)
