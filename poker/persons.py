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

    def start_game(self):
        self.deck = Deck()

    def give_cards(self):
        # デッキをシャッフルして各プレイヤーにカードを配る
        pass

    def judge_winner(self):
        # 各プレイヤーのカードから勝者を判定する
        pass


class PlayingTable:

    MAX_PLAYERS = 5

    def __init__(self, dealer: Dealer):

        self.dealer = dealer
        self.players = []

    def add_player(self, *new_players: Player):

        if not all([isinstance(Player, p) for p in new_players]):
            raise ValueError("プレイヤーが不正です")
        if self.MAX_PLAYERS < len(self.players) + len(new_players):
            raise ValueError("定員オーバーです. 本テーブルの定員数は{max}です.".format(max=self.MAX_PLAYERS))
