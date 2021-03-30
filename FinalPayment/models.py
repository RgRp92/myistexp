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

import random

author = 'Ruggiero Rippo'

doc = """
Random Draw for Final payment
"""


class Constants(BaseConstants):
    name_in_url = 'FinalPayment'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        winner = random.randint(1,10)
        app = random.randint(1 , 3)
        self.session.vars["winner"] = winner
        self.session.vars["app"] = app

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
