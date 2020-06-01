from otree.api import Currency as c, currency_range

from . import pages
from ._builtin import Bot
from .models import Constants

from numpy import random

class PlayerBot(Bot):

    def play_round(self):

        yield (pages.Demographics, {'age': 24, 'gender': 'Male','citizen':random.choice([False,True]),'residence':1,'degree':True,'participation':1,'experience_econ':1,
                'experience_game':1,'risk_tolerance':1,'inform_source':1,'problem':1 })

        yield (
            pages.QuestionaireOnExperiment,
            {'Q1':1,'Q2':2,'Q3':3,'Q4':4,'Q5':5,'Q6':5,'Q7':4,'Q8':3,'Q9':2,'Q10':1},
        )

