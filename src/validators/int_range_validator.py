class IntInRangeValidator:
    def __init__(self, *, valid_range):
        self.greater_or_equal_than, self.lower_than = valid_range

    def __call__(self, val):
        try:
            int_val = int(val)
            if self.greater_or_equal_than <= int_val < self.lower_than:
                return True
        except:
            pass
        return False
