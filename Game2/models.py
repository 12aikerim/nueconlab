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
import random
import numpy as np
author = 'vouch11'

doc = """
Test 3-by-3 inspector vs. firm game 
"""



class Constants(BaseConstants):
    name_in_url = 'game2'
    players_per_group = 2
    num_rounds = 35
    k = 3  # number of randomly selected rounds
    index_list = sorted(random.sample(range(5, num_rounds), k))  # exclude first 5 trial rounds
    selected_rounds = [p + 1 for p in index_list]

    print('selected rounds in game2: ', selected_rounds)  # for the experimenters to see randomly selected rounds

    instructions_template = 'Game2/Instructions.html'

    # firm's points
    firm_fully_comply = c(20)  # fully comply (payoff is the same when inspection is full, light or there is not inspection at all

    firm_PF = c(10)  # paritally comply when fully inspected
    firm_PL = c(50) # partially comply when lightly inspected
    firm_PN = c(50) # partially comply when not inspected

    firm_NF = c(10)  # not comply when fully inspected
    firm_NL = c(80)  # not comply when lightly inspected
    firm_NN = c(60)  # not comply when not inspected

    # inspector's points
    insp_FI = c(20)  # full inspection when fully comply
    insp_FL = c(50)  # light inspection when fully comply
    insp_FN = c(60)  # not inspect when when fully comply

    insp_PF = c(120)  # full inspection when paritally comply
    insp_PL = c(0)  # light inspection when paritally comply
    insp_PN = c(10)  # not inspect when paritally comply

    insp_NF = c(20)  # full inspection when not comply
    insp_NL = c(90)  # light inspection when not comply
    insp_NN = c(10)  # not inspect when not comply


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)

    pass


class Group(BaseGroup):
    firm_PF = models.CurrencyField(initial=c(100))
    firm_NL = models.CurrencyField(initial=c(200))

    def set_payoffs(self):
        self.firm_PF = c(np.random.choice([50, 0], 1, p=[0.1, 0.9]).item(0))
        print("changed value of firm_PF in group : ", self.firm_PF)
        self.firm_NL = c(np.random.choice([60, 10], 1, p=[0.5, 0.5]).item(0))
        print("modified value of firm_NL in group", self.firm_NL)
        for p in self.get_players():
            p.set_payoff()
    pass


class Player(BasePlayer):

    def role(self):
        if self.id_in_group == 1:
            return 'inspector'
        else:
            return 'firm'

    decision = models.StringField(
        choices=['Full_Inspection','Light_Inspection','No_Inspection', 'Fully_Comply','Partially_Comply','Not_Comply'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):

        payoff_matrix = dict(
            Fully_Comply=dict(
                Full_Inspection=Constants.firm_fully_comply,
                Light_Inspection=Constants.firm_fully_comply,
                No_Inspection = Constants.firm_fully_comply,
            ),
            Partially_Comply=dict(
                Full_Inspection=self.group.firm_PF,
                Light_Inspection=Constants.firm_PL,
                No_Inspection=Constants.firm_PN,
            ),
            Not_Comply=dict(
                Full_Inspection=Constants.firm_NF,
                Light_Inspection=self.group.firm_NL,
                No_Inspection=Constants.firm_NN,
            ),
            Full_Inspection = dict(
                Fully_Comply = Constants.insp_FI,
                Partially_Comply = c(-30 if self.group.firm_PF==c(50) else 20),
                Not_Comply = Constants.insp_NF,
            ),
            Light_Inspection=dict(
                Fully_Comply=Constants.insp_FL,
                Partially_Comply=Constants.insp_PL,
                Not_Comply=c(50 if self.group.firm_NL==c(10) else 0),
            ),
            No_Inspection=dict(
                Fully_Comply=Constants.insp_FN,
                Partially_Comply=Constants.insp_PN,
                Not_Comply=Constants.insp_NN,
            ),
        )

        self.payoff = payoff_matrix[self.decision][self.other_player().decision]

    def check_lump(self):
        while len(self.participant.vars['lump'])!=2:
            self.participant.vars['lump'].pop()

    def total_payoff(self):
        list_of_payments = [p.payoff for p in self.in_all_rounds()]
        print('all payments: ', list_of_payments)
        random_payoffs = [list_of_payments[p] for p in Constants.index_list]
        print('randomly selected payoffs: ', random_payoffs)
        selected_rounds = [p + 1 for p in Constants.index_list]
        print('selected rounds: ', selected_rounds)
        random_pay = dict(zip(selected_rounds, random_payoffs))
        print('dictionary: ', random_pay)

        total = sum(random_payoffs)
        self.participant.vars['lump'].append(total)
        self.check_lump()
        print("accumulated payoffs in game 2: ",self.participant.vars['lump'])
        self.participant.payoff = sum(self.participant.vars['lump'])

        return dict(
            list_of_all_payments=list_of_payments,
            round_earning=total,
            random_payments=random_pay,
            round_number=selected_rounds,
        )

    pass

