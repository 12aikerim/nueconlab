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


author = 'Aikerim O'

doc = """
Pro-Social Preferences Donation Game
"""


class Constants(BaseConstants):
    name_in_url = 'donation'
    players_per_group = None
    num_rounds = 1
    endowment = c(1000)
    sample_donation = c(500)
    sample_earning = endowment-sample_donation

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    donation = models.IntegerField(
        min=0,
        max=Constants.endowment,
        label='How many tenge would you like to donate? ',
        doc='Amount to be donated'
    )
    def role(self):
        if self.participant.vars['group'] == 'treatment':
            return 'treatment'
        else:
            return 'control'


    def set_payoff(self):
        self.payoff = Constants.endowment - self.donation


