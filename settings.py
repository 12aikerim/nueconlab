from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1, participation_fee=2000, doc="",
    use_browser_bots=0,
)


SESSION_CONFIGS = [

    #dict(
      # name='inspection_game',
      # display_name = '4 Games',
      # num_demo_participants = 2,
       # app_sequence = ['Game1','Game2','Game3','Game4','payment_info1','survey'],
   #),
    dict(
        name='payment_info_dice',
        display_name = 'Payment info Dice',
        num_demo_participants = 1,
        app_sequence = ['payment_info_dice'],
    ),
    dict(
        name='donation',
        display_name = 'Donation Game',
        num_demo_participants = 2,
        app_sequence = ['donation'],
    ),
    dict(
        name='rolling_dice_game',
        display_name = 'Rolling Dice Game',
        num_demo_participants = 2,
        app_sequence = ['rolling_dice'],
    ),
    dict(
        name='experiment_rolling_dice',
        display_name = 'Experiment game',
        num_demo_participants = 2,
        app_sequence = ['survey1_PSM','rolling_dice','survey2_CBRC','dictator','survey3_Demographics','rolling_dice_2','survey4_Job','donation','payment_info_dice']
    ),
    dict(
        name='survey_psm',
        display_name ='Survey PSM',
        num_demo_participants =1,
        app_sequence =['survey1_PSM'],
    ),
    dict(
        name='survey_cbrc',
        display_name ='Survey Corruption Bureaucracy',
        num_demo_participants =1,
        app_sequence =['survey2_CBRC'],
    ),
    dict(
        name='survey_demographics',
        display_name ='Survey Demographics',
        num_demo_participants =1,
        app_sequence =['survey3_Demographics'],
    ),
    dict(
        name='survey_job',
        display_name ='Survey Job attributes and Career Preferences',
        num_demo_participants =1,
        app_sequence =['survey4_Job'],
    ),
    dict(
        name='dictator',
        display_name ='Dictatorship Game',
        num_demo_participants =2,
        app_sequence =['dictator'],
    ),
    ]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'KZT'
USE_POINTS = False

ROOMS = [
    dict(
        name='trial_mpp663',
        display_name='Room for trial session (MPP663)',
        participant_label_file='_rooms/MPP663.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
    #dict(name='one', display_name= 'Room #1 SG session', participant_label_file='_rooms/room1.txt'),
   # dict(name='two', display_name= 'Room #2 SG session', participant_label_file='_rooms/room2.txt'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = '6lertt4wlb09zj@4wyuy-p-6)i$vh!ljwx&r9bti6kgw54k-h8'

INSTALLED_APPS = ['otree']


