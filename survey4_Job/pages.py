from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class JobAttributeIndicators(Page):
    form_model = 'player'
    form_fields = ['job_security', 'high_income', 'benefits_package', 'advancement', 'interesting_job', 'help_job',
                   'useful_job', 'work_hours', 'influential_people', 'prestigious_job']

class CareerPreferenceandExpectations(Page):
    form_model = 'player'
    form_fields = ['career_preference_variable', 'motivation', 'fedgov_job', 'state_job', 'private_job', 'SME',
                   'owner', 'banking', 'consulting', 'NPS', 'budget_sector']

class Results(Page):
    pass

page_sequence = [JobAttributeIndicators, CareerPreferenceandExpectations]
