from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class DonationPage(Page):
    form_model = 'player'
    form_fields = ['charity_group','donation']
    def before_next_page(self):
        self.player.set_payoff()

class Results(Page):
    def vars_for_template(self):
        return dict(amount_donated = self.player.donation,
                    amount_earned = self.player.payoff)
page_sequence = [DonationPage,Results]
