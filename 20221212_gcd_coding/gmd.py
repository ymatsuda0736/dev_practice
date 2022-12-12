class GreatestCommonDivisorCalculator:
    def __init__(self, *numbers):

        self.numbers = numbers
        self._validate()

    def _validate(self):
        for n in self.numbers:
            if not isinstance(n, int):
                raise ValueError("inputs must be integer")

    def calc(self):
        if self._is_all_zero():
            return 0
        else:
            return self._get_from_non_zeros()

    def _is_all_zero(self):
        return all([n == 0 for n in self.numbers])

    def _drop_zero(self):
        return [n for n in self.numbers if n != 0]

    def _get_from_non_zeros(self):

        non_zeros = self._drop_zero()
        max_possible_divisor = min([abs(n) for n in non_zeros])
        for divisor in reversed(range(1, max_possible_divisor + 1)):
            if all([n % divisor == 0 for n in non_zeros]):
                return divisor
        return 1
