import itertools
import random


class Card:
    '''トランプのカードを表すクラス
    ジョーカーは未対応'''

    SUITS_DISPLAY_DICT = {
        "heart": "❤️",
        "clover": "♣︎",
        "spade": "♠︎",
        "diamond": "♦︎"
    }

    NUMS_DISPLAY_DICT = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K"
    }
    MIN_NUM = min(NUMS_DISPLAY_DICT.keys())
    MAX_NUM = max(NUMS_DISPLAY_DICT.keys())
    assert len(NUMS_DISPLAY_DICT) == MAX_NUM, "数値の設定を確認ください"

    def __init__(self,
                 suit: str,
                 number: int):

        self._validate(suit, number)
        self.suit = suit
        self.number = number

    def _validate(self, suit, number):
        suit_options = self.SUITS_DISPLAY_DICT.keys()
        if not any(suit == k for k in suit_options):
            suits = ",".join(suit_options)
            raise ValueError("絵柄は{suits}から選択してください".format(suits=suits))

        if not isinstance(number, int):
            raise ValueError("数値はinteger型を入力してください")

        if number < self.MIN_NUM or self.MAX_NUM < number:
            raise ValueError("数値は{min}から{max}の間の値を入力してください".format(min=self.MIN_NUM, max=self.MAX_NUM))

    def __str__(self):
        suit_display = self.SUITS_DISPLAY_DICT[self.suit]
        number_display = self.NUMS_DISPLAY_DICT[self.number]
        return suit_display + number_display


class Deck:
    '''トランプのカードデックを表すクラス
    ジョーカーは含まない'''

    def __init__(self):
        self.cards = self._create_initial_deck()

    def _create_initial_deck(self):

        suits = Card.SUITS_DISPLAY_DICT.keys()
        min_num = Card.MIN_NUM
        max_num = Card.MAX_NUM

        deck = [Card(suit, num) for suit, num in itertools.product(suits, range(min_num, max_num + 1))]
        return deck

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            raise ValueError("カードがもうありません!!")
        return self.cards.pop(0)


class Chip:

    UNITS = [1, 5, 10, 20, 100]

    def __init__(self, unit: int):
        self._validate(unit)
        self.unit = unit

    def _validate(self, unit):

        if not isinstance(unit, int):
            raise ValueError("チップの単位はIntegerを入力してください")

        if not any([unit == i for i in self.UNITS]):
            units = ",".join([str(i) for i in self.UNITS])
            raise ValueError("チップの単位は{units}から選択してください".format(units=units))


class Pot:

    def __init__(self):
        self.chip_total = 0

    def add(self, *chips: Chip):
        pass

    def release(self):
        release_chips = self.chip_total
        self.chip_total = 0
        return release_chips
