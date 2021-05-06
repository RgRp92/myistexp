from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Page0(Page):


    def is_displayed(self):
        return self.round_number == 1

class IstruzioniPage1(Page):
    form_model = 'player'

class IstruzioniPage2(Page):
    form_model = 'player'

class IstruzioniPage3(Page):
    form_model = 'player'
    def vars_for_template(self):
        var1 = Constants.var1*100
        var2 = Constants.var2*100
        var3 = Constants.var3*100
        var4 = Constants.var4 * 100
        var5 = Constants.var5 * 100
        var6 = Constants.var6 * 100
        prb1 = Constants.prb1
        prb2 = Constants.prb2
        prb3 = Constants.prb3
        prb4 = Constants.prb4
        prb5 = Constants.prb5
        prb6 = Constants.prb6

        return {
            'var1': var1,
            'var2': var2,
            'var3': var3,
            'var4': var4,
            'var5': var5,
            'var6': var6,
            'prb1': prb1,
            'prb2': prb2,
            'prb3': prb3,
            'prb4': prb4,
            'prb5': prb5,
            'prb6': prb6,

        }

class IstruzioniPage4(Page):
    form_model = 'player'

class EsempioPage1(Page):
# which forms are needed from class player
    form_model = 'player'

    # values that are to be displayed (dictionary)
    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)

class MyWaitPage(Page):
    form_model = 'player'

class HL_Page1(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['rHL_1',
                   'rHL_2',
                   'rHL_3',
                   'rHL_4',
                   'rHL_5',
                   'rHL_6',
                   'rHL_7',
                   ] # all 10 options

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        prb1 = Constants.prb1
        prb2 = Constants.prb2
        return {
            'prb1': prb1,
            'prb2': prb2,
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'ist1': Constants.ist_s1[0],
            'ist2': Constants.ist_s1[1],
            'ist3': Constants.ist_s1[2],
            'ist4': Constants.ist_s1[3],
            'ist5': Constants.ist_s1[4],
            'ist6': Constants.ist_s1[5],
            'ist7': Constants.ist_s1[6],

            'rs1_a1_1': Constants.rs1_a1_1,
            'rs1_a1_2': Constants.rs1_a1_2,
            'rs1_a1_3': Constants.rs1_a1_3,
            'rs1_a1_4': Constants.rs1_a1_4,
            'rs1_a1_5': Constants.rs1_a1_5,
            'rs1_a1_6': Constants.rs1_a1_6,
            'rs1_a1_7': Constants.rs1_a1_7,

            'rs1_a2_1': Constants.rs1_a2_1,
            'rs1_a2_2': Constants.rs1_a2_2,
            'rs1_a2_3': Constants.rs1_a2_3,
            'rs1_a2_4': Constants.rs1_a2_4,
            'rs1_a2_5': Constants.rs1_a2_5,
            'rs1_a2_6': Constants.rs1_a2_6,
            'rs1_a2_7': Constants.rs1_a2_7,

            'rs1_b1': Constants.rs1_b1,
            'rs1_b2': Constants.rs1_b2,
            }
    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)


    def before_next_page(self):
    # built-in method
        self.player.set_payoff_rHL()  # see in models in Player class
        self.participant.vars['ra_value'] = Constants.rs1_a1[self.participant.vars['rHL_row'] - 1]
        self.participant.vars['raa_value'] = Constants.rs1_a2[self.participant.vars['rHL_row'] - 1]
        self.participant.vars['rb11_value'] = Constants.rs1_b1
        self.participant.vars['rb12_value'] = Constants.rs1_b2

class HL_Page2(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['r_s2_HL_1',
                   'r_s2_HL_2',
                   'r_s2_HL_3',
                   'r_s2_HL_4',
                   'r_s2_HL_5',
                   'r_s2_HL_6',
                   'r_s2_HL_7',
                   ] # all 10 options

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        prb1 = Constants.prb3
        prb2 = Constants.prb4
        return {
            'prb1': prb1,
            'prb2': prb2,
            'var3': var3,
            'var4': var4,
            'var33': var33,
            'var44': var44,
            'ist1': Constants.ist_s2[0],
            'ist2': Constants.ist_s2[1],
            'ist3': Constants.ist_s2[2],
            'ist4': Constants.ist_s2[3],
            'ist5': Constants.ist_s2[4],
            'ist6': Constants.ist_s2[5],
            'ist7': Constants.ist_s2[6],

            'rs2_a1_1': Constants.rs2_a1_1,
            'rs2_a1_2': Constants.rs2_a1_2,
            'rs2_a1_3': Constants.rs2_a1_3,
            'rs2_a1_4': Constants.rs2_a1_4,
            'rs2_a1_5': Constants.rs2_a1_5,
            'rs2_a1_6': Constants.rs2_a1_6,
            'rs2_a1_7': Constants.rs2_a1_7,

            'rs2_a2_1': Constants.rs2_a2_1,
            'rs2_a2_2': Constants.rs2_a2_2,
            'rs2_a2_3': Constants.rs2_a2_3,
            'rs2_a2_4': Constants.rs2_a2_4,
            'rs2_a2_5': Constants.rs2_a2_5,
            'rs2_a2_6': Constants.rs2_a2_6,
            'rs2_a2_7': Constants.rs2_a2_7,

            'rs2_b1': Constants.rs2_b1,
            'rs2_b2': Constants.rs2_b2,

        }

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    def before_next_page(self):
    # built-in method
        self.player.set_payoff_rHL()  # see in models in Player class
        self.participant.vars['ra_value'] = Constants.rs2_a1[self.participant.vars['rHL_row'] - 1]
        self.participant.vars['raa_value'] = Constants.rs2_a2[self.participant.vars['rHL_row'] - 1]
        self.participant.vars['rb11_value'] = Constants.rs2_b1
        self.participant.vars['rb12_value'] = Constants.rs2_b2

class HL_Page3(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['r_s3_HL_1',
                   'r_s3_HL_2',
                   'r_s3_HL_3',
                   'r_s3_HL_4',
                   'r_s3_HL_5']

    # values that are to be displayed (dictionary)


    def vars_for_template(self):
        var5 = Constants.var5 * 100
        var6 = Constants.var6 * 100
        var55 = Constants.var55 * 100
        var66 = Constants.var66 * 100
        prb1 = Constants.prb5
        prb2 = Constants.prb6
        return {
            'prb1': prb1,
            'prb2': prb2,
            'var5': var5,
            'var6': var6,
            'var55': var55,
            'var66': var66,
            'ist1': Constants.ist_s3[0],
            'ist2': Constants.ist_s3[1],
            'ist3': Constants.ist_s3[2],
            'ist4': Constants.ist_s3[3],
            'ist5': Constants.ist_s3[4],
            'rs3_a1_1': Constants.rs3_a1_1,
            'rs3_a1_2': Constants.rs3_a1_2,
            'rs3_a1_3': Constants.rs3_a1_3,
            'rs3_a1_4': Constants.rs3_a1_4,
            'rs3_a1_5': Constants.rs3_a1_5,
            'rs3_a2_1': Constants.rs3_a2_1,
            'rs3_a2_2': Constants.rs3_a2_2,
            'rs3_a2_3': Constants.rs3_a2_3,
            'rs3_a2_4': Constants.rs3_a2_4,
            'rs3_a2_5': Constants.rs3_a2_5,
            'rs3_b1': Constants.rs3_b1,
            'rs3_b2': Constants.rs3_b2,

        }

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    def before_next_page(self):
        # built-in method
        self.player.set_payoff_rHL()# see in models in Player class
        self.participant.vars['ra_value'] = Constants.rs3_a1[self.participant.vars['rHL_row_3'] - 1]
        self.participant.vars['raa_value'] = Constants.rs3_a2[self.participant.vars['rHL_row_3'] - 1]
        self.participant.vars['rb11_value'] = Constants.rs3_b1
        self.participant.vars['rb12_value'] = Constants.rs3_b2

class OutcomeHL(Page):
# values needed to inform subjects about the actual outcome
    def vars_for_template(self):
        if self.participant.vars["rHL_series"] == 1 :
            # retrieve values from participant.vars and store them in a dictionary
            return{
            'rHL_series':1,
            'rpayoff_HL': self.player.participant.vars['rpayoff_HL'],#payoff
            'rrow': self.player.participant.vars['rHL_row'], # randomly chosen row
            'rvalue': self.participant.vars['rHL_random'],# randomly chosen value to define outcome
            'rchoice': self.participant.vars['HL_choice_rs1'],# actual choice
            # outcomes of the selected row
            'ra_value': Constants.rs1_a1[self.participant.vars['rHL_row'] - 1],
            'raa_value': Constants.rs1_a2[self.participant.vars['rHL_row'] - 1],
            'rb11_value': Constants.rs1_b1,
            'rb12_value': Constants.rs1_b2,
            'rp_A_1': self.participant.vars['rHL_row'],
            'rp_A_2': 10-self.participant.vars['rHL_row'],
            'rp_B_1': self.participant.vars['rHL_row'],
            'rp_B_2': 10-self.participant.vars['rHL_row'],
            'ist_value': Constants.ist_s1[self.participant.vars['rHL_row'] - 1],
            'var1': -Constants.var1 * 100,
            'var2': +Constants.var2 * 100,
            'var11': -Constants.var11 * 100,
            'var22': +Constants.var22 * 100,
            'prb1': Constants.prb1,
            'prb2': Constants.prb2
            }
        elif self.participant.vars["rHL_series"] == 2 :
            # retrieve values from participant.vars and store them in a dictionary
            return{
            'rHL_series': 2,
            'rpayoff_HL': self.player.participant.vars['rpayoff_HL'],#payoff
            'rrow': self.player.participant.vars['rHL_row'], # randomly chosen row
            'rvalue': self.participant.vars['rHL_random'],# randomly chosen value to define outcome
            'rchoice': self.participant.vars['HL_choice_rs2'],# actual choice
            # outcomes of the selected row
            'ra_value': Constants.rs2_a1[self.participant.vars['rHL_row'] - 1],
            'raa_value': Constants.rs2_a2[self.participant.vars['rHL_row'] - 1],
            'rb11_value': Constants.rs2_b1,
            'rb12_value': Constants.rs2_b2,
            'rp_A_1': self.participant.vars['rHL_row'],
            'rp_A_2': 10-self.participant.vars['rHL_row'],
            'rp_B_1': self.participant.vars['rHL_row'],
            'rp_B_2': 10-self.participant.vars['rHL_row'],
            'ist_value':Constants.ist_s2[self.participant.vars['rHL_row'] - 1],
            'var1': -Constants.var3 * 100,
            'var2': +Constants.var4 * 100,
           'var11': -Constants.var33 * 100,
            'var22': +Constants.var44 * 100,
            'prb1': Constants.prb3,
            'prb2': Constants.prb4
            }
        else :
            # retrieve values from participant.vars and store them in a dictionary
            return{
            'rHL_series': 3,
            'rpayoff_HL': self.player.participant.vars['rpayoff_HL'],#payoff
            'rrow': self.player.participant.vars['rHL_row_3'], # randomly chosen row
            'rvalue': self.participant.vars['rHL_random_3'],# randomly chosen value to define outcome
            'rchoice': self.participant.vars['HL_choice_rs3'],# actual choice
            # outcomes of the selected row
            'ra_value': Constants.rs3_a1[self.participant.vars['rHL_row_3'] - 1],
            'raa_value': Constants.rs3_a2[self.participant.vars['rHL_row_3'] - 1],
            'rb11_value': Constants.rs3_b1,
            'rb12_value': Constants.rs3_b2,
            'rp_A_1': self.participant.vars['rHL_row_3'],
            'rp_A_2': 10-self.participant.vars['rHL_row_3'],
            'rp_B_1': self.participant.vars['rHL_row_3'],
            'rp_B_2': 10-self.participant.vars['rHL_row_3'],
            'ist_value':Constants.ist_s3[self.participant.vars['rHL_row_3'] - 1],
            'var1': -Constants.var5 * 100,
            'var2': -Constants.var6 * 100,
            'var11': -Constants.var55 * 100,
            'var22': -Constants.var66 * 100,
            'prb1': Constants.prb5,
            'prb2': Constants.prb6
            }

    def before_next_page(self):
        if self.participant.vars["rHL_series"] == 1 :
            self.participant.vars['rvar1'] = Constants.var1 * 100
            self.participant.vars['rvar2'] = Constants.var2 * 100
            self.participant.vars['rvar11'] = Constants.var11 * 100
            self.participant.vars['rvar22'] = Constants.var22 * 100
            self.participant.vars['prb1'] = Constants.prb1
            self.participant.vars['prb2'] = Constants.prb2
            self.participant.vars['rist_value'] = Constants.ist_s1[self.participant.vars['rHL_row'] - 1]
            self.participant.vars['rHL_series'] = 1
            self.participant.vars['rHL_choice'] =  self.participant.vars['HL_choice_rs1']
            self.participant.vars['ra_value'] = Constants.rs1_a1[self.participant.vars['rHL_row'] - 1]
            self.participant.vars['raa_value'] = Constants.rs1_a2[self.participant.vars['rHL_row'] - 1]
            self.participant.vars['rb11_value'] = Constants.rs1_b1
            self.participant.vars['rb12_value'] = Constants.rs1_b2
            self.participant.vars['rrow'] = [self.participant.vars['rHL_row'] - 1]

        elif self.participant.vars["rHL_series"] == 2 :
            self.participant.vars['rvar1'] = Constants.var3 * 100
            self.participant.vars['rvar2'] = Constants.var4 * 100
            self.participant.vars['rvar11'] = Constants.var33 * 100
            self.participant.vars['rvar22'] = Constants.var44 * 100
            self.participant.vars['prb1'] = Constants.prb3
            self.participant.vars['prb2'] = Constants.prb4
            self.participant.vars['rist_value'] = Constants.ist_s2[self.participant.vars['rHL_row'] - 1]
            self.participant.vars['rHL_series'] = 2
            self.participant.vars['rHL_choice'] =  self.participant.vars['HL_choice_rs2']
            self.participant.vars['ra_value'] = Constants.rs2_a1[self.participant.vars['rHL_row'] - 1]
            self.participant.vars['raa_value'] = Constants.rs2_a2[self.participant.vars['rHL_row'] - 1]
            self.participant.vars['rb11_value'] = Constants.rs2_b1
            self.participant.vars['rb12_value'] = Constants.rs2_b2
            self.participant.vars['rrow'] = [self.participant.vars['rHL_row'] - 1]

        else:
            self.participant.vars["rHL_series"] = 3
            self.participant.vars['rvar1'] = Constants.var5 * 100
            self.participant.vars['rvar2'] = Constants.var6 * 100
            self.participant.vars['rvar11'] = Constants.var55 * 100
            self.participant.vars['rvar22'] = Constants.var66 * 100
            self.participant.vars['prb1'] = Constants.prb5
            self.participant.vars['prb2'] = Constants.prb6
            self.participant.vars['rist_value'] = Constants.ist_s3[self.participant.vars['rHL_row_3'] - 1]
            self.participant.vars['rHL_choice'] =  self.participant.vars['HL_choice_rs3']
            self.participant.vars['ra_value'] = Constants.rs3_a1[self.participant.vars['rHL_row_3'] - 1]
            self.participant.vars['raa_value'] = Constants.rs3_a2[self.participant.vars['rHL_row_3'] - 1]
            self.participant.vars['rb11_value'] = Constants.rs3_b1
            self.participant.vars['rb12_value'] = Constants.rs3_b2
            self.participant.vars['rrow'] = [self.participant.vars['rHL_row_3'] - 1]


    def app_after_this_page(self, upcoming_apps):
            return 'Fase4'


# the coreography of pages
page_sequence = [
                    Page0,
                    IstruzioniPage1,
                    IstruzioniPage2,
                    IstruzioniPage4,
                    EsempioPage1,
                    MyWaitPage,
                    HL_Page1,
                    HL_Page2,
                    HL_Page3,
                    OutcomeHL
]
