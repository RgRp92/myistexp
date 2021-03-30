from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)

author = 'RR'

doc = """
Beliefs Task
"""
# To read from the CSV file
import pandas as pd

class Constants(BaseConstants):
    name_in_url = 'Fase1SF'
    num_rounds = 3
    players_per_group = None
    app_name = 'beliefs_task'

    # Colors picked with a good pallete
    hex_colors = ["#F8766D", "#00BFC4"]


class Subsession(BaseSubsession):
    def creating_session(self):

        farm_dat = pd.read_csv("farmdata/data.csv")
        self.session.vars["beliefs_farm_dat"] = farm_dat
        self.session.vars["beliefs_hex_colors"] = ["#ff9933", "#00BFC4"]

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    labelset    = models.IntegerField(default = 0)

    final_payment = models.StringField()

    bin1  = models.IntegerField(initial = 0)
    bin2  = models.IntegerField(initial = 0)
    bin3  = models.IntegerField(initial = 0)
    bin4  = models.IntegerField(initial = 0)
    bin5  = models.IntegerField(initial = 0)
    bin6  = models.IntegerField(initial = 0)
    bin7  = models.IntegerField(initial = 0)
    bin8  = models.IntegerField(initial = 0)
    bin9  = models.IntegerField(initial = 0)
    bin10 = models.IntegerField(initial = 0)

    rep_1 = models.CharField(label="", choices=[['SI', 'SI'],['NO', 'NO']])

    rep_2 = models.CharField(label="", choices=[  ['SI', 'SI'],['NO', 'NO']])

    pref1 = models.IntegerField(default = 0, min=0, max=100, label="")
    pref2 = models.IntegerField(default = 0, min=0, max=100, label="")
    pref3 = models.IntegerField(default = 0, min=0, max=100, label="")

    sum_token = models.FloatField(min=100, max=100)

