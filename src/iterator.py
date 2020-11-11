class Iterator:
    def __init__(self, container):
        self.container = container
        self.idx = 0

    def __len__(self):
        return len(self.container)

    def get(self):
        if not self._is_valid(self.idx):
            raise Exception("Can't get element because iterated container is empty")

        return self.idx, self.container[self.idx]

    def next(self, predicate=None):
        return self._move_idx(1, predicate)

    def previous(self, predicate=None):
        return self._move_idx(-1, predicate)

    def _is_valid(self, idx):
        return 0 <= idx < len(self.container) and self.container

    def _move_idx(self, dir_val, predicate):
        curr_tested_idx = self.idx + dir_val

        if predicate:
            while self._is_valid(curr_tested_idx) and not predicate(self.container[curr_tested_idx]):
                curr_tested_idx += dir_val

        if self._is_valid(curr_tested_idx):
            self.idx = curr_tested_idx
            return True
        else:
            return False


