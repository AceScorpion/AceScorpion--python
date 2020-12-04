from .player import Player
from .board import Board
from .round import Round


class Game(object):

    def __init__(self, id, players, thread):
        self.id = id
        self.player = players
        self.words_used = []
        self.round = None
        self.board = Board()
        self.start_new_round()
        self.connected_thread = thread


    def start_new_round(self):
        self.round = Round(self.get_word(), self.players[self.player_draw_ind], self.players, self)
        self.player_draw_ind += 1

        if self.player_draw_ind >= len(self.players):
            self.end_round()
            self.end_game()

    def player_guess(self, player, guess):
        return self.round.guess(player, guess)

    def player_disconnected(self, player):
        pass

    def skip(self):
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()

        else:
            raise Exception("No round started yet!")

    def round_ended(self):
        """
        If the round ends call this
        :return: None
        """
        self.start_new_round()
        self.board.clear()

    def update_board(self, x, y, color):
        """
        calls update on board.
        :param x:int
        :param y:int
        :param color:(int,int,int)
        :return: None
        """
        if not self.board:
            raise Exception("No board created")
        self.board.update(x, y, color)
        pass

    def end_round(self):
        """
        ends the game
        :return: None
        """
        # todo implement
        pass

    def get_word(self):
        # todo get a list of words from somewhere
        pass