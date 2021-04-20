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


author = 'Zhanar'

doc = """
Survey on Public Service Motivation
"""


class Constants(BaseConstants):
    name_in_url = 'survey_psm'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    consent = models.BooleanField()
    APP1 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='1) I am interested in helping to improve public service',
        widget=widgets.RadioSelect,
    )
    CPI1 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='2) Meaningful public service is not important to me',
        widget=widgets.RadioSelect,
    )
    CPV1 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='3) I think equal opportunities for citizens are very important',
        widget=widgets.RadioSelect,
    )
    COM1 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='4) It is difficult for me to contain my feelings when I see people in distress',
        widget=widgets.RadioSelect,
    )
    SS1 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='5) Making a difference to society means more to me than personal achievements',
        widget=widgets.RadioSelect,
    )
    APP7 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='6) It is important to contribute to activities that tackle social problems',
        widget=widgets.RadioSelect,
    )
    APP2 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='1) I am satisfied when I see people benefiting from the public programs I was involved in',
        widget=widgets.RadioSelect,
    )
    CPI2 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='2) It is not important for me to contribute to the common good',
        widget=widgets.RadioSelect,
    )
    CPV2 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='3) It is important that citizens can rely on the continuous provision of public services',
        widget=widgets.RadioSelect,
    )
    COM2 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='4) I do not feel sympathetic to the plight of the underprivileged',
        widget=widgets.RadioSelect,
    )
    SS2 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='5) I am prepared to make sacrifices for the good of society',
        widget=widgets.RadioSelect,
    )
    CPV9 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='6) I personally identify with the aim of protecting individual liberties and rights',
        widget=widgets.RadioSelect,
    )
    APP3 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='1) I like to discuss topics regarding public programs and policies with others',
        widget=widgets.RadioSelect,
    )
    CPI3 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='2) I would prefer seeing public officials do what is best for the whole community, even if '
              'it harmed my interests',
        widget=widgets.RadioSelect,
    )
    CPV3 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='3) It is not fundamental that public services respond to the needs of citizens',
        widget=widgets.RadioSelect,
    )
    COM3 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='4) I empathize with other people who face difficulties',
        widget=widgets.RadioSelect,
    )
    SS3 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='5) I do not believe in putting civic duty before self',
        widget=widgets.RadioSelect,
    )
    SS7 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='6) I would agree to a good plan to make a better life for the poor, even if it costs me money',
        widget=widgets.RadioSelect,
    )
    APP4 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='1) I believe that public sector activities contribute to our general welfare',
        widget=widgets.RadioSelect,
    )
    CPI4 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='2) Serving the public interest is more important than helping a single individual',
        widget=widgets.RadioSelect,
    )
    CPV4 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='3) Decisions regarding public services should be democratic despite the time and effort it takes',
        widget=widgets.RadioSelect,
    )
    COM4 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='4) I have little compassion for people in need who are unwilling to take the first step to help '
              'themselves',
        widget=widgets.RadioSelect,
    )
    SS4 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='5) I am not willing to risk personal loss to help society',
        widget=widgets.RadioSelect,
    )
    APP5 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='1) I admire people who initiate or are involved in activities to aid my community',
        widget=widgets.RadioSelect,
    )
    CPV5 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='2) Everybody is entitled to a good service, even if it costs a lot of money',
        widget=widgets.RadioSelect,
    )
    CPV6 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='3) It is not fundamental that the interests of future generations are taken into account when '
              'developing public policies',
        widget=widgets.RadioSelect,
    )
    COM5 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='4) I get very upset when I see other people being treated unfairly',
        widget=widgets.RadioSelect,
    )
    SS5 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='5) People should not give back to society more than they get from it',
        widget=widgets.RadioSelect,
    )
    APP6 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='1) Contributing to public programs and policies helps me realize myself',
        widget=widgets.RadioSelect,
    )
    CPV7 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='2) To act ethically is not essential for public servants',
        widget=widgets.RadioSelect,
    )
    CPV8 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='3) I believe that public employees must always be aware of the legitimacy of their activities',
        widget=widgets.RadioSelect,
    )
    COM6 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='4) Considering the welfare of other is not important',
        widget=widgets.RadioSelect,
    )
    SS6 = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='5) Serving other citizens would give me a good feeling even if no one paid me for it',
        widget=widgets.RadioSelect,
    )
