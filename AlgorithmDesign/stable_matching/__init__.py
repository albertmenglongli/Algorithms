from funcy import identity


class Person(object):
    def __init__(self, name, age, height, preferences_key=identity):
        self._name = name
        self._height = height
        self._age = age
        self.preferences_key = preferences_key
        self._proposal = None
        self._proposed_list = []

    @property
    def name(self):
        return self._name

    @property
    def height(self):
        return self._height

    @property
    def age(self):
        return self._age

    @property
    def proposal(self):
        return self._proposal

    @proposal.setter
    def proposal(self, value):
        self._proposal = value

    def append_to_proposed(self, value):
        if value not in self._proposed_list:
            self._proposed_list.append(value)

    def has_proposed(self, value):
        return True if value in self._proposed_list else False

    def reset(self):
        self._proposal = None
        self._proposed_list = []

    def get_ranks(self, lst):
        return sorted(lst, key=self.preferences_key)

    def __str__(self):
        return '(Name: "{self.name}", Age: "{self.age}", Height: "{self.height}")'.format(self=self)

    def __repr__(self):
        return str(self)


class Man(Person):
    def __init__(self, name, age, height, preferences_key=identity):
        super(Man, self).__init__(name, age, height, preferences_key)

    @property
    def proposal(self):
        return self._proposal

    @proposal.setter
    def proposal(self, value):
        assert (isinstance(value, Woman) or value is None)
        self._proposal = value


class Woman(Person):
    def __init__(self, name, age, height, preferences_key=identity):
        super(Woman, self).__init__(name, age, height, preferences_key)

        @property
        def proposal(self):
            return self._proposal

        @proposal.setter
        def proposal(self, value):
            assert (isinstance(value, Man) or value is None)
            self._proposal = value
