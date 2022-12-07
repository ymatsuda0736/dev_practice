class GreatestCommonDivisorCalculator:
    def __init__(self, number_1: int, number_2: int) -> None:
        self.number_1 = number_1
        self.number_2 = number_2

    def get_gmd(self):
        zero_included_case_result = self._calculate_zero_included_case()
        if zero_included_case_result is not None:
            return zero_included_case_result

        non_zero_case_result = self._calculate_non_zero_included_case()
        return non_zero_case_result

    def _calculate_zero_included_case(self):
        is_both_zero = self.number_1 == 0 and self.number_2 == 0
        if is_both_zero:
            return 0

        is_partial_zero = not is_both_zero and (self.number_1 == 0 or self.number_2 == 1)
        if is_partial_zero:
            if self.number_1 == 0:
                return self.number_2
            elif self.number_2 == 0:
                return self.number_1

    def _calculate_non_zero_included_case(self):
        assert self.number_1 != 0 and self.number_2 != 0

        max_possible_divisor = max(abs(self.number_1), abs(self.number_2))
        for divisor in reversed(range(1, max_possible_divisor + 1)):
            if self.number_1 % divisor == 0 and self.number_2 % divisor == 0:
                return divisor
        return 1
