class IntInRangeValidator:
    def __init__(self, greater_than, lower_than):
        self.greater_than = greater_than
        self.lower_than = lower_than

    def __call__(self, val):
        try:
            int_val = int(val)
            if self.greater_than < int_val < self.lower_than:
                return True
        except:
            pass
        return False
