import time as t
from _thread import *
from.game import Game
from.chat import Chat


class Round(object):
    def __init__(self, word, player_drawing, players, game):
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0
        self.player_scores = {player: 0 for player in players}
        self.time = 75
        self.chat  = Chat(self)
        self.start = t.time()
        start_new_thread(self.time_thread,  ())

    def skip(self):
        """
        Returns true if round skipped threshold met
        :return: bool
        """
        self.skips += 1
        if self.skips > len(self.players) - 2:
            return True

        return False

    def get_scores(self):
        """
        :returns all the player scores
        """
        return self.player_scores

    def get_score(self, player):
        """
        gets a specific
        :param player: Player
        :return: int
        """
        if player in self.player_scores:
         return self.player_scores[player]
        else:
            raise Exception("PLayer not in score list")


    def time_thread(self):
        while self.time > 0:
            t.sleep(1)
            self.time -= 1
        self.end_round("Time is up")

    def guess(self, player, wrd):
        """
        :returns bool if got guess correct
        :param player: player
        :param wrd: str
        :return: bool
        """
        correct = wrd == self.word
        if correct:
            self.player_guessed.append(player)
            # TODO IMPLEMENT SCORING SYSTEM HERE

    def player_left(self, player):
        if player in self.player_scores:
            del self.player_scores[player]

        if player in self.player_guessed:
            self.player_guessed.remove(player)
        if player == self.player_drawing:
            self.end_round("Drawing player leaves!")

    def end_round(self, msg):
        # TODO implement end round functionality
        pass