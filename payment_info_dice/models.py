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


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class Constants(BaseConstants):
    name_in_url = 'payment_info_dice'
    players_per_group = None
    num_rounds = 1
    game_rounds = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def convert(self):
        return self.participant.payoff.to_real_world_currency(self.session)
