from src.model.provider import Provider
from src.model.provider_service import ProviderService


class ProviderReader:

    def __init__(self, path):
        self.path = path
        self.service = ProviderService()

    # #
    # POST: A list of sorted providers must be returned
    # #
    def read(self):
        file = open(self.path)
        providers = []
        for line in file:
            data = line.replace('\n', '').split(sep=",")
            providers.append(Provider(
                radius=int(data[2]),
                position=int(data[1]),
                provider_id=int(data[0]))
            )
        file.close()
        providers = self.service.sort(providers)
        return providers