from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Group


class game2_instructions(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(
            Revenue =60,
            cost =40,
            on_paper =10,
            Budget =60,
            expert =40,
            intern =10,
            fine =50,
            environment =50,
        )



class Decision2(Page):
    form_model = 'player'
    form_fields = ['decision']
    def vars_for_template(self):
        return dict(
            Revenue =60,
            cost =40,
            on_paper =10,
            Budget =60,
            expert =40,
            intern =10,
            fine =50,
            environment=50,)


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()
    pass

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
            fail = c(-30),
        )
    timeout_seconds = 30
    pass


class FinalResults(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        a=self.player.total_payoff()
        return a

    pass



page_sequence = [game2_instructions, Decision2, ResultsWaitPage,Results,RandomizePlayers,FinalResults]
