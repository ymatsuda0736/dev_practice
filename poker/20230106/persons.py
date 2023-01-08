from instruments import Deck, Card, Chip


class Player:

    HAND_CARD_NUM = 5

    def __init__(self,
                 *chips: Chip):

        self._validate(chips)

        self.chips = chips
        self.dealer = None
        self.hand_cards = None
        self.is_folded = False

    def _validate(self):
        # Chipが不正じゃないかなどチェック
        pass

    def receive_cards(self, *cards):
        if any([not isinstance(Card, c) for c in cards]):
            raise ValueError("カードが不正です")
        if len(cards) != self.HAND_CARD_NUM:
            raise ValueError("手札は{num}枚受け取ってください".format(num=self.HAND_CARD_NUM))
        self.hand_cards = cards

    def pay_chip(self):
        pass

    def bet(self, bet):
        # 自身のチップからベットを行う
        pass

    def open(self):
        # 自身のハンドをオープンする
        return self.hand_cards

    def raise_(self):
        pass

    def call(self, num):
        pass

    def fold(self):
        self.is_folded = True

    def receive_chip(self):
        pass


class Dealer:

    def __init__(self):
        self.deck = None

    def start_game(self):
        self.deck = Deck()

    def give_cards(self):
        # デッキをシャッフルして各プレイヤーにカードを配る
        pass

    def ask(self):
        # 各プレイヤーにcall, raise, foldを聞く
        pass

    def judge_winner(self):
        # 各プレイヤーのカードから勝者を判定する
        pass
