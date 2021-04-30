from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Ruggiero Rippo'

doc = """
    MPL risk elicitation à la Tanaka et al 2010
"""

import random

class Constants(BaseConstants):
    name_in_url = 'Fase3'
    players_per_group = None
    num_rounds = 1
    # these are the lottery payoffs, f1 and f2 refer to lottery A and f3 and f4 to lottery B
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
    prb1 = 15
    prb2 = 85
    prb3 = 20
    prb4 = 80
    prb5 = 10
    prb6 = 90
    rs1_a1 = [21439.67, 21239.67, 21163.67 , 20943.67 , 20893.67, 20793.67, 20743.67]
    rs1_a2 = [23068.42, 22868.42, 22738.42, 22518.42, 22468.42, 22368.42, 22318.42]
    rs1_b1 = 18080.46
    rs1_b2 = 23329.63

    rs1_a1_1 = rs1_a1[0]
    rs1_a1_2 = rs1_a1[1]
    rs1_a1_3 = rs1_a1[2]
    rs1_a1_4 = rs1_a1[3]
    rs1_a1_5 = rs1_a1[4]
    rs1_a1_6 = rs1_a1[5]
    rs1_a1_7 = rs1_a1[6]


    rs1_a2_1 = rs1_a2[0]
    rs1_a2_2 = rs1_a2[1]
    rs1_a2_3 = rs1_a2[2]
    rs1_a2_4 = rs1_a2[3]
    rs1_a2_5 = rs1_a2[4]
    rs1_a2_6 = rs1_a2[5]
    rs1_a2_7 = rs1_a2[6]


    ##SERIE_2
    rs2_a1 = [21668.64, 21518.64, 21368.64, 21268.64, 21218.64, 21168.64, 21118.64]
    rs2_a2 = [26567.86, 26417.86, 26267.86, 26167.86, 26117.86, 26067.86, 26017.86]
    rs2_b1 = 18663.70
    rs2_b2 = 26829.07

    rs2_a1_1 = rs2_a1[0]
    rs2_a1_2 = rs2_a1[1]
    rs2_a1_3 = rs2_a1[2]
    rs2_a1_4 = rs2_a1[3]
    rs2_a1_5 = rs2_a1[4]
    rs2_a1_6 = rs2_a1[5]
    rs2_a1_7 = rs2_a1[6]


    rs2_a2_1 = rs2_a2[0]
    rs2_a2_2 = rs2_a2[1]
    rs2_a2_3 = rs2_a2[2]
    rs2_a2_4 = rs2_a2[3]
    rs2_a2_5 = rs2_a2[4]
    rs2_a2_6 = rs2_a2[5]
    rs2_a2_7 = rs2_a2[6]

    ##SERIE_3
    rs3_a1 =[19268.97, 19218.97, 18118.97, 17918.97, 17718.97]
    rs3_a2 = [19268.97, 19218.97, 18118.97, 17918.97, 17718.97]
    rs3_b1 = 11664.81
    rs3_b2 = 24496.11

    rs3_a1_1 = rs3_a1[0]
    rs3_a1_2 = rs3_a1[1]
    rs3_a1_3 = rs3_a1[2]
    rs3_a1_4 = rs3_a1[3]
    rs3_a1_5 = rs3_a1[4]

    rs3_a2_1 = rs3_a2[0]
    rs3_a2_2 = rs3_a2[1]
    rs3_a2_3 = rs3_a2[2]
    rs3_a2_4 = rs3_a2[3]
    rs3_a2_5 = rs3_a2[4]

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    # This is for main choices, each variable is one row in the choice table MPL
    rHL_1 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_2 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_3 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_4 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_5 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_6 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_7 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)


    r_s2_HL_1 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s2_HL_2 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s2_HL_3 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s2_HL_4 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s2_HL_5 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s2_HL_6 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s2_HL_7 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)


    r_s3_HL_1 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s3_HL_2 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s3_HL_3 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s3_HL_4 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s3_HL_5 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)

    # This is needed for the instructions
    rHL = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)



    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff_rHL(self):
        # *******************************************
        # select random row and random outcome
        # *******************************************
        self.participant.vars['rHL_series'] = random.randint(1, 3)
        #
        self.participant.vars['rHL_row'] = random.randint(1,7)
        self.participant.vars['rHL_row_3'] = random.randint(1,5)

        # select one row randomly for payment (from module random)
        self.participant.vars['rHL_random'] = random.randint(1, 7)
        self.participant.vars['rHL_random_3'] = random.randint(1, 5)

        # select the number x that defines the outcome of the lottery (if x<=p, outcome is left f1 or f3, otherwise f2 or f4)
        self.participant.vars['rHL_scenario'] = random.randint(1,100)
        # write it to participant.vars['HL_random']

        # *******************************************
        # select choices in correspondence to random row
        # *******************************************
        choices_rs1 = [self.rHL_1,
                      self.rHL_2,
                      self.rHL_3,
                      self.rHL_4,
                      self.rHL_5,
                      self.rHL_6,
                      self.rHL_7,
                      ]

        choices_rs2 = [self.r_s2_HL_1,
                      self.r_s2_HL_2,
                      self.r_s2_HL_3,
                      self.r_s2_HL_4,
                      self.r_s2_HL_5,
                      self.r_s2_HL_6,
                      self.r_s2_HL_7,
                      ]

        choices_rs3 = [self.r_s3_HL_1,
                      self.r_s3_HL_2,
                      self.r_s3_HL_3,
                      self.r_s3_HL_4,
                      self.r_s3_HL_5]

        # create a list with all choices of the player (see self)
        self.participant.vars['HL_choice_rs1'] = choices_rs1[self.participant.vars['rHL_row'] - 1]
        self.participant.vars['HL_choice_rs2'] = choices_rs2[self.participant.vars['rHL_row'] - 1]
        self.participant.vars['HL_choice_rs3'] = choices_rs3[self.participant.vars['rHL_row_3'] - 1]

        # select from the list the choice in correspondence to the randomly drawn row (notice the offset)
        # write it to participant.vars['HL_choice']

        # *******************************************
        # Compute here the payoffs
        # *******************************************
        if self.participant.vars['rHL_series'] == 1:
            if self.participant.vars['rHL_scenario'] <= 20:
                # if the random number is smaller equal than the random row
                if self.participant.vars['HL_choice_rs1'] == 1:  # A
                    # if the choice was A
                    self.participant.vars['rpayoff_HL'] = Constants.rs1_a1[self.participant.vars['rHL_row'] - 1]
                    # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rs1_b1
            else:
                # if the random number is larger than the random row
                if self.participant.vars['HL_choice_rs1'] == 1:  # A
                    # if the choice was A
                    self.participant.vars['rpayoff_HL'] = Constants.rs1_a2[self.participant.vars['rHL_row'] - 1]
                    # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rs1_b2

        elif self.participant.vars['rHL_series'] == 2:
            if self.participant.vars['rHL_scenario'] <= 20:
                # if the random number is smaller equal than the random row
                if self.participant.vars['HL_choice_rs2'] == 1:  # A
                    # if the choice was A
                    self.participant.vars['rpayoff_HL'] = Constants.rs2_a1[self.participant.vars['rHL_row'] - 1]
                    # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rs2_b1
            else:
                # if the random number is larger than the random row
                if self.participant.vars['HL_choice_rs2'] == 1:  # A
                    # if the choice was A
                    self.participant.vars['rpayoff_HL'] = Constants.rs2_a2[self.participant.vars['rHL_row'] - 1]
                    # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rs2_b2

        else:
            if self.participant.vars['rHL_scenario'] <= 10:
                # if the random number is smaller equal than the random row
                if self.participant.vars['HL_choice_rs3'] == 1:  # A
                    # if the choice was A
                    self.participant.vars['rpayoff_HL'] = Constants.rs3_a1[self.participant.vars['rHL_row_3'] - 1]
                    # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rs3_b1
            else:
                # if the random number is larger than the random row
                if self.participant.vars['HL_choice_rs3'] == 1:  # A
                    # if the choice was A
                    self.participant.vars['rpayoff_HL'] = Constants.rs3_a2[self.participant.vars['rHL_row_3'] - 1]
                    # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rs3_b2

        self.payoff = self.participant.vars['rpayoff_HL']
        # write the payoff to player.payoff