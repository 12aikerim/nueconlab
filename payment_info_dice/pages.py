from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class PaymentInfo(Page):
    def vars_for_template(self):
        participant = self.participant
        return dict(redemption_code=participant.label,
                    experiment_payoff = self.participant.payoff,
                    converted_pay = self.player.convert(),
                    participation_fee = self.session.participation_fee,
                    total_game_rounds = self.player.num_rounds*2)


page_sequence = [PaymentInfo]
