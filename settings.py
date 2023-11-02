from os import environ
import random
SESSION_CONFIGS = [
     dict(
         name='InvestmentDecisions',

         app_sequence=['intro_exp2','inv_exp2','financialliteracy','cognitive'],
         num_demo_participants=600,
         use_browser_bots = False,
     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.0005, participation_fee=1.50, doc=""
)

PARTICIPANT_FIELDS = ['decision', 'a', 'wealth', 'dec', 'returns', 'inv', 'treat','list1','list2','list3','list4','list5','list6','list7','list8','list9','list10','time']
SESSION_FIELDS = ['order', 'order2', 'liste', 'liste2', 'treatment', 'pricelist', 'seq_list1']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False

ROOMS = [
    dict(
        name='survey',
        display_name='Matching Survey'
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5602840073739'

