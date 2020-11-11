class ContainerComparator:
    def __init__(self, *, elem_equality_comparator=None, sort_key=None):
        self.elem_equality_comparator = elem_equality_comparator
        self.sort_key = sort_key

    def __call__(self, lhs, rhs):
        if len(lhs) != len(rhs):
            return False

        lhs = list(lhs)
        rhs = list(rhs)

        if self.sort_key is not None:
            lhs.sort(key=self.sort_key)
            rhs.sort(key=self.sort_key)

        if self.elem_equality_comparator is None:
            comparator = lambda lhs, rhs: lhs==rhs
        else:
            comparator = self.elem_equality_comparator

        for lhs_elem, rhs_elem in zip(lhs, rhs):
            if not comparator(lhs_elem, rhs_elem):
                return False

        return True
