class GreatestCommonDivisorCalculator:
    def __init__(self, n1: int, n2: int) -> None:

        self.n1 = n1
        self.n2 = n2
        self._validate()

    def _validate(self):
        if self.n1 % 1 != 0 or self.n2 % 1 != 0:
            raise ValueError("input must be integer")

    def calc(self):
        if self._is_both_zero():
            return 0
        elif self._is_partial_zero():
            return self._get_non_zero()
        else:
            return self._calculate_non_zero_included_case()

    def _is_both_zero(self):
        return self.n1 == 0 and self.n2 == 0

    def _is_partial_zero(self):
        return self.n1 == 0 or self.n2 == 0

    def _get_non_zero(self):
        if self.n1 == 0:
            return self.n2
        elif self.n2 == 0:
            return self.n1

    def _calculate_non_zero_included_case(self):
        assert self.n1 != 0 and self.n2 != 0

        max_possible_divisor = min(abs(self.n1), abs(self.n2))
        for divisor in reversed(range(1, max_possible_divisor + 1)):
            if self.n1 % divisor == 0 and self.n2 % divisor == 0:
                return divisor
        return 1
