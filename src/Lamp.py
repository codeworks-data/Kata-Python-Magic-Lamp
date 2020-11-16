class Object:
    def __init__(self, name, price, weight, count):
        self.name = name
        self.price = price
        self.weight = weight
        self.count = count

    def __eq__(self, other):
        return self.name == other.name and \
               self.price == other.price and \
               self.weight == other.weight and \
               self.count == other.count


class Powder:
    def __init__(self, name, quantity, price_per_gram):
        self.name = name
        self.quantity = quantity
        self.price_per_gram = price_per_gram

    def __eq__(self, other):
        return self.name == other.name and \
               self.quantity == other.quantity and \
               self.price_per_gram == other.price_per_gram


class Lamp:
    def __init__(self, max_capacity):
        self.objects = []
        self.powders = []
        self.max_capacity = max_capacity

    def fill(self, objects, powders):
        # fill objects and powders
        # The count of objects can be modified
        # The quantities of powders can be modified
        self.objects = [...]
        self.powders = [...]
