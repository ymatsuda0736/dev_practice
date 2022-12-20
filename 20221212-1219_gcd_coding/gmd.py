import numpy


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
        min_abs_n = min([abs(n) for n in non_zeros])
        divisor_candidates = self._get_divisors(min_abs_n)

        divisor_candidates.sort(reverse=True)
        for divisor in divisor_candidates:
            if all([n % divisor == 0 for n in non_zeros]):
                return divisor
        else:
            return 1

    @staticmethod
    def _get_divisors(n: int):
        assert 1 <= n and isinstance(n, int)
        range_max = int(numpy.sqrt(abs(n)))
        pair_list = [[i, int(n / i)] for i in range(1, range_max + 1) if n % i == 0]
        return sorted(sum(pair_list, []))
