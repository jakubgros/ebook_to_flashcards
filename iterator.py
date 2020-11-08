class Iterator:
    def __init__(self, container):
        self.container = container
        self.idx = 0

    def get(self):
        return self.idx, self.container[self.idx]

    def next(self):
        if len(self.container) <= self.idx + 1:
            False
        else:
            self.idx += 1
            return True

    def previous(self):
        if self.idx - 1 < 0:
            return False
        else:
            self.idx -= 1
            return True
