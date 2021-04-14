from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class CorruptionBureaucracyRisk(Page):
    form_model = 'player'
    form_fields = ['networks', 'bribes', 'risk', 'predictor', 'cheating_on_tests', 'punishment_for_lying',
                  'reward_honesty', 'report_cheating', 'report_by_name', 'cheating_unethical', 'risk_cheating',
                  'innocent_cheating', 'never_cheat', 'cheating_lying', 'corruption_in_KZ','corruption_10yearsago',
                  'corruption_occurrence', 'corruption_gov', 'anti_corruption', 'corruption_perp', 'corruption_compare',
                  'beh1', 'beh2', 'beh3', 'beh4', 'beh5', 'beh6', 'beh7', 'beh8', 'bureaucracy1']

class Results(Page):
    pass

page_sequence = [CorruptionBureaucracyRisk]
