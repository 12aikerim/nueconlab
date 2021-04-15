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

    charity_group = models.StringField(
        choices = [['DARA Charity Foundation','DARA Charity Foundation'],['Saby Charitable Foundation','Saby Charitable Foundation'],
                   ['Public Fund “ANA UYI”','Public Fund “ANA UYI”'],['Charitable Foundation “Niyet”','Charitable Foundation “Niyet”'],
                   ['Aruzhan Sain Public Foundation “Voluntary Society Mercy”','Aruzhan Sain Public Foundation “Voluntary Society Mercy”']],
        widget=widgets.RadioSelect,
        label = 'You may keep all of this money or you may make a donation to one of the following five organizations in Kazakhstan'
    )
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


