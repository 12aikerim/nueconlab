from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass

class Decision(Page):
    form_model = 'player'
    form_fields = ['amount']
    def before_next_page(self):
        self.player.set_payoff()


class Results(Page):
    def vars_for_template(self):
        return{
            'amount':self.player.amount}
    pass


page_sequence = [Instructions, Decision]
