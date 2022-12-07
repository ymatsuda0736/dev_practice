from gmd import GreatestCommonDivisorCalculator
from datetime import datetime as dt


def display_result(func):
    def exec_and_display():
        try:
            func()
            print(f"☀️ 成功: 「{func.__name__}」")
        except Exception as e:
            print(f"☔️ 失敗: 「{func.__name__}」: {e}")

    return exec_and_display


class GreatestCommonDivisorTester:

    def __init__(self):
        pass

    def test(self):
        self.test_1と1の最大公約数は1()
        self.test_3と7の最大公約数は1()
        self.test_マイナス3と7の最大公約数は1()
        self.test_0と7の最大公約数は7()
        self.test_0と0の最大公約数は0()
        self.test_2と10の最大公約数は2()
        self.test_マイナス2と10の最大公約数は2()
        self.test_速度_10000000と10の最大公約数を0_01秒以内()

    @staticmethod
    @display_result
    def test_1と1の最大公約数は1():
        number_1 = 1
        number_2 = 1
        expected = 1
        assert GreatestCommonDivisorCalculator(number_1, number_2).get_gmd() == expected

    @staticmethod
    @display_result
    def test_3と7の最大公約数は1():
        number_1 = 3
        number_2 = 7
        expected = 1
        assert GreatestCommonDivisorCalculator(number_1, number_2).get_gmd() == expected

    @staticmethod
    @display_result
    def test_マイナス3と7の最大公約数は1():
        number_1 = -3
        number_2 = 7
        expected = 1
        assert GreatestCommonDivisorCalculator(number_1, number_2).get_gmd() == expected

    @staticmethod
    @display_result
    def test_0と7の最大公約数は7():
        number_1 = 0
        number_2 = 7
        expected = 7
        assert GreatestCommonDivisorCalculator(number_1, number_2).get_gmd() == expected

    @staticmethod
    @display_result
    def test_0と0の最大公約数は0():
        number_1 = 0
        number_2 = 0
        expected = 0
        assert GreatestCommonDivisorCalculator(number_1, number_2).get_gmd() == expected

    @staticmethod
    @display_result
    def test_2と10の最大公約数は2():
        number_1 = 2
        number_2 = 10
        expected = 2
        assert GreatestCommonDivisorCalculator(number_1, number_2).get_gmd() == expected

    @staticmethod
    @display_result
    def test_マイナス2と10の最大公約数は2():
        number_1 = -2
        number_2 = 10
        expected = 2
        assert GreatestCommonDivisorCalculator(number_1, number_2).get_gmd() == expected

    @staticmethod
    @display_result
    def test_速度_10000000と10の最大公約数を0_01秒以内():
        number_1 = 10000000
        number_2 = 10
        expected = 10
        required_speed_seconds = 0.01

        start = dt.now()
        result = GreatestCommonDivisorCalculator(number_1, number_2).get_gmd() == expected
        assert (dt.now() - start).total_seconds() <= required_speed_seconds
        assert result == expected
