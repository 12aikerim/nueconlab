from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Introduction(Page):
    def is_displayed (self):
        return self.round_number == 1


class Instructions(Page):
    def is_displayed (self):
        return self.round_number == 1
    pass


class ControlDecision(Page):
    form_model = 'player'
    form_fields = ['guess']


class TreatmentDecision(Page):
    form_model = 'player'
    form_fields = ['guess']
    def vars_for_template(self):
        return dict(
            img_dice_path='rolling_dice/{}.png'.format(self.player.dice_roll)
        )
    pass


class Decision(Page):
    form_model = 'player'
    form_fields = ['guess']

    def vars_for_template(self):
        random_dice = random.randint(Constants.min_allowed_guess, Constants.max_allowed_guess)
        self.player.dice_roll = random_dice
        print("self.player.dice_roll = {}".format(random_dice))
        return dict(dice_roll=random_dice,
                    img_dice_path='rolling_dice/{}.png'.format(self.player.dice_roll))

    def before_next_page(self):
        self.player.set_payoff()

    pass

class MyWaitPage(WaitPage):
    pass

class Results(Page):
    #dynamic images of results

    def vars_for_template(self):
        return dict(
            img_dice_path='rolling_dice/{}.png'.format(self.player.dice_roll)
        )
    pass


class FinishPayment(Page):
    def is_displayed(self):
        return self.round_number==Constants.num_rounds

    def vars_for_template(self):
        participant = self.participant
        return dict(redemption_code=participant.label,
                    experiment_payoff = self.participant.payoff,
                    participation_fee = self.session.participation_fee,
                    total_game_rounds = 40)


page_sequence = [Introduction, Instructions, Decision, Results, FinishPayment]
