from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender','citizen','residence', 'degree', 'participation','experience_econ','experience_game','risk_tolerance',
                   'inform_source','problem']


class QuestionaireOnExperiment(Page):
    form_model = 'player'
    form_fields = ['Q{}'.format(i) for i in range(1, 11)]

class FinalPageAfterSurvey(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    pass



page_sequence = [Demographics, QuestionaireOnExperiment,FinalPageAfterSurvey]
