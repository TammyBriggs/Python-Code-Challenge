class Magazine:
    instances = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.instances.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    @classmethod
    def all(cls):
        return cls.instances
    pass