from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import locale
locale.setlocale(locale.LC_ALL,'')


author = 'Ruggiero Rippo'

doc = """
    MPL risk elicitation à la Tanaka et al 2010
"""

import random

class Constants(BaseConstants):
    name_in_url = 'Fase2'
    players_per_group = None
    num_rounds = 1
    # these are the lottery payoffs, f1 and f2 refer to lottery A and f3 and f4 to lottery B
    ##SERIE_1
    ist  =[500,450,400,350,300,250,200,150,100,80]
    var1 = 0.2
    var2 = 0.1
    var3 = 0.3
    var4 = 0.4
    var5 = 0.5
    var6 = 0.25
    s1_a1 = [4550, 4500, 4450 , 4400 , 4350, 4330, 4300, 4200, 4280, 4230]
    s1_a2 = [5000, 5100, 5150, 5200, 5250, 5300, 5350, 5400, 5420, 5450]
    s1_b1 = 3500
    s1_b2 = 6000

    s1_a1_1 = s1_a1[0]
    s1_a1_2 = s1_a1[1]
    s1_a1_3 = s1_a1[2]
    s1_a1_4 = s1_a1[3]
    s1_a1_5 = s1_a1[4]
    s1_a1_6 = s1_a1[5]
    s1_a1_7 = s1_a1[6]
    s1_a1_8 = s1_a1[7]
    s1_a1_9 = s1_a1[8]
    s1_a1_10 = s1_a1[9]

    s1_a2_1 = s1_a2[0]
    s1_a2_2 = s1_a2[1]
    s1_a2_3 = s1_a2[2]
    s1_a2_4 = s1_a2[3]
    s1_a2_5 = s1_a2[4]
    s1_a2_6 = s1_a2[5]
    s1_a2_7 = s1_a2[6]
    s1_a2_8 = s1_a2[7]
    s1_a2_9 = s1_a2[8]
    s1_a2_10 = s1_a2[9]

    ##SERIE_2
    s2_a1 = [3550, 3500, 3450, 3400, 3350, 3330, 3300, 3200, 3280, 3230]
    s2_a2 = [6000, 6100, 6150, 6200, 6250, 6300, 6350, 6400, 6420, 6450]
    s2_b1 = 2500
    s2_b2 = 7000

    s2_a1_1 = s2_a1[0]
    s2_a1_2 = s2_a1[1]
    s2_a1_3 = s2_a1[2]
    s2_a1_4 = s2_a1[3]
    s2_a1_5 = s2_a1[4]
    s2_a1_6 = s2_a1[5]
    s2_a1_7 = s2_a1[6]
    s2_a1_8 = s2_a1[7]
    s2_a1_9 = s2_a1[8]
    s2_a1_10 = s2_a1[9]

    s2_a2_1 = s2_a2[0]
    s2_a2_2 = s2_a2[1]
    s2_a2_3 = s2_a2[2]
    s2_a2_4 = s2_a2[3]
    s2_a2_5 = s2_a2[4]
    s2_a2_6 = s2_a2[5]
    s2_a2_7 = s2_a2[6]
    s2_a2_8 = s2_a2[7]
    s2_a2_9 = s2_a2[8]
    s2_a2_10 = s2_a2[9]

    ##SERIE_3
    s3_a1 = [4550, 4500, 4450, 4400, 4350]
    s3_a2 = [5000, 5100, 5150, 5200, 5250]
    s3_b1 = 3500
    s3_b2 = 6000

    s3_a1_1 = s3_a1[0]
    s3_a1_2 = s3_a1[1]
    s3_a1_3 = s3_a1[2]
    s3_a1_4 = s3_a1[3]
    s3_a1_5 = s3_a1[4]

    s3_a2_1 = s3_a2[0]
    s3_a2_2 = s3_a2[1]
    s3_a2_3 = s3_a2[2]
    s3_a2_4 = s3_a2[3]
    s3_a2_5 = s3_a2[4]

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):

    # This is for main choices, each variable is one row in the choice table MPL
    HL_1 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_2 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_3 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_4 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_5 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_6 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_7 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_8 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_9 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_10 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)

    s2_HL_1 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s2_HL_2 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s2_HL_3 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s2_HL_4 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s2_HL_5 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s2_HL_6 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s2_HL_7 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s2_HL_8 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s2_HL_9 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s2_HL_10 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)

    s3_HL_1 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s3_HL_2 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s3_HL_3 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s3_HL_4 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s3_HL_5 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)

    HL = models.IntegerField(choices=[[1,'A'],[2,'B']],widget=widgets.RadioSelectHorizontal,initial=0)



    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff_HL(self):
        #*******************************************
        # select random row and random outcome
        #*******************************************
        self.participant.vars['HL_series']=random.randint(1,3)
        #
        self.participant.vars['HL_row'] = random.randint(1,10)
        self.participant.vars['HL_row_3'] = random.randint(1,5)

        # select one row randomly for payment (from module random)
        self.participant.vars['HL_random'] = random.randint(1,10)
        self.participant.vars['HL_random_3'] = random.randint(1,5)

        # select the number x that defines the outcome of the lottery (if x<=p, outcome is left f1 or f3, otherwise f2 or f4)
        # write it to participant.vars['HL_random']

        #*******************************************
        # select choices in correspondence to random row
        #*******************************************
        choices_s1 = [self.HL_1,
                   self.HL_2,
                   self.HL_3,
                   self.HL_4,
                   self.HL_5,
                   self.HL_6,
                   self.HL_7,
                   self.HL_8,
                   self.HL_9,
                   self.HL_10]

        choices_s2 = [self.s2_HL_1,
                   self.s2_HL_2,
                   self.s2_HL_3,
                   self.s2_HL_4,
                   self.s2_HL_5,
                   self.s2_HL_6,
                   self.s2_HL_7,
                   self.s2_HL_8,
                   self.s2_HL_9,
                   self.s2_HL_10]

        choices_s3=[self.s3_HL_1,
                   self.s3_HL_2,
                   self.s3_HL_3,
                   self.s3_HL_4,
                   self.s3_HL_5]

        # create a list with all choices of the player (see self)
        self.participant.vars['HL_choice_s1'] = choices_s1[self.participant.vars['HL_row']-1]
        self.participant.vars['HL_choice_s2'] = choices_s2[self.participant.vars['HL_row']-1]
        self.participant.vars['HL_choice_s3'] = choices_s3[self.participant.vars['HL_row_3']-1]

        # select from the list the choice in correspondence to the randomly drawn row (notice the offset)
        # write it to participant.vars['HL_choice']

        #*******************************************
        # Compute here the payoffs
        #*******************************************
        if self.participant.vars['HL_series'] == 1:
            if self.participant.vars['HL_random'] <= self.participant.vars['HL_row']:
            # if the random number is smaller equal than the random row
                if self.participant.vars['HL_choice_s1'] == 1: #A
                # if the choice was A
                    self.participant.vars['payoff_HL'] = Constants.s1_a1[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['payoff_HL'] = Constants.s1_b1
            else:
            # if the random number is larger than the random row
                if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                    self.participant.vars['payoff_HL'] = Constants.s1_a2[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['payoff_HL'] = Constants.s1_b2

        elif self.participant.vars['HL_series'] == 2:
            if self.participant.vars['HL_random'] <= self.participant.vars['HL_row']:
            # if the random number is smaller equal than the random row
                if self.participant.vars['HL_choice_s2'] == 1: #A
                # if the choice was A
                    self.participant.vars['payoff_HL'] = Constants.s2_a1[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['payoff_HL'] = Constants.s2_b1
            else:
            # if the random number is larger than the random row
                if self.participant.vars['HL_choice_s2'] == 1 :#A
                    # if the choice was A
                    self.participant.vars['payoff_HL'] = Constants.s2_a2[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['payoff_HL'] = Constants.s2_b2

        else:
            if self.participant.vars['HL_random_3'] <= self.participant.vars['HL_row_3']:
            # if the random number is smaller equal than the random row
                if self.participant.vars['HL_choice_s3'] == 1: #A
                # if the choice was A
                    self.participant.vars['payoff_HL'] = Constants.s3_a1[self.participant.vars['HL_row_3']-1]
                    # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['payoff_HL'] = Constants.s3_b1
            else:
            # if the random number is larger than the random row
                if self.participant.vars['HL_choice_s3'] == 1 :#A
                    # if the choice was A
                    self.participant.vars['payoff_HL'] = Constants.s3_a2[self.participant.vars['HL_row_3']-1]
                    # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['payoff_HL'] = Constants.s3_b2


        self.payoff = self.participant.vars['payoff_HL']
        # write the payoff to player.payoff
