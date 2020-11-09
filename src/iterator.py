class Iterator:
    def __init__(self, container):
        self.container = container
        self.idx = 0

    def _is_valid(self, idx):
        return 0 <= idx < len(self.container)

    def get(self):
        return self.idx, self.container[self.idx]

    def _move_idx(self, dir_val, predicate):
        if predicate:
            curr_tested_idx = self.idx + dir_val
            while self._is_valid(curr_tested_idx) and not predicate(self.container[curr_tested_idx]):
                curr_tested_idx += dir_val

            if self._is_valid(curr_tested_idx):
                self.idx = curr_tested_idx
                return True
            else:
                return False
        else:
            if self._is_valid(self.idx + dir_val):
                self.idx += dir_val
                return True
            else:
                return False

    def previous(self, predicate=None):
        return self._move_idx(-1, predicate)

    def next(self, predicate=None):
        return self._move_idx(1, predicate)


