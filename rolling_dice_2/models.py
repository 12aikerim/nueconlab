from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random

author = 'Aikerim O'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'rolling_dice_2'
    players_per_group = None
    num_rounds = 5

    instructions_template = 'rolling_dice_2/Instructions.html'

    max_allowed_guess = 6
    min_allowed_guess = 1

    win = c(100)  # payment if win
    lose = c(0)  # payment if lose
    participation_fee = c(2000)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def role(self):
        if self.participant.vars['group'] == 'treatment':
            return 'treatment'
        else:
            return 'control'

    dice_roll = models.IntegerField()
    guess = models.IntegerField(
        min=Constants.min_allowed_guess,
        max=Constants.max_allowed_guess,
        doc="Guess value of participant"
    )

    is_winner = models.BooleanField()

    def set_payoff(self):
        print("inside set_payoff")
        if self.guess == self.dice_roll:
            self.is_winner = True
        else:
            self.is_winner = False

        if self.is_winner != True:
            self.payoff = Constants.lose
        else:
            self.payoff = Constants.win

    def convert(self):
        return self.participant.payoff.to_real_world_currency(self.session)
