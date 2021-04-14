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
    name_in_url = 'survey_demographics'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    age = models.IntegerField(label='1) What is your age?', min=18, max=64)
    female = models.StringField(
        choices=[['0', 'Male'], ['1', 'Female']],
        label='2) What is your gender?',
        widget=widgets.RadioSelectHorizontal,
    )
    marital_status = models.StringField(
        choices=[['1', 'Single, never married'], ['2', 'Married or domestic partnership'], ['3', 'Widowed'],
                 ['4', 'Divorced'], ['5', 'Separated']],
        label='3) What is your marital status?',
        widget=widgets.RadioSelect,
    )
    children = models.IntegerField(label='4) How many children do you have?', min=0, max=10)
    hometown = models.IntegerField(label='5) What is your hometown?')
    school_status = models.StringField(
        choices=[['FS', 'Full-time student'], ['PS', 'Part-time student'],
                 ['NA', 'Not a student']],
        label='6) Are you currently?',
        widget=widgets.RadioSelect,
    )
    academic = models.StringField(
        choices=[['BSc', "Bachelor’s degree"], ['MSC', "Master’s degree"],
                 ['PhD', 'Doctorate degree'], ['ND', 'Non-degree']],
        label='7) What is your current program level?',
        widget=widgets.RadioSelect,
    )
    field_study = models.StringField(label='8) What is your field of study?')
    GPA = models.StringField(
        choices=[['1', '4.00-3.50'], ['2', '3.50-3.00'], ['3', '3.00-2.50'], ['4', '2.50-2.00'], ['5', '2.00-1.50'],
                 ['6', '1.50-1.00'], ['7', 'less than 1.00']],
        label='9) What is your current GPA?',
        widget=widgets.RadioSelect,
    )
    mother_education = models.StringField(
        choices=[['BSc', 'Bachelor’s degree'], ['MSC', 'Master’s degree'],
                 ['PhD', 'Doctorate degree'], ['ND', 'Non-degree']],
        label='10) Whats the highest degree of your mothers education?',
        widget=widgets.RadioSelect,
    )
    father_education = models.StringField(
        choices=[['BSc', 'Bachelor’s degree'], ['MSC', 'Master’s degree'],
                 ['PhD', 'Doctorate degree'], ['ND', 'Non-degree']],
        label='11) Whats the highest degree of your fathers education?',
        widget=widgets.RadioSelect,
    )
    employment_status = models.StringField(
        choices=[['1', 'Employed in private sector (local company)'],
                ['2', 'Employed in private sector (foreign company)'],
                ['3', 'Employed in public sector'], ['4', 'Employed in quasi-governmental sector'],
                ['5', 'Self-employed'], ['7', 'Unemployed']],
        label='12) Are you currently?',
        widget=widgets.RadioSelect,
    )
    income_level = models.StringField(
        choices=[['1', '0-50,000'], ['2', '50,000-100,000'], ['3', '100,000-150,000'], ['4', '150,000-200,000'],
               ['5', '200,000-250,000'], ['7', '250,000-300,000'], ['8', '300,000-350,000'], ['9', '350,000-400,000'],
               ['10', 'more than 400,000']],
        label='13) What is your monthly income? (in tenge, excluding stipend)',
        widget=widgets.RadioSelect,
    )
    mother_employment = models.StringField(
        choices=[['1', 'Employed in private sector (local company)'],
                 ['2', 'Employed in private sector (foreign company)'],
                 ['3', 'Employed in public sector'], ['4', 'Employed in quasi-governmental sector'],
                 ['5', 'Self-employed'], ['7', 'Unemployed']],
        label='14) Which sector is your mother employed?',
        widget=widgets.RadioSelect,
    )
    father_employment = models.StringField(
        choices=[['1', 'Employed in private sector (local company)'],
                 ['2', 'Employed in private sector (foreign company)'],
                 ['3', 'Employed in public sector'], ['4', 'Employed in quasi-governmental sector'],
                 ['5', 'Self-employed'], ['7', 'Unemployed']],
        label='15) Which sector is your father employed?',
        widget=widgets.RadioSelect,
    )
