from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from numpy import random

class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield pages.game2_instructions

        if self.player.id_in_group == 1:
            yield pages.Decision2, dict(decision=random.choice(['Full_Inspection', 'Light_Inspection', 'No_Inspection']))
        else:
            yield pages.Decision2, dict(decision=random.choice(['Fully_Comply', 'Partially_Comply', 'Not_Comply']))
        yield pages.Results


        if self.round_number == Constants.num_rounds:
            yield pages.FinalResults

        pass
