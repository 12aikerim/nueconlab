from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass

class Decision(Page):
    form_model = 'player'
    form_fields = ['add','amount']

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    def vars_for_template(self):
        return{
            'decision':self.player.add,
            'amount':self.player.amount
        }
    pass


page_sequence = [Instructions, Decision, Results]
