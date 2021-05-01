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
    aex = 20943.67
    aaex=22518.42
    bex=18080.46
    bbex=23329.63
    ist_s1  =[150,350,480,700,750,850,900]
    var1 = 0.25
    var11 = 0.22
    var2 = 0.00
    var22 = 0.05
    ist_s2  =[150,300,450,550,600,650,700]
    var3 = 0.20
    var33 = 0.21
    var4 = 0.06
    var44 = 0.15
    ist_s3  =[450,500,1600,1800,2000]
    var5 = 0.31
    var55 = 0.35
    var6 = 0.00
    var66 = 0.05
    s1_a1 = [21439.67, 21239.67, 21163.67 , 20943.67 , 20893.67, 20793.67, 20743.67]
    s1_a2 = [23068.42, 22868.42, 22738.42, 22518.42, 22468.42, 22368.42, 22318.42]
    s1_b1 = 18080.46
    s1_b2 = 23329.63

    s1_a1_1 = s1_a1[0]
    s1_a1_2 = s1_a1[1]
    s1_a1_3 = s1_a1[2]
    s1_a1_4 = s1_a1[3]
    s1_a1_5 = s1_a1[4]
    s1_a1_6 = s1_a1[5]
    s1_a1_7 = s1_a1[6]


    s1_a2_1 = s1_a2[0]
    s1_a2_2 = s1_a2[1]
    s1_a2_3 = s1_a2[2]
    s1_a2_4 = s1_a2[3]
    s1_a2_5 = s1_a2[4]
    s1_a2_6 = s1_a2[5]
    s1_a2_7 = s1_a2[6]

    ##SERIE_2
    s2_a1 = [21668.64, 21518.64, 21368.64, 21268.64, 21218.64, 21168.64, 21118.64]
    s2_a2 = [26567.86, 26417.86, 26267.86, 26167.86, 26117.86, 26067.86, 26017.86]
    s2_b1 = 18663.70
    s2_b2 = 26829.07

    s2_a1_1 = s2_a1[0]
    s2_a1_2 = s2_a1[1]
    s2_a1_3 = s2_a1[2]
    s2_a1_4 = s2_a1[3]
    s2_a1_5 = s2_a1[4]
    s2_a1_6 = s2_a1[5]
    s2_a1_7 = s2_a1[6]


    s2_a2_1 = s2_a2[0]
    s2_a2_2 = s2_a2[1]
    s2_a2_3 = s2_a2[2]
    s2_a2_4 = s2_a2[3]
    s2_a2_5 = s2_a2[4]
    s2_a2_6 = s2_a2[5]
    s2_a2_7 = s2_a2[6]


    ##SERIE_3
    s3_a1 = [19268.97, 19218.97, 18118.97, 17918.97, 17718.97]
    s3_a2 = [23834.90, 23884.90, 22784.90, 22584.90, 22384.90]
    s3_b1 = 11664.81
    s3_b2 = 24496.11

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

    s2_HL_1 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s2_HL_2 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s2_HL_3 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s2_HL_4 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s2_HL_5 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s2_HL_6 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    s2_HL_7 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)

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
        self.participant.vars['HL_row'] = random.randint(1,7)
        self.participant.vars['HL_row_3'] = random.randint(1,5)

        # select one row randomly for payment (from module random)
        self.participant.vars['HL_random'] = random.randint(1,7)
        self.participant.vars['HL_random_3'] = random.randint(1,5)

        # select the number x that defines the outcome of the lottery (if x<=p, outcome is left f1 or f3, otherwise f2 or f4)
        self.participant.vars['HL_scenario'] = random.randint(1,100)

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
                   self.HL_7,]

        choices_s2 = [self.s2_HL_1,
                   self.s2_HL_2,
                   self.s2_HL_3,
                   self.s2_HL_4,
                   self.s2_HL_5,
                   self.s2_HL_6,
                   self.s2_HL_7,
                   ]

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
            if self.participant.vars['HL_scenario'] <= 20:
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
            if self.participant.vars['HL_scenario'] <= 20 :
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
            if self.participant.vars['HL_scenario'] <= 10:
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
