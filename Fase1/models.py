from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)

author = 'RR'

doc = """
Beliefs Task
"""
# To read from the CSV file
import pandas as pd

class Constants(BaseConstants):
    name_in_url = 'Fase1'
    num_rounds = 3
    players_per_group = None
    app_name = 'Fase1'

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
    quiz = models.CharField(choices=[['0', '6.16'],['1', '20.16'],['2','17.16']],
                               widget= widgets.RadioSelectHorizontal,
                               label='1. In base alla figura mostrata quale sarà il vostro guadagno se il reddito varierà del + 2%',
                              blank=True,default = "")
    quiz2 = models.CharField(choices=[['1', '6.16'], ['0', '20.16'], ['2', '17.16']],
                               widget=widgets.RadioSelectHorizontal,
                               label='2.In base alla figura mostrata quale sarà il vostro guadagno se il reddito varierà del + 20%',
                              blank=True,default = "" )

    labelset = models.IntegerField(default = 0)

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

    rep_1 = models.CharField(label="", choices=[['SI', 'SI'],['NO','NO']], initial = "")

    rep_2 = models.CharField(label="", choices=[['SI', 'SI'],['NO', 'NO']], initial = "")

    pref1 = models.IntegerField(default = 0, min=0, max=100, initial=0, label="")
    pref2 = models.IntegerField(default = 0, min=0, max=100, initial=0, label="")
    pref3 = models.IntegerField(default = 0, min=0, max=100, initial=0, label="")

    sum_token = models.FloatField(min=100, max=100)

    w_amt = models.FloatField(default=0,min=0,label="")
