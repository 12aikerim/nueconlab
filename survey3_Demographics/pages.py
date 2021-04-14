from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'female', 'marital_status', 'children', 'hometown', 'school_status', 'academic',
                  'field_study', 'GPA', 'mother_education', 'father_education', 'employment_status', 'income_level',
                  'mother_employment', 'father_employment']

class Results(Page):
    pass

page_sequence = [Demographics]
