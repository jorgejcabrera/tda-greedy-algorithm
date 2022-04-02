class Provider:

    def __init__(self, radius, position, provider_id):
        self.radius = radius
        self.position = position
        self.id = provider_id

    def __repr__(self):
        return f'[id:{self.id},position:{self.position},radius:{self.radius}]'

    def lower_position(self):
        return self.position - self.radius

    def higher_position(self):
        return self.position + self.radius
