from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class PSM1(Page):
    form_model = 'player'
    form_fields = ['APP1', 'CPI1', 'CPV1', 'COM1', 'SS1', 'APP7']

class PSM2(Page):
    form_model = 'player'
    form_fields = ['APP2', 'CPI2', 'CPV2', 'COM2', 'SS2', 'CPV9']

class PSM3(Page):
    form_model = 'player'
    form_fields = ['APP3', 'CPI3', 'CPV3', 'COM3', 'SS3', 'SS7']

class PSM4(Page):
    form_model = 'player'
    form_fields = ['APP4', 'CPI4', 'CPV4', 'COM4', 'SS4']

class PSM5(Page):
    form_model = 'player'
    form_fields = ['APP5', 'CPV5', 'CPV6', 'COM5', 'SS5']

class PSM6(Page):
    form_model = 'player'
    form_fields = ['APP6', 'CPV7', 'CPV8', 'COM6', 'SS6']

class Results(Page):
    pass

page_sequence = [PSM1, PSM2, PSM3, PSM4, PSM5, PSM6]
