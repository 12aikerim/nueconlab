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

from typing import List, Any

author = 'vouch11'

doc = """
Test 2-by-2 inspector vs. firm game 
"""

class Constants(BaseConstants):
    name_in_url = 'game1'
    players_per_group = 2
    num_rounds = 35
    k = 3 #number of randomly selected rounds
    index_list = sorted(random.sample(range(5,num_rounds), k))
    print('indexes game1: ', index_list)

    # constants with links to pages
    instructions_template = 'Game1/Instructions.html'
    intro_screen = 'Game1/Screen1.html'
    screen_2 = 'Game1/Screen2.html'
    screen_3 = 'Game1/Screen3.html'


    #Player A points in Game one
    ul = c(20) # UP when LEFT
    dl = c(10) # DOWN when LEFT
    ur = c(20) # UP when RIGHT
    dr = c(60) # DOWN when RIGHT

    # Player B points in Game one
    lu = c(20) #LEFT when UP
    ld = c(20) #LEFT when DOWN
    ru = c(60) #RIGHT when UP
    rd = c(10) #RIGHT when DOWN

    # firm's points
    firm_IC = ul  # comply when inspected
    firm_IN = dl  # not comply when inspected
    firm_NC = ur  # comply when not inspected
    firm_NN = dr  # not comply when not inspected

    # inspector's points
    insp_IC = lu  # inspect when comply
    insp_IN = ld  # inspect when not comply
    insp_NC = ru  # not inspect when comply
    insp_NN = rd  # not inspect when not comply


class Subsession(BaseSubsession):

    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)
    pass


class Group(BaseGroup):
    def set_payoffs(self):
        for p in self.get_players():
            p.set_payoff()
    pass

class Player(BasePlayer):

    def role(self):
        if self.id_in_group == 1:
            return 'inspector'
        else:
            return 'firm'

    q1 = models.StringField(
        choices=['Yes', 'No'],
        label='Will you play against the computer in this experiment?',
        widget=widgets.RadioSelect,
    )
    q2 = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No']],
        label='Will your decisions affect the final payoff you will collect?',
        widget=widgets.RadioSelect,
    )
    q3 = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No']],
        label='Are payoffs from each round in every game added to your total earnings?',
        widget=widgets.RadioSelect,
    )

    decision = models.StringField(
        choices=['Inspect', 'Comply','Not_inspect', 'Not_comply'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff_matrix = dict(
            Comply=dict(
                Inspect=Constants.firm_IC,
                Not_inspect=Constants.firm_NC,
            ),
            Not_comply=dict(
                Inspect=Constants.firm_IN, Not_inspect=Constants.firm_NN
            ),
            Inspect = dict(
                Comply = Constants.insp_IC,
                Not_comply = Constants.insp_IN,
            ),
            Not_inspect = dict(
                Comply = Constants.insp_NC,
                Not_comply = Constants.insp_NN,
            ),

        )
        self.payoff = payoff_matrix[self.decision][self.other_player().decision]

    def create_payment_list(self):
        self.participant.vars['lump'] = []
        return self.participant.vars['lump']

    pass

    def check_lump(self):
        while len(self.participant.vars['lump'])!=1:
            self.participant.vars['lump'].pop()

    pass

    def total_payoff(self):

        list_of_payments = [p.payoff for p in self.in_all_rounds()]
        print('all payments: ', list_of_payments)

        random_payoffs =[list_of_payments[p] for p in Constants.index_list]

        print('randomly selected payoffs: ', random_payoffs)
        selected_rounds = [p + 1 for p in Constants.index_list]

        print('selected rounds: ',selected_rounds)
        random_pay =dict(zip(selected_rounds, random_payoffs))
        print('dictionary: ', random_pay)

        total=sum(random_payoffs)
        self.participant.payoff = total
        self.participant.vars['lump']=[total]
        self.check_lump()
        print("accumulated payoff in game 1: ", self.participant.vars['lump'])
        return dict(
            list_of_all_payments=list_of_payments,
            round_earning=total,
            random_payments=random_pay,
            round_number=selected_rounds,
        )


    pass


