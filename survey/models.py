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


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(label='1) What is your age?', min=18, max=99)

    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='2) What is your gender?',
        widget=widgets.RadioSelect,
    )

    citizen = models.BooleanField(
        choices=[
            [False,'No'],
            [True,'Yes'],
        ],
        label='3) Are you a citizen of Singapore?',
        widget=widgets.RadioSelect,
    )
    residence = models.IntegerField(
        choices=[
            [1, 'Mostly in Singapore'],
            [2, 'Both in and outside of Singapore'],
            [3, 'Mostly outside of Singapore']],
            label='4) Where have you been living in the past 10 years of your life?',
            widget=widgets.RadioSelect,
    )

    degree = models.BooleanField(
        choices=[
            [False, 'Undegraduate level'],
            [True, 'Graduate level'],
        ],
        label='5) Indicate the degree level you are currently pursuing.',
        widget=widgets.RadioSelect,
    )
    participation = models.IntegerField(
        choices=[
            [1,'Yes,once'],
            [2,'Yes, more than once'],
            [3,'No, this is my first time'],
        ],
        label='6) Have you ever participated in an economics experiment before?',
        widget=widgets.RadioSelect,
    )
    experience_econ = models.IntegerField(
        label='7) Have you studied economics as part of your undergraduate or graduate coursework?',
        choices=[
            [1,'Yes, introductory level'],
            [2,'Yes, intermediate or advanced level'],
            [3,'No, I have not taken any economics courses'],
        ],
        widget=widgets.RadioSelect,
    )
    experience_game = models.IntegerField(
        label='8) Have you studied game theory as part of your undergraduate or graduate coursework?',
        choices=[
            [1, 'Yes, introductory level'],
            [2, 'Yes, intermediate or advanced level'],
            [3, 'No, I have not taken any economics courses'],
        ],
        widget=widgets.RadioSelect,
    )
    risk_tolerance = models.IntegerField(
        label='9) How would you describe your risk tolerance?',
        choices=[
            [1,'I am very risk averse and conservative'],
            [2,'I am somewhat risk averse'],
            [3,'I am not very risk averse'],
            [4,'I am a risk lover'],
        ],
         widget = widgets.RadioSelect,
    )
    inform_source = models.IntegerField(
        label='10) How did you get informed about this experiment?',
        choices=[
            [1,'Through an advertisement on campus'],
            [2,'Through an email advertisement'],
            [3,'Through one of the experiment leaders'],
            [4,'Through a friend'],
            [5, 'Other'],
        ]
    )
    problem=models.IntegerField(
        label='11) Globally, which one of the following problems should be given the top priority?',
        choices=[
            [1,'Poverty and Inequality'],
            [2,'Environmental issues'],
            [3,'Corruption'],
            [4,'Other'],
        ]
    )
    Q1 = models.PositiveIntegerField(choices=[5,4,3,2,1], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name="12) I got a good understanding of the rules and payoffs in each game."
                                     )
    Q2 = models.PositiveIntegerField(choices=[5,4,3,2,1], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name="13) The instructions and explanations by the experimenters provided me with enough information "
                                                  "to understand how to earn points in the experiment."
                                     )
    Q3 = models.PositiveIntegerField(choices=[5,4,3,2,1], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name="14) Right before the experiment ended, I wished the experiment had more rounds."
                                     )
    Q4 = models.PositiveIntegerField(choices=[5,4,3,2,1], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name="15) With total points I earned, I believe that I was lucky during the experiment."
                                     )
    Q5 = models.PositiveIntegerField(choices=[5,4,3,2,1], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name="16) I believe I would collect more points if I had a chance to do the experiment again."
                                     )
    Q6 = models.PositiveIntegerField(choices=[5,4,3,2,1], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name="17) Fairness played a role in my decision-making."
                                     )
    Q7 = models.PositiveIntegerField(choices=[5,4,3,2,1], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name="18) The money I earn through participating in this experiment is a substantial contribution to my monthly budget.")

    Q8 = models.PositiveIntegerField(choices=[5, 4, 3, 2, 1], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name="19) Generally speaking, I only trust people that I have known for a while."
                                     )
    Q9 = models.PositiveIntegerField(choices=[5, 4, 3, 2, 1], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name="20) Generally speaking, there are only a few people I can trust completely."
                                     )
    Q10 = models.PositiveIntegerField(choices=[5, 4, 3, 2, 1], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name="21) Generally speaking, I think of myself as someone that can be trusted."
                                     )
