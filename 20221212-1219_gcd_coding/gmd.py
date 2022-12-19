class GCDCalculator:
    def __init__(self, *nums):

        self.nums = nums
        self._validate()

    def _validate(self):
        contains_non_int = any([not isinstance(n, int) for n in self.nums])
        if contains_non_int:
            raise ValueError("inputs must be integer")

    def calc(self):
        if self._is_all_zero():
            return 0
        else:
            return self._get_non_zeros_gcd()

    def _is_all_zero(self):
        return all([n == 0 for n in self.nums])

    def _get_non_zeros_gcd(self):
        non_zeros = [n for n in self.nums if n != 0]
        max_possible_divisor = min([abs(n) for n in non_zeros])
        for divisor in reversed(range(1, max_possible_divisor + 1)):
            if all([n % divisor == 0 for n in non_zeros]):
                return divisor
        return 1
