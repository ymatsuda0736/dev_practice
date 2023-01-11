class Card:
    SUIT_LABEL_DICT = {"spade": "♠", "heart": "♥", "diamond": "♦", "club": "♣"}
    NUM_LABEL_DICT = {
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
        13: "K",
    }
    SUITS = SUIT_LABEL_DICT.keys()
    NUMS = NUM_LABEL_DICT.keys()

    def __init__(self, suit, num) -> None:
        self._suit = suit
        self._num = num

    def __str__(self) -> str:
        suit_label = self.SUIT_LABEL_DICT[self._suit]
        num_label = self.NUM_LABEL_DICT[self._num]
        return f"{suit_label}{num_label}"


class Hand:
    """
    ポーカーの手札を表す. 5枚の手札, 交換はなしの前提.
    ロイヤルストレートフラッシュは個別の役とせずストレートフラッシュに包含する.
    カードのスーツによるランク付けは行わない.
    """

    CARD_COUNT = 5

    def __init__(self, *cards: Card) -> None:
        self._validate(cards)
        self._cards = cards

    def _validate(self, cards):
        if len(cards) != self.CARD_COUNT:
            raise ValueError(f"cardsの数は{self.CARD_COUNT}枚にしてください")

    def __str__(self) -> str:
        return str([str(card) for card in self._cards])

    @property
    def cards(self):
        return self._cards

    def eval(self):
        return HandRule.eval(self.cards)

    def __eq__(self, other):
        self._validate_comparison(other)
        d1 = self.eval()
        d2 = other.eval()
        return HandRule.POKER_HANDS_ASCENDING.index(d1["hand"]) == HandRule.POKER_HANDS_ASCENDING.index(d2["hand"])

    def __ne__(self, other):
        self._validate_comparison(other)
        d1 = self.eval()
        d2 = other.eval()
        return HandRule.POKER_HANDS_ASCENDING.index(d1["hand"]) != HandRule.POKER_HANDS_ASCENDING.index(d2["hand"])

    def __lt__(self, other):
        self._validate_comparison(other)
        d1 = self.eval()
        d2 = other.eval()
        return HandRule.POKER_HANDS_ASCENDING.index(d1["hand"]) < HandRule.POKER_HANDS_ASCENDING.index(d2["hand"])

    def __le__(self, other):
        self._validate_comparison(other)
        d1 = self.eval()
        d2 = other.eval()
        return HandRule.POKER_HANDS_ASCENDING.index(d1["hand"]) <= HandRule.POKER_HANDS_ASCENDING.index(d2["hand"])

    def __gt__(self, other):
        self._validate_comparison(other)
        d1 = self.eval()
        d2 = other.eval()
        return HandRule.POKER_HANDS_ASCENDING.index(d1["hand"]) > HandRule.POKER_HANDS_ASCENDING.index(d2["hand"])

    def __ge__(self, other):
        self._validate_comparison(other)
        d1 = self.eval()
        d2 = other.eval()
        return HandRule.POKER_HANDS_ASCENDING.index(d1["hand"]) >= HandRule.POKER_HANDS_ASCENDING.index(d2["hand"])

    def _validate_comparison(self, other):
        if not isinstance(other, self.__class__):
            self_class = self.__class__.__name__
            other_class = other.__class__.__name__
            raise NotImplementedError(f'comparison between {self_class} and {other_class} is not supported')


class Evaluator:

    RESULT_BASE_DICT = {
        "has_hand": False,
        "hand_nums": (None,),
        "remaining_nums": (None,)
    }

    @classmethod
    def straight_flush(self, cards):
        eval_straight_dict = self.straight(cards)
        eval_flush_dict = self.flush(cards)
        is_straight_flush = eval_straight_dict["has_hand"] and eval_flush_dict["has_hand"]

        eval_dict = self.RESULT_BASE_DICT.copy()
        eval_dict["has_hand"] = is_straight_flush
        return eval_dict

    @classmethod
    def straight(self, cards):
        eval_dict = self.RESULT_BASE_DICT.copy()
        return eval_dict

    @classmethod
    def flush(self, cards):
        eval_dict = self.RESULT_BASE_DICT.copy()
        return eval_dict

    @classmethod
    def four_card(self, cards):
        eval_dict = self.RESULT_BASE_DICT.copy()
        return eval_dict

    @classmethod
    def full_house(self, cards):
        eval_dict = self.RESULT_BASE_DICT.copy()
        return eval_dict

    @classmethod
    def three_card(self, cards):
        eval_dict = self.RESULT_BASE_DICT.copy()
        return eval_dict

    @classmethod
    def two_pair(self, cards):
        eval_dict = self.RESULT_BASE_DICT.copy()
        return eval_dict

    @classmethod
    def one_pair(self, cards):
        eval_dict = self.RESULT_BASE_DICT.copy()
        return eval_dict

    @classmethod
    def no_hand(self, cards):
        eval_dict = self.RESULT_BASE_DICT.copy()
        eval_dict["has_hand"] = True
        return eval_dict


class HandRule:

    POKER_HANDS_DESCENDING = [
        "straight_flush",
        "four_card",
        "full_house",
        "flush",
        "straight",
        "three_card",
        "two_pair",
        "one_pair",
        "no_hand",
    ]
    POKER_HANDS_ASCENDING = list(reversed(POKER_HANDS_DESCENDING))

    HAND_EVALUATOR_DICT = {
        "straight_flush": Evaluator.straight_flush,
        "four_card": Evaluator.four_card,
        "full_house": Evaluator.full_house,
        "flush": Evaluator.flush,
        "straight": Evaluator.straight,
        "three_card": Evaluator.three_card,
        "two_pair": Evaluator.two_pair,
        "one_pair": Evaluator.one_pair,
        "no_hand": Evaluator.no_hand
    }
    assert(POKER_HANDS_DESCENDING) != sorted(list(HAND_EVALUATOR_DICT.keys()))

    @classmethod
    def eval(self, cards):

        for hand in self.POKER_HANDS_DESCENDING:
            eval_func = HandRule.HAND_EVALUATOR_DICT[hand]
            eval_dict = eval_func(cards)
            if eval_dict["has_hand"]:
                return {"hand": hand,
                        "hand_nums": eval_dict["hand_nums"],
                        "remaining_nums": eval_dict["remaining_nums"]}
        else:
            raise ValueError("役が見つかりません.")
