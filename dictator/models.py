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

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'dictator'
    players_per_group = None
    num_rounds = 1
    endowment = c(100)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                player.participant.vars['endowment'] = c(100)
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    amount = models.IntegerField(
        min=0,
        max=Constants.endowment,
        label='How much you want to send?',
        doc='Amount to be added/subtracted'
    )
    def set_payoff(self):
        self.payoff = Constants.endowment - self.amount





