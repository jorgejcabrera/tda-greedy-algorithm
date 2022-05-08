from src.model.provider import Provider


class ProviderReader:

    def __init__(self, path):
        self.path = path

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
        return providers
