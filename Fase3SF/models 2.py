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
    name_in_url = 'Fase3SF'
    players_per_group = None
    num_rounds = 1
    # these are the lottery payoffs, f1 and f2 refer to lottery A and f3 and f4 to lottery B
    ist_s1  =[150,350,480,700,750,850,900]
    var1a = 0.225
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
    var5a = 0.5
    var6a = 0.05
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
class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):



    # This is for main choices, each variable is one row in the choice table MPL
    rHL_1 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    rHL_2 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    rHL_3 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    rHL_4 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    rHL_5 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    rHL_6 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    rHL_7 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)

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
    rHL = models.IntegerField(choices=[[1,'A'],[2,'B']],widget=widgets.RadioSelectHorizontal,initial=0)



    def vars_for_template(self):
        insvalue = self.participant.vars['insvalue']
        insprem = self.participant.vars['insprem']
        avginc = self.participant.vars['avginc']

        insvalueist = (insvalue * 0.005)
        insvaluedisc = (insvalue * 0.001)

        inspremist = (insprem * 0.04)
        inspremdisc = (insprem * 0.04)

        disctot = (insvaluedisc + inspremdisc)

        isttot_1 = (Constants.ist_s1[0] + inspremist + insvalueist)
        isttot_2 = (Constants.ist_s1[1] + inspremist + insvalueist)
        isttot_3 = (Constants.ist_s1[2] + inspremist + insvalueist)
        isttot_4 = (Constants.ist_s1[3] + inspremist + insvalueist)
        isttot_5 = (Constants.ist_s1[4] + inspremist + insvalueist)
        isttot_6 = (Constants.ist_s1[5] + inspremist + insvalueist)
        isttot_7 = (Constants.ist_s1[6] + inspremist + insvalueist)

        isttot_8 = (Constants.ist_s2[0] + inspremist + insvalueist)
        isttot_9 = (Constants.ist_s2[1] + inspremist + insvalueist)
        isttot_10 = (Constants.ist_s2[2] + inspremist + insvalueist)
        isttot_11 = (Constants.ist_s2[3] + inspremist + insvalueist)
        isttot_12 = (Constants.ist_s2[4] + inspremist + insvalueist)
        isttot_13 = (Constants.ist_s2[5] + inspremist + insvalueist)
        isttot_14 = (Constants.ist_s2[6] + inspremist + insvalueist)

        isttot_15 = (Constants.ist_s3[0] + inspremist + insvalueist)
        isttot_16 = (Constants.ist_s3[1] + inspremist + insvalueist)
        isttot_17 = (Constants.ist_s3[2] + inspremist + insvalueist)
        isttot_18 = (Constants.ist_s3[3] + inspremist + insvalueist)
        isttot_19 = (Constants.ist_s3[4] + inspremist + insvalueist)


        farmercost_1 = (isttot_1 - disctot)
        farmercost_2 = (isttot_2 - disctot)
        farmercost_3 = (isttot_3 - disctot)
        farmercost_4 = (isttot_4 - disctot)
        farmercost_5 = (isttot_5 - disctot)
        farmercost_6 = (isttot_6 - disctot)
        farmercost_7 = (isttot_7 - disctot)
        farmercost_8 = (isttot_8 - disctot)
        farmercost_9 = (isttot_9 - disctot)
        farmercost_10 = (isttot_10 - disctot)
        farmercost_11 = (isttot_11 - disctot)
        farmercost_12 = (isttot_12 - disctot)
        farmercost_13 = (isttot_13 - disctot)
        farmercost_14 = (isttot_14 - disctot)
        farmercost_15 = (isttot_15 - disctot)
        farmercost_16 = (isttot_16 - disctot)
        farmercost_17 = (isttot_17 - disctot)
        farmercost_18 = (isttot_18 - disctot)
        farmercost_19 = (isttot_19 - disctot)

        avginc = avginc

        ## SERIE 1
        inc_fut_1_rs1 = round((avginc - (Constants.var1a * avginc)), 2)
        self.participant.vars['inc_fut_1_rs1'] = inc_fut_1_rs1

        loss1 = round(inc_fut_1_rs1 - avginc, 2)

        inc_fut_ist_rs1_a1 = round(inc_fut_1_rs1 - farmercost_1 + ((0.7 * -loss1) ), 2)
        inc_fut_ist_rs1_a2 = round(inc_fut_1_rs1 - farmercost_2 + ((0.7 * -loss1) ), 2)
        inc_fut_ist_rs1_a3 = round(inc_fut_1_rs1 - farmercost_3 + ((0.7 * -loss1) ), 2)
        inc_fut_ist_rs1_a4 = round(inc_fut_1_rs1 - farmercost_4 + ((0.7 * -loss1) ), 2)
        inc_fut_ist_rs1_a5 = round(inc_fut_1_rs1 - farmercost_5 + ((0.7 * -loss1) ), 2)
        inc_fut_ist_rs1_a6 = round(inc_fut_1_rs1 - farmercost_6 + ((0.7 * -loss1) ), 2)
        inc_fut_ist_rs1_a7 = round(inc_fut_1_rs1 - farmercost_7 + ((0.7 * -loss1) ), 2)

        self.participant.vars['inc_fut_ist_1_rs1'] = [inc_fut_ist_rs1_a1,
                                                    inc_fut_ist_rs1_a2,
                                                    inc_fut_ist_rs1_a3,
                                                    inc_fut_ist_rs1_a4,
                                                    inc_fut_ist_rs1_a5,
                                                    inc_fut_ist_rs1_a6,
                                                    inc_fut_ist_rs1_a7,
                                                    ]

        inc_fut_2_rs1 = round((avginc + (Constants.var2 * avginc)), 2)
        self.participant.vars['inc_fut_2_rs1'] = inc_fut_2_rs1

        inc_fut_ist_rs1_b1 = round((inc_fut_2_rs1 - farmercost_1),2)
        inc_fut_ist_rs1_b2 = round((inc_fut_2_rs1 - farmercost_2),2)
        inc_fut_ist_rs1_b3 = round((inc_fut_2_rs1 - farmercost_3),2)
        inc_fut_ist_rs1_b4 = round((inc_fut_2_rs1 - farmercost_4),2)
        inc_fut_ist_rs1_b5 = round((inc_fut_2_rs1 - farmercost_5),2)
        inc_fut_ist_rs1_b6 = round((inc_fut_2_rs1 - farmercost_6),2)
        inc_fut_ist_rs1_b7 = round((inc_fut_2_rs1 - farmercost_7),2)

        self.participant.vars['inc_fut_ist_2_rs1'] = [inc_fut_ist_rs1_b1,
                                                  inc_fut_ist_rs1_b2,
                                                  inc_fut_ist_rs1_b3,
                                                  inc_fut_ist_rs1_b4,
                                                  inc_fut_ist_rs1_b5,
                                                  inc_fut_ist_rs1_b6,
                                                  inc_fut_ist_rs1_b7,
                                                  ]


        ## SERIE 2
        inc_fut_1_rs2 = round((avginc - (Constants.var3 * avginc)), 2)
        self.participant.vars['inc_fut_1_rs2'] = inc_fut_1_rs2

        loss2 = round(inc_fut_1_rs2 - avginc, 2)

        inc_fut_ist_rs2_a1 = round(inc_fut_1_rs2 - farmercost_8 + ((0.7 * -loss2)), 2)
        inc_fut_ist_rs2_a2 = round(inc_fut_1_rs2 - farmercost_9 + ((0.7 * -loss2)), 2)
        inc_fut_ist_rs2_a3 = round(inc_fut_1_rs2 - farmercost_10 + ((0.7 * -loss2)), 2)
        inc_fut_ist_rs2_a4 = round(inc_fut_1_rs2 - farmercost_11 + ((0.7 * -loss2)), 2)
        inc_fut_ist_rs2_a5 = round(inc_fut_1_rs2 - farmercost_12 + ((0.7 * -loss2)), 2)
        inc_fut_ist_rs2_a6 = round(inc_fut_1_rs2 - farmercost_13 + ((0.7 * -loss2)), 2)
        inc_fut_ist_rs2_a7 = round(inc_fut_1_rs2 - farmercost_14 + ((0.7 * -loss2)), 2)

        self.participant.vars['inc_fut_ist_1_rs2'] = [inc_fut_ist_rs2_a1,
                                                    inc_fut_ist_rs2_a2,
                                                    inc_fut_ist_rs2_a3,
                                                    inc_fut_ist_rs2_a4,
                                                    inc_fut_ist_rs2_a5,
                                                    inc_fut_ist_rs2_a6,
                                                    inc_fut_ist_rs2_a7,
                                                   ]
        inc_fut_2_rs2 = round((avginc + (Constants.var44 * avginc)), 2)
        self.participant.vars['inc_fut_2_rs2'] = inc_fut_2_rs2

        inc_fut_ist_rs2_b1 = round((inc_fut_2_rs2 - farmercost_8),2)
        inc_fut_ist_rs2_b2 = round((inc_fut_2_rs2 - farmercost_9),2)
        inc_fut_ist_rs2_b3 = round((inc_fut_2_rs2 - farmercost_10),2)
        inc_fut_ist_rs2_b4 = round((inc_fut_2_rs2 - farmercost_11),2)
        inc_fut_ist_rs2_b5 = round((inc_fut_2_rs2 - farmercost_12),2)
        inc_fut_ist_rs2_b6 = round((inc_fut_2_rs2 - farmercost_13),2)
        inc_fut_ist_rs2_b7 = round((inc_fut_2_rs2 - farmercost_14),2)


        self.participant.vars['inc_fut_ist_2_rs2'] = [inc_fut_ist_rs2_b1,
                                                  inc_fut_ist_rs2_b2,
                                                  inc_fut_ist_rs2_b3,
                                                  inc_fut_ist_rs2_b4,
                                                  inc_fut_ist_rs2_b5,
                                                  inc_fut_ist_rs2_b6,
                                                  inc_fut_ist_rs2_b7,]

        ## SERIE 3
        inc_fut_1_rs3 = round((avginc - (Constants.var5a * avginc)), 2)
        self.participant.vars['inc_fut_1_rs3'] = inc_fut_1_rs3

        loss3 = round(inc_fut_1_rs3 - avginc, 2)

        inc_fut_ist_rs3_a1 = round(inc_fut_1_rs3 - farmercost_15 + ((0.7 * -loss3)), 2)
        inc_fut_ist_rs3_a2 = round(inc_fut_1_rs3 - farmercost_16 + ((0.7 * -loss3)), 2)
        inc_fut_ist_rs3_a3 = round(inc_fut_1_rs3 - farmercost_17 + ((0.7 * -loss3)), 2)
        inc_fut_ist_rs3_a4 = round(inc_fut_1_rs3 - farmercost_18 + ((0.7 * -loss3)), 2)
        inc_fut_ist_rs3_a5 = round(inc_fut_1_rs3 - farmercost_19 + ((0.7 * -loss3)), 2)

        self.participant.vars['inc_fut_ist_1_rs3'] = [inc_fut_ist_rs3_a1,
                                                    inc_fut_ist_rs3_a2,
                                                    inc_fut_ist_rs3_a3,
                                                    inc_fut_ist_rs3_a4,
                                                    inc_fut_ist_rs3_a5]


        inc_fut_2_rs3 = round((avginc + (Constants.var6a * avginc)), 2)
        self.participant.vars['inc_fut_2_rs3'] = inc_fut_2_rs3

        loss4 = round(inc_fut_2_rs3 - avginc, 2)

        inc_fut_ist_rs3_b1 = round(inc_fut_2_rs3 - farmercost_15,2)
        inc_fut_ist_rs3_b2 = round(inc_fut_2_rs3 - farmercost_16,2)
        inc_fut_ist_rs3_b3 = round(inc_fut_2_rs3 - farmercost_17,2)
        inc_fut_ist_rs3_b4 = round(inc_fut_2_rs3 - farmercost_18,2)
        inc_fut_ist_rs3_b5 = round(inc_fut_2_rs3 - farmercost_19,2)


        self.participant.vars['inc_fut_ist_2_rs3'] = [inc_fut_ist_rs3_b1,
                                                  inc_fut_ist_rs3_b2,
                                                  inc_fut_ist_rs3_b3,
                                                  inc_fut_ist_rs3_b4,
                                                  inc_fut_ist_rs3_b5,
                                                  ]


    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff_rHL(self):
        # *******************************************
        # select random row and random outcome
        # *******************************************
        self.participant.vars['rHL_series'] = random.randint(1, 3)
        #
        self.participant.vars['rHL_row'] = random.randint(1, 7)
        self.participant.vars['rHL_row_3'] = random.randint(1, 5)

        # select one row randomly for payment (from module random)
        self.participant.vars['rHL_random'] = random.randint(1, 7)
        self.participant.vars['rHL_random_3'] = random.randint(1, 5)
        self.participant.vars['rHL_scenario'] = random.randint(1,100)

        #*******************************************
        # select choices in correspondence to random row
        #*******************************************
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

        #*******************************************
        # Compute here the payoffs
        #*******************************************
        if self.participant.vars['rHL_series'] == 1:
            if self.participant.vars['rHL_scenario'] <= 20:
            # if the random number is smaller equal than the random row
                if self.participant.vars['HL_choice_rs1'] == 1: #A
                # if the choice was A
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['inc_fut_ist_1_rs1'][self.participant.vars['rHL_row']-1]
                # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['inc_fut_1_rs1']
            else:
            # if the random number is slarger than the random row
                if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['inc_fut_ist_2_rs1'][self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['inc_fut_2_rs1']
        elif self.participant.vars['rHL_series'] == 2:
            if self.participant.vars['rHL_scenario'] <=20:
            # if the random number is smaller equal than the random row
                if self.participant.vars['HL_choice_rs2'] == 1: #A
                # if the choice was A
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['inc_fut_ist_1_rs2'][self.participant.vars['rHL_row']-1]
                # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['inc_fut_1_rs2']
            else:
            # if the random number is slarger than the random row
                if self.participant.vars['HL_choice_rs2'] == 1 :#A
                    # if the choice was A
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['inc_fut_ist_2_rs2'][self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['inc_fut_2_rs2']
        else:
            if self.participant.vars['rHL_scenario']  <= 10:
            # if the random number is smaller equal than the random row
                if self.participant.vars['HL_choice_rs3'] == 1: #A
                # if the choice was A
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['inc_fut_ist_1_rs3'][self.participant.vars['rHL_row_3']-1]
                # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['inc_fut_1_rs3']
            else:
            # if the random number is slarger than the random row
                if self.participant.vars['HL_choice_rs3'] == 1 :#A
                    # if the choice was A
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['inc_fut_ist_2_rs3'][self.participant.vars['rHL_row_3']-1]
                    # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['inc_fut_2_rs3']

        self.payoff = self.participant.vars['rpayoff_HL']
        # write the payoff to player.payoff

