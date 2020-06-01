from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=10, participation_fee=2800, doc="",
    use_browser_bots=0,
)


SESSION_CONFIGS = [

    dict(
        name='inspection_game',
        display_name = '4 Games',
        num_demo_participants = 2,
        app_sequence = ['Game1','Game2','Game3','Game4','payment_info1','survey'],
    ),
    dict(
        name='survey',
        display_name ='Survey',
        num_demo_participants =1,
        app_sequence =['survey'],
    )

]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'KZT'
USE_POINTS = True

ROOMS = [
    dict(
        name='trial',
        display_name='Room for trainings',
        participant_label_file='_rooms/trial.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
    dict(name='session1', display_name= 'Room for session 1 ', participant_label_file='_rooms/session1.txt'),
    dict(name='session2', display_name= 'Room for session 2 ', participant_label_file='_rooms/session2.txt'),
    dict(name='MPP2021', display_name= 'Room for trial session (MPP2021)', participant_label_file='_rooms/MPP2021.txt')
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


