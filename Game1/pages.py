from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Group


class Greetings(Page):
    def is_displayed (self):
        return self.round_number == 1


class Introduction(Page):
    def is_displayed (self):
        return self.round_number == 1


class ValidationSurvey(Page) :
    def is_displayed (self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['q1','q2','q3']


class Answers(Page) :
    def is_displayed(self):
        return self.round_number == 1


class game1_instructions(Page):
    def is_displayed (self):
        return self.round_number == 1


class Decision1(Page):
    form_model = 'player'
    form_fields = ['decision']

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class RandomizePlayers(WaitPage):
    def is_displayed(self):
        return self.round_number!=Constants.num_rounds
    body_text = "Matching you with the new player..."


class Results(Page):

    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()

        return dict(
            my_decision=me.decision,
            opponent_decision=opponent.decision,

        )
    timeout_seconds = 30

    pass


class FinalResults(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.create_payment_list()
        return self.player.total_payoff()


    pass


page_sequence = [Greetings,Introduction,ValidationSurvey,Answers,game1_instructions,Decision1,
                 ResultsWaitPage,Results,RandomizePlayers,FinalResults]
