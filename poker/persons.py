from instruments import Deck, Card, Chip

HAND_CARD_NUM = 5


class Player:

    def __init__(self,
                 *chips: Chip):

        self._validate(chips)

        self.chips = chips
        self.dealer = None
        self.hand_cards = None

    def _validate(self):
        # Chipが不正じゃないかなどチェック
        pass

    def start_game(self, dealer):
        if not isinstance(Dealer, dealer):
            raise ValueError("ディーラーが不正です")
        self.dealer = dealer

    def receive_cards(self, *cards):
        if any([not isinstance(Card, c) for c in cards]):
            raise ValueError("カードが不正です")
        if len(cards) != HAND_CARD_NUM:
            raise ValueError("手札は{num}枚受け取ってください".format(num=HAND_CARD_NUM))
        self.hand_cards = cards

    def bet(self, bet):
        # 自身のチップからベットを行う
        pass

    def open(self):
        # 自身のハンドをオープンする
        return self.hand_cards


class Dealer:

    def __init__(self):
        self.deck = None
        self.players = None

    def start_game(self, *players):
        if any([not isinstance(Player, p) for p in players]):
            raise ValueError("プレイヤーが不正です")

        self.deck = Deck()
        self.players = players

    def give_cards(self):
        # デッキをシャッフルして各プレイヤーにカードを配る
        pass

    def judge_winner(self):
        # 各プレイヤーのカードから勝者を判定する
        pass
