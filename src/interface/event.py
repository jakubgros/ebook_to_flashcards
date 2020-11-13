class Event:

    @classmethod
    def from_string(cls, str_val):
        type, mapping = cls._parse(str_val)
        return cls(type, mapping)

    def __init__(self, answ, mapping):
        self.type, self.description = None, None
        if answ in mapping:
            self.type, self.description = mapping[answ]

    def is_valid(self):
        return self.type is not None

    @staticmethod
    def _parse(value):

        """
        self.type = event_type
        self.attributes = attributes
        """