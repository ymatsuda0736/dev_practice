from persons import Player, Dealer
from instruments import Pot


class PlayingTable:

    MAX_PLAYERS = 5

    def __init__(self, dealer: Dealer):

        self.dealer = dealer
        self.players = []
        self.pot = Pot()

        self.is_game_started = False

    def start_game(self, *new_players: Player):
        self.dealer.start_game()
        self._add_player(new_players)
        self.is_game_started = True

    def _add_player(self, *new_players):
        if not all([isinstance(Player, p) for p in new_players]):
            raise ValueError("プレイヤーが不正です")
        if self.MAX_PLAYERS < len(self.players) + len(new_players):
            raise ValueError("定員オーバーです. 本テーブルの定員数は{max}です.".format(max=self.MAX_PLAYERS))

    def exec_single_game(self):

        if not self.is_game_started:
            raise ValueError("まだゲームの場が整えられていません.")

        for player in self.players:
            cards = self.dealer.give_cards()
            player.receive_cards(cards)

        for player in self.players:
            action = self.dealer.ask(player)
            if action == "fold":
                player.fold()
            elif action == "raise":
                bet = player.raise_()
                self.pot.add(bet)
            elif action == "call":
                bet = player.call()
                self.pot.add(bet)

        hands = [player.open() for player in self.players if not player.is_folded]
        winner = self.dealer.judge_winner(hands)
        winner.receive_chips(self.pot.release())
