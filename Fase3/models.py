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
    ist  =[500,450,400,350,300,250,200,150,100,80]
    var1 = 0.2
    var2 = 0.1
    var3 = 0.3
    var4 = 0.4
    var5 = 0.5
    var6 = 0.25
    prb1 = 70
    prb2 = 30
    prb3 = 40
    prb4 = 60
    prb5 = 60
    prb6 = 40
    rs1_a1 = [20417.75, 20467.75, 20517.75 , 20567.75 , 20617.75, 20667.75, 20717.75, 20767.75, 20817.75, 20837.75]
    rs1_a2 = [23997.15, 24047.15, 24097.15, 24147.15, 24197.15, 24347.15, 24297.15, 24347.15, 24397.15, 24417.15]
    rs1_b1 = 17896.99
    rs1_b2 = 24608.36

    rs1_a1_1 = rs1_a1[0]
    rs1_a1_2 = rs1_a1[1]
    rs1_a1_3 = rs1_a1[2]
    rs1_a1_4 = rs1_a1[3]
    rs1_a1_5 = rs1_a1[4]
    rs1_a1_6 = rs1_a1[5]
    rs1_a1_7 = rs1_a1[6]
    rs1_a1_8 = rs1_a1[7]
    rs1_a1_9 = rs1_a1[8]
    rs1_a1_10 = rs1_a1[9]

    rs1_a2_1 = rs1_a2[0]
    rs1_a2_2 = rs1_a2[1]
    rs1_a2_3 = rs1_a2[2]
    rs1_a2_4 = rs1_a2[3]
    rs1_a2_5 = rs1_a2[4]
    rs1_a2_6 = rs1_a2[5]
    rs1_a2_7 = rs1_a2[6]
    rs1_a2_8 = rs1_a2[7]
    rs1_a2_9 = rs1_a2[8]
    rs1_a2_10 = rs1_a2[9]

    ##SERIE_2
    rs2_a1 = [19746.62, 19796.62, 19846.62, 19896.62, 19946.62, 19996.62, 20046.62, 20096.62, 20146.62, 20166.62]
    rs2_a2 = [30708.52, 30758.52, 30808.52, 30858.52, 30908.52, 30958.52, 31008.52, 31058.52, 31108.52, 31128.52]
    rs2_b1 = 15659.87
    rs2_b2 = 31319.73

    rs2_a1_1 = rs2_a1[0]
    rs2_a1_2 = rs2_a1[1]
    rs2_a1_3 = rs2_a1[2]
    rs2_a1_4 = rs2_a1[3]
    rs2_a1_5 = rs2_a1[4]
    rs2_a1_6 = rs2_a1[5]
    rs2_a1_7 = rs2_a1[6]
    rs2_a1_8 = rs2_a1[7]
    rs2_a1_9 = rs2_a1[8]
    rs2_a1_10 = rs2_a1[9]

    rs2_a2_1 = rs2_a2[0]
    rs2_a2_2 = rs2_a2[1]
    rs2_a2_3 = rs2_a2[2]
    rs2_a2_4 = rs2_a2[3]
    rs2_a2_5 = rs2_a2[4]
    rs2_a2_6 = rs2_a2[5]
    rs2_a2_7 = rs2_a2[6]
    rs2_a2_8 = rs2_a2[7]
    rs2_a2_9 = rs2_a2[8]
    rs2_a2_10 = rs2_a2[9]

    ##SERIE_3
    rs3_a1 =[18404.34, 18454.34, 18504.34, 18554.34, 18604.34]
    rs3_a2 = [20082.18, 20132.18, 20182.18, 20232.18, 20282.18]
    rs3_b1 = 11185.62
    rs3_b2 = 16778.43

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
    rHL_8 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_9 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_10 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)

    r_s2_HL_1 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s2_HL_2 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s2_HL_3 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s2_HL_4 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s2_HL_5 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s2_HL_6 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s2_HL_7 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s2_HL_8 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s2_HL_9 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    r_s2_HL_10 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)

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
        self.participant.vars['rHL_row'] = random.randint(1, 10)
        self.participant.vars['rHL_row_3'] = random.randint(1, 5)

        # select one row randomly for payment (from module random)
        self.participant.vars['rHL_random'] = random.randint(1, 10)
        self.participant.vars['rHL_random_3'] = random.randint(1, 5)

        # select the number x that defines the outcome of the lottery (if x<=p, outcome is left f1 or f3, otherwise f2 or f4)
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
                      self.rHL_8,
                      self.rHL_9,
                      self.rHL_10]

        choices_rs2 = [self.r_s2_HL_1,
                      self.r_s2_HL_2,
                      self.r_s2_HL_3,
                      self.r_s2_HL_4,
                      self.r_s2_HL_5,
                      self.r_s2_HL_6,
                      self.r_s2_HL_7,
                      self.r_s2_HL_8,
                      self.r_s2_HL_9,
                      self.r_s2_HL_10]

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
            if self.participant.vars['rHL_random'] <= self.participant.vars['rHL_row']:
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
            if self.participant.vars['rHL_random'] <= self.participant.vars['rHL_row']:
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
            if self.participant.vars['rHL_random_3'] <= self.participant.vars['rHL_row_3']:
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