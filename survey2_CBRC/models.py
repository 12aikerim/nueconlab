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


author = 'Your name here'

doc = """
Your app description
"""



class Constants(BaseConstants):
    name_in_url = 'survey_cbrc'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    networks = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='1) Do you believe that networks are necessary for success?',
        widget=widgets.RadioSelect,
    )
    bribes = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='2) Do bribes are necessary to operate a business in Kazakhstan?',
        widget=widgets.RadioSelect,
    )
    risk = models.StringField(
        choices=[['RA', 'Risk averse'], ['RN', 'Risk neutral'], ['RT', 'Risk taker']],
        label='3) Do you consider yourself?',
        widget=widgets.RadioSelect,
    )
    predictor = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='4) Do you consider yourself a good predictor about random future events?',
        widget=widgets.RadioSelect,
    )
    cheating_on_tests = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'],
                 ['D', 'Disagree'], ['SD', 'Strongly disagree']],
        label='5) Cheating on college tests is morally wrong.',
        widget=widgets.RadioSelect,
    )
    punishment_for_lying = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'],
                 ['D', 'Disagree'], ['SD', 'Strongly disagree']],
        label='6) When a student who denies cheating is found guilty, the student should receive additional'
              'punishment for lying',
        widget=widgets.RadioSelect,
    )
    reward_honesty = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'],
                 ['D', 'Disagree'], ['SD', 'Strongly disagree']],
        label='7) If a student accused of cheating admits having cheated, the punishment should be reduced to'
              'reward honesty.',
        widget=widgets.RadioSelect,
    )
    report_cheating = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'],
                 ['D', 'Disagree'], ['SD', 'Strongly disagree']],
        label='8) A student who sees another student cheating and reports it should refuse to identify the cheater.',
        widget=widgets.RadioSelect,
    )
    report_by_name = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'],
                 ['D', 'Disagree'], ['SD', 'Strongly disagree']],
        label='9) Students should report by name anyone seen cheating.',
        widget=widgets.RadioSelect,
    )
    cheating_unethical = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'],
                 ['D', 'Disagree'], ['SD', 'Strongly disagree']],
        label='10) Most students who cheat are unethical people.',
        widget=widgets.RadioSelect,
    )
    risk_cheating = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'],
                 ['D', 'Disagree'], ['SD', 'Strongly disagree']],
        label='11) There is really nothing wrong with cheating, other than the risk of being caught.',
        widget=widgets.RadioSelect,
    )
    innocent_cheating = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'],
                 ['D', 'Disagree'], ['SD', 'Strongly disagree']],
        label='12) Most students who are accused of cheating are actually innocent.',
        widget=widgets.RadioSelect,
    )
    never_cheat = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'],
                 ['D', 'Disagree'], ['SD', 'Strongly disagree']],
        label='13) Most college students never cheat.',
        widget=widgets.RadioSelect,
    )
    cheating_lying = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'],
                 ['D', 'Disagree'], ['SD', 'Strongly disagree']],
        label='14) It is lying when a student who cheated denies it.',
        widget=widgets.RadioSelect,
    )
    corruption_in_KZ = models.StringField(
        choices=[['5', 'A very serious problem'], ['4', 'A serious problem'], ['3', 'A somewhat serious problem'],
                 ['2', 'Not a serious problem'], ['1', 'Not a problem at all']],
        label='15) Corruption in Kazakhstan today is.',
        widget=widgets.RadioSelect,
    )
    corruption_10yearsago = models.StringField(
        choices=[['5', 'Much worse'], ['4', 'Worse'], ['3', 'The same'], ['2', 'Reduced'], ['1', 'Reduced much']],
        label='16) Compared to 10 years ago, corruption in Kazakhstan today is:',
        widget=widgets.RadioSelect,
    )
    corruption_occurrence = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='17) Corruption is a natural occurrence and part of our daily life, so denouncing it is unnecessary:',
        widget=widgets.RadioSelect,
    )
    corruption_gov = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='18) In the government of Kazakhstan, there is no sincere desire and will to combat corruption:',
        widget=widgets.RadioSelect,
    )
    anti_corruption = models.StringField(
        choices=[['SA', 'Strongly agree'], ['A', 'Agree'],
                 ['U', 'Undecided (or if you do not understand the statement)'], ['D', 'Disagree'],
                 ['SD', 'Strongly disagree']],
        label='19) Current government anti-corruption strategies for combating corruption are effective:',
        widget=widgets.RadioSelect,
    )
    corruption_perp = models.StringField(
        choices=[['C', 'Citizens'], ['B', 'Businessmen'], ['P', 'Politicians'], ['B', 'Bureaucrats']],
        label='20) Corruption is perpetuated mostly by:',
        widget=widgets.RadioSelect,
    )
    corruption_compare = models.StringField(
        choices=[['1', 'More corrupt'], ['2', 'Equal'], ['3', 'Less corrupt']],
        label='21) How do you compare Kazakhstan with other Central Asian countries regarding corruption?',
        widget=widgets.RadioSelect,
    )
    beh1 = models.StringField(
        choices=[['AA', 'Always acceptable'], ['UA', 'Usually acceptable'], ['SA', 'Sometimes acceptable'],
                 ['NA', 'Not acceptable']],
        label='22) A public officer being recruited on the basis of family ties and friendship networks?',
        widget=widgets.RadioSelect,
    )
    beh2 = models.StringField(
        choices=[['AA', 'Always acceptable'], ['UA', 'Usually acceptable'], ['SA', 'Sometimes acceptable'],
                 ['NA', 'Not acceptable']],
        label='23) A public officer asking for a bribe to speed up administrative procedures.',
        widget=widgets.RadioSelect,
    )
    beh3 = models.StringField(
        choices=[['AA', 'Always acceptable'], ['UA', 'Usually acceptable'], ['SA', 'Sometimes acceptable'],
                 ['NA', 'Not acceptable']],
        label='24) A private citizen offering a bribe to a public official to speed up administrative procedures.',
        widget=widgets.RadioSelect,
    )
    beh4 = models.StringField(
        choices=[['AA', 'Always acceptable'], ['UA', 'Usually acceptable'], ['SA', 'Sometimes acceptable'],
                 ['NA', 'Not acceptable']],
        label='25) An elected official taking public funds for private use.',
        widget=widgets.RadioSelect,
    )
    beh5 = models.StringField(
        choices=[['AA', 'Always acceptable'], ['UA', 'Usually acceptable'], ['SA', 'Sometimes acceptable'],
                 ['NA', 'Not acceptable']],
        label='26) An elected official using stolen public funds to assist his or her community.',
        widget=widgets.RadioSelect,
    )
    beh6 = models.StringField(
        choices=[['AA', 'Always acceptable'], ['UA', 'Usually acceptable'], ['SA', 'Sometimes acceptable'],
                 ['NA', 'Not acceptable']],
        label='27) A law enforcement officer (police, customs, immigration, army) asking for a bribe.',
        widget=widgets.RadioSelect,
    )
    beh7 = models.StringField(
        choices=[['AA', 'Always acceptable'], ['UA', 'Usually acceptable'], ['SA', 'Sometimes acceptable'],
                 ['NA', 'Not acceptable']],
        label='28) A private company owner asking for a bribe from a job applicant.',
        widget=widgets.RadioSelect,
    )
    beh8 = models.StringField(
        choices=[['AA', 'Always acceptable'], ['UA', 'Usually acceptable'], ['SA', 'Sometimes acceptable'],
                 ['NA', 'Not acceptable']],
        label='29) A public company official asking for a bribe from a job applicant.',
        widget=widgets.RadioSelect,
    )
    bureaucracy1 = models.StringField(
        choices=[['1', 'Not at all important'], ['2', 'Slightly Important'], ['3', 'Important'],
                ['4', 'Fairly Important'], ['5', 'Extremely important']],
        label='30) Reporting daily activities as part of a bureaucratic process that requires submitting a report to '
              'managers or supervisors is:',
        widget=widgets.RadioSelect,
    )
