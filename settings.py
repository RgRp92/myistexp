from os import environ

SESSION_CONFIGS = [
     dict(
        name='Test',
        display_name="Test",
        num_demo_participants=2,
        app_sequence=['Intro','Fase1', 'Fase2','Fase3','Fase4', 'FinalPayment']
     ),
    dict(
    name='TestSF',
        display_name="TestSF",
        num_demo_participants=2,
        app_sequence=['Intro','Fase1SF', 'Fase2SF','Fase3','Fase4', 'FinalPaymentSF']
     ),
     dict(
        name='Fase1',
        display_name="Fase1",
        num_demo_participants=1,
        app_sequence=['Fase1', 'Fase2','Fase3', 'FinalPayment']
     ),
     dict(
        name='Fase1SF',
        display_name="Fase1SF",
        num_demo_participants=1,
        app_sequence=['Fase1SF', 'Fase2SF','Fase3SF','FinalPaymentSF']
     ),
    dict(
        name='Fase2',
        display_name="Fase2",
        num_demo_participants=1,
        app_sequence=['Fase2','FinalPayment']
     ),
    dict(
        name='Fase2SF',
        display_name="Fase2SF",
        num_demo_participants=1,
        app_sequence=['Fase2SF']
     ),
    dict(
        name='Fase3',
        display_name="Fase3",
        num_demo_participants=1,
        app_sequence=['Fase3','FinalPayment']
     ),
    dict(
        name='Fase3SF',
        display_name="Fase3SF",
        num_demo_participants=1,
        app_sequence=['Fase3SF']
     ),
    dict(
        name='Fase4',
        display_name="Fase4",
        num_demo_participants=1,
        app_sequence=['Fase4']
     ),
    dict(
        name='Intro',
        display_name="Intro",
        num_demo_participants=2,
        app_sequence=['Intro']
     ),
    dict(
        name='FinalPayment',
        display_name="FinalPayment",
        num_demo_participants=5,
        app_sequence=['FinalPayment']
     ),
    dict(
        name='FinalPaymentSF',
        display_name="FinalPaymentSF",
        num_demo_participants=10,
        app_sequence=['FinalPaymentSF']
     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'd*234n^cxml5nkk09#r0%&%8$kt)pwi3qq)8jk36ts*y)nk)kf'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

PARTICIPANT_FIELDS = ['applearea']


