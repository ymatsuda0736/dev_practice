from gmd import GCDCalculator
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

    def test(self):
        self.test_8の最大公約数は8()
        self.test_1と1の最大公約数は1()
        self.test_3と7の最大公約数は1()
        self.test_マイナス3と7の最大公約数は1()
        self.test_0と7の最大公約数は7()
        self.test_7と0の最大公約数は7()
        self.test_0と0の最大公約数は0()
        self.test_2と10の最大公約数は2()
        self.test_マイナス2と10の最大公約数は2()
        self.test_2と4と18の最大公約数は2()
        self.test_3と4と18の最大公約数は1()
        self.test_0と0と18の最大公約数は18()
        self.test_0と0と0の最大公約数は0()
        self.test_速度_10000000と10の最大公約数を0_01秒以内()
        self.test_速度_10000000と20000000の最大公約数を0_01秒以内()
        self.test_速度_293999と294013の2つの大きい素数の最大公約数を0_01秒以内()
        self.test_エラー_小数は受け付けない()

    @staticmethod
    @display_result
    def test_8の最大公約数は8():
        assert GCDCalculator(8).calc() == 8

    @staticmethod
    @display_result
    def test_1と1の最大公約数は1():
        number_1 = 1
        number_2 = 1
        expected = 1
        assert GCDCalculator(number_1, number_2).calc() == expected

    @staticmethod
    @display_result
    def test_3と7の最大公約数は1():
        number_1 = 3
        number_2 = 7
        expected = 1
        assert GCDCalculator(number_1, number_2).calc() == expected

    @staticmethod
    @display_result
    def test_マイナス3と7の最大公約数は1():
        number_1 = -3
        number_2 = 7
        expected = 1
        assert GCDCalculator(number_1, number_2).calc() == expected

    @staticmethod
    @display_result
    def test_0と7の最大公約数は7():
        number_1 = 0
        number_2 = 7
        expected = 7
        assert GCDCalculator(number_1, number_2).calc() == expected

    @staticmethod
    @display_result
    def test_7と0の最大公約数は7():
        number_1 = 7
        number_2 = 0
        expected = 7
        assert GCDCalculator(number_1, number_2).calc() == expected

    @staticmethod
    @display_result
    def test_0と0の最大公約数は0():
        number_1 = 0
        number_2 = 0
        expected = 0
        assert GCDCalculator(number_1, number_2).calc() == expected

    @staticmethod
    @display_result
    def test_2と10の最大公約数は2():
        number_1 = 2
        number_2 = 10
        expected = 2
        assert GCDCalculator(number_1, number_2).calc() == expected

    @staticmethod
    @display_result
    def test_マイナス2と10の最大公約数は2():
        number_1 = -2
        number_2 = 10
        expected = 2
        assert GCDCalculator(number_1, number_2).calc() == expected

    @staticmethod
    @display_result
    def test_2と4と18の最大公約数は2():
        assert GCDCalculator(2, 4, 18).calc() == 2

    @staticmethod
    @display_result
    def test_3と4と18の最大公約数は1():
        assert GCDCalculator(1, 4, 18).calc() == 1

    @staticmethod
    @display_result
    def test_0と0と18の最大公約数は18():
        assert GCDCalculator(0, 0, 18).calc() == 18

    @staticmethod
    @display_result
    def test_0と0と0の最大公約数は0():
        assert GCDCalculator(0, 0, 0).calc() == 0

    @staticmethod
    @display_result
    def test_速度_10000000と10の最大公約数を0_01秒以内():
        number_1 = 10000000
        number_2 = 10
        expected = 10
        required_speed_seconds = 0.01

        start = dt.now()
        result = GCDCalculator(number_1, number_2).calc()
        elapsed_seconds = (dt.now() - start).total_seconds()
        assert elapsed_seconds <= required_speed_seconds, f"elapsed: 「{str(elapsed_seconds)} seconds」"
        assert result == expected

    @staticmethod
    @display_result
    def test_速度_10000000と20000000の最大公約数を0_01秒以内():
        number_1 = 10000000
        number_2 = 20000000
        expected = 10000000
        required_speed_seconds = 0.01

        start = dt.now()
        result = GCDCalculator(number_1, number_2).calc()
        elapsed_seconds = (dt.now() - start).total_seconds()
        assert elapsed_seconds <= required_speed_seconds, f"elapsed: 「{str(elapsed_seconds)} seconds」"
        assert result == expected

    @staticmethod
    @display_result
    def test_速度_293999と294013の2つの大きい素数の最大公約数を0_01秒以内():
        number_1 = 293999
        number_2 = 294013
        expected = 1
        required_speed_seconds = 0.01

        start = dt.now()
        result = GCDCalculator(number_1, number_2).calc()
        elapsed_seconds = (dt.now() - start).total_seconds()
        assert elapsed_seconds <= required_speed_seconds, f"elapsed: 「{str(elapsed_seconds)} seconds」"
        assert result == expected

    @staticmethod
    @display_result
    def test_エラー_小数は受け付けない():
        number_1 = 0.1
        number_2 = 0.1
        expected = None
        result = GCDCalculator(number_1, number_2).calc()
