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
    name_in_url = 'survey_job'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    job_security = models.StringField(
        choices=[['1', 'Not at all important'], ['2', 'Slightly Important'], ['3', 'Important'],
                ['4', 'Fairly Important'], ['5', 'Extremely important']],
        label='1) Job security',
        widget=widgets.RadioSelect,
    )
    high_income = models.StringField(
        choices=[['1', 'Not at all important'], ['2', 'Slightly Important'], ['3', 'Important'],
                 ['4', 'Fairly Important'], ['5', 'Extremely important']],
        label='2) High income',
        widget=widgets.RadioSelect,
    )
    benefits_package = models.StringField(
        choices=[['1', 'Not at all important'], ['2', 'Slightly Important'], ['3', 'Important'],
                 ['4', 'Fairly Important'], ['5', 'Extremely important']],
        label='3) Good benefits package',
        widget=widgets.RadioSelect,
    )
    advancement = models.StringField(
        choices=[['1', 'Not at all important'], ['2', 'Slightly Important'], ['3', 'Important'],
                 ['4', 'Fairly Important'], ['5', 'Extremely important']],
        label='4) Opportunities for advancement',
        widget=widgets.RadioSelect,
    )
    interesting_job = models.StringField(
        choices=[['1', 'Not at all important'], ['2', 'Slightly Important'], ['3', 'Important'],
                 ['4', 'Fairly Important'], ['5', 'Extremely important']],
        label='5) A job you find interesting',
        widget=widgets.RadioSelect,
    )
    help_job = models.StringField(
        choices=[['1', 'Not at all important'], ['2', 'Slightly Important'], ['3', 'Important'],
                 ['4', 'Fairly Important'], ['5', 'Extremely important']],
        label='6) A job that allows you to help other people',
        widget=widgets.RadioSelect,
    )
    useful_job = models.StringField(
        choices=[['1', 'Not at all important'], ['2', 'Slightly Important'], ['3', 'Important'],
                 ['4', 'Fairly Important'], ['5', 'Extremely important']],
        label='7) A job that is useful for society',
        widget=widgets.RadioSelect,
    )
    work_hours = models.StringField(
        choices=[['1', 'Not at all important'], ['2', 'Slightly Important'], ['3', 'Important'],
                 ['4', 'Fairly Important'], ['5', 'Extremely important']],
        label='8) Reasonable work hours',
        widget=widgets.RadioSelect,
    )
    influential_people = models.StringField(
        choices=[['1', 'Not at all important'], ['2', 'Slightly Important'], ['3', 'Important'],
                 ['4', 'Fairly Important'], ['5', 'Extremely important']],
        label='9) Opportunities to meet influential people',
        widget=widgets.RadioSelect,
    )
    prestigious_job = models.StringField(
        choices=[['1', 'Not at all important'], ['2', 'Slightly Important'], ['3', 'Important'],
                 ['4', 'Fairly Important'], ['5', 'Extremely important']],
        label='10) A job that others consider prestigious',
        widget=widgets.RadioSelect,
    )
    career_preference_variable = models.StringField(
        choices=[['1', 'I would prefer to work in the public sector'],
                ['2', 'I would prefer to work in the private sector'],
                ['3', 'I would prefer to work in the international organization'],
                ['4', 'I would prefer to work in the quasi-governmental sector'],
                ['5', 'I would prefer to have my own business'],
                ['6', 'Do not plan to work']],
        label='1) Which of the following statements best describes your career preferences?',
        widget=widgets.RadioSelect,
    )
    motivation = models.StringField(
        choices=[['1', 'Better salary'], ['2', 'Job security and staff retention'],
                 ['3', 'Better service to community'], ['4', 'Political connections'], ['5', 'Other']],
        label='2) What is the primary reason and motivation in your previous section?',
        widget=widgets.RadioSelect,
    )
    fedgov_job = models.StringField(
        choices=[['1', 'Very likely'], ['2', 'Likely'], ['3', 'Neutral'], ['4', 'Not Likely'], ['5', 'Very Unlikely']],
        label='3) A job in the federal government',
        widget=widgets.RadioSelect,
    )
    state_job = models.StringField(
        choices=[['1', 'Very likely'], ['2', 'Likely'], ['3', 'Neutral'], ['4', 'Not Likely'], ['5', 'Very Unlikely']],
        label='4) A job in the state or local government',
        widget=widgets.RadioSelect,
    )
    private_job = models.StringField(
        choices=[['1', 'Very likely'], ['2', 'Likely'], ['3', 'Neutral'], ['4', 'Not Likely'], ['5', 'Very Unlikely']],
        label='5) A job in a private-sector corporation',
        widget=widgets.RadioSelect,
    )
    SME = models.StringField(
        choices=[['1', 'Very likely'], ['2', 'Likely'], ['3', 'Neutral'], ['4', 'Not Likely'], ['5', 'Very Unlikely']],
        label='6) A job in a small or medium-sized private sector business',
        widget=widgets.RadioSelect,
    )
    owner = models.StringField(
        choices=[['1', 'Very likely'], ['2', 'Likely'], ['3', 'Neutral'], ['4', 'Not Likely'], ['5', 'Very Unlikely']],
        label='7) A job as an owner of a private business',
        widget=widgets.RadioSelect,
    )
    banking = models.StringField(
        choices=[['1', 'Very likely'], ['2', 'Likely'], ['3', 'Neutral'], ['4', 'Not Likely'], ['5', 'Very Unlikely']],
        label='8) A job in the banking of finance sectors',
        widget=widgets.RadioSelect,
    )
    consulting = models.StringField(
        choices=[['1', 'Very likely'], ['2', 'Likely'], ['3', 'Neutral'], ['4', 'Not Likely'], ['5', 'Very Unlikely']],
        label='9) A job in a consulting',
        widget=widgets.RadioSelect,
    )
    NPS = models.StringField(
        choices=[['1', 'Very likely'], ['2', 'Likely'], ['3', 'Neutral'], ['4', 'Not Likely'], ['5', 'Very Unlikely']],
        label='10) A job in an organization in the non-profit sector',
        widget=widgets.RadioSelect,
    )
    budget_sector = models.StringField(
        choices=[['1', 'Very likely'], ['2', 'Likely'], ['3', 'Neutral'], ['4', 'Not Likely'], ['5', 'Very Unlikely']],
        label='11) A job in the government budget sector (e.g., public health, science, education, culture)',
        widget=widgets.RadioSelect,
    )




