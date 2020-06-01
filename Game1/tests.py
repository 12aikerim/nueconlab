from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from numpy import random


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number ==1:
            yield pages.Greetings
            yield pages.Introduction
            yield pages.ValidationSurvey, dict(q1="Yes", q2="Yes", q3="No")
            yield pages.Answers
            yield pages.game1_instructions

        if self.player.id_in_group == 1:
            yield pages.Decision1, dict(decision=random.choice(['Inspect', 'Not_inspect']))
        else:
            yield pages.Decision1, dict(decision=random.choice(['Comply', 'Not_comply']))

        yield pages.Results
        if self.round_number == Constants.num_rounds:
            yield pages.FinalResults

        pass
