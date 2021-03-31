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


author = 'Ruggiero Rippo'

doc = """
Introduction to the experiment
"""


class Constants(BaseConstants):
    name_in_url = 'Intro'
    num_rounds = 1
    players_per_group = None
    app_name = 'Intro'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass