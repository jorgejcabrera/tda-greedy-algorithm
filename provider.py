class Provider:

    def __init__(self, radius, position, provider_id):
        self.radius = radius
        self.position = position
        self.id = provider_id

    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self.id == other.id and
                self.radius == other.radius and
                self.position == other.position
        )

    def __repr__(self):
        return f'[id:{self.id},position:{self.position},radius:{self.radius}]'

    def lower_position(self):
        return self.position - self.radius

    def higher_position(self):
        return self.position + self.radius

    def available_in(self, position):
        return self.lower_position() <= position <= self.higher_position()

    def is_below(self, position):
        return self.lower_position() <= position
