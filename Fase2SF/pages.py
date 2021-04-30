from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Page0(Page):
    def is_displayed(self):
        return self.round_number == 1

class ISTPage1(Page):
    form_model = 'player'

class ISTPage2(Page):
    form_model = 'player'

class ISTPage3(Page):
    form_model = 'player'

    def vars_for_template(self):
        applearea = self.participant.vars['applearea']
        appleareaist = self.participant.vars['appleareaist']

        insvalue = self.participant.vars['insvalue']
        insvalueist = round((insvalue * 0.005),2)
        insvaluedisc = round((insvalue * 0.001),2)

        insprem = self.participant.vars['insprem']
        inspremist = round((insprem * 0.04),2)
        inspremdisc = round((insprem * 0.04),2)

        istct = (150 + inspremist + insvalueist)

        disctot = round((insvaluedisc + inspremdisc),2)

        farmercost = round((istct - disctot),2)

        eutot = round(((istct *70)/30),2)

        totfin = (istct + eutot)
        totfin = round(totfin,2)

        return{
            'applearea': applearea,
            'appleareaist': appleareaist,
            'insvalue': insvalue,
            'insvalueist': insvalueist,
            'insprem': insprem,
            'inspremist': inspremist,
            'inspremdisc':inspremdisc,
            'insvaluedisc':insvaluedisc,
            'istct':istct,
            'disctot': disctot,
            'farmercost':farmercost,
            'eutot' : eutot,
            'totfin': totfin,

        }

class ISTPage4(Page):
    form_model = 'player'

    def vars_for_template(self):
        insvalue = self.participant.vars['insvalue']
        insvalueist = (insvalue * 0.005)
        insvaluedisc = (insvalue * 0.001)

        insprem = self.participant.vars['insprem']
        inspremist = (insprem * 0.04)
        inspremdisc = (insprem * 0.04)

        istct = (inspremist + insvalueist + 150)

        disctot = (insvaluedisc + inspremdisc)

        farmercost = (istct - disctot)

        eutot = round(((istct * 70) / 30), 2)

        totfin = (istct + eutot)

        avginc = self.participant.vars['avginc']
        red = 40
        inc_fut = round(avginc - ((red/100)*avginc),2)
        loss = round(inc_fut - avginc,2)

        ind = round(-(70*loss)/100,2)
        fin_inc = round(inc_fut - farmercost + ind,2)

        return {

            'insvalue': insvalue,
            'insvalueist': insvalueist,
            'insprem': insprem,
            'inspremist': inspremist,
            'inspremdisc': inspremdisc,
            'insvaluedisc': insvaluedisc,
            'istct': istct,
            'disctot': disctot,
            'farmercost': farmercost,
            'eutot': eutot,
            'totfin': totfin,
            'avginc':avginc,
            'red':red,
            'inc_fut':inc_fut,
            'loss': loss,
            'ind': ind,
            'fin_inc': fin_inc

        }

class IstruzioniPage1(Page):
    form_model = 'player'

class IstruzioniPage2(Page):
    form_model = 'player'

    def vars_for_template(self):
        var1 = Constants.var1*100
        var2 = Constants.var2*100
        var3 = Constants.var3*100
        var4 = Constants.var4 * 100
        var5 = Constants.var5 * 100
        var6 = Constants.var6 * 100
        return {
            'var1': var1,
            'var2': var2,
            'var3': var3,
            'var4': var4,
            'var5': var5,
            'var6': var6
        }

class IstruzioniPage3(Page):
    form_model = 'player'

class IstruzioniPage4(Page):
    form_model = 'player'

class IstruzioniPage5(Page):
# which forms are needed from class player
    form_model = 'player'

class EsempioPage1(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'a4': Constants.s1_a1_4,
            'aa4': Constants.s1_a2_4,
        }

class EsempioPage2(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'b11': Constants.s1_b1,
            'b12': Constants.s1_b2,
        }

class EsempioPage3(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'b11': Constants.s1_b1,
            'b12': Constants.s1_b2,
        }

class EsempioPage4(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'b11': Constants.s1_b1,
            'b12': Constants.s1_b2,
        }

class EsempioPage5(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'b11': Constants.s1_b1,
            'b12': Constants.s1_b2,
        }

class Esperti(Page):
    form_model = 'player'

class MyWaitPage(Page):
    form_model = 'player'
    def vars_for_template(self):
        self.player.vars_for_template()
        rate = round(25000/self.participant.vars['inc_fut_2_s2'],2)
        return {'rate':rate}

    def before_next_page(self):
        self.participant.vars['rate'] = round(25000/self.participant.vars['inc_fut_2_s2'],2)

class HL_Page1(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['HL_1',
                   'HL_2',
                   'HL_3',
                   'HL_4',
                   'HL_5',
                   'HL_6',
                   'HL_7',
                   ] # all 10 options

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        self.player.vars_for_template()
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        return {
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

            's1_a1_1': self.participant.vars['inc_fut_ist_1_s1'][0],
            's1_a1_2': self.participant.vars['inc_fut_ist_1_s1'][1],
            's1_a1_3': self.participant.vars['inc_fut_ist_1_s1'][2],
            's1_a1_4': self.participant.vars['inc_fut_ist_1_s1'][3],
            's1_a1_5': self.participant.vars['inc_fut_ist_1_s1'][4],
            's1_a1_6': self.participant.vars['inc_fut_ist_1_s1'][5],
            's1_a1_7': self.participant.vars['inc_fut_ist_1_s1'][6],

            's1_a2_1': self.participant.vars['inc_fut_ist_2_s1'][0],
            's1_a2_2': self.participant.vars['inc_fut_ist_2_s1'][1],
            's1_a2_3': self.participant.vars['inc_fut_ist_2_s1'][2],
            's1_a2_4': self.participant.vars['inc_fut_ist_2_s1'][3],
            's1_a2_5': self.participant.vars['inc_fut_ist_2_s1'][4],
            's1_a2_6': self.participant.vars['inc_fut_ist_2_s1'][5],
            's1_a2_7': self.participant.vars['inc_fut_ist_2_s1'][6],

            's1_b1': self.participant.vars['inc_fut_1_s1'],
            's1_b2': self.participant.vars['inc_fut_2_s1'],
        }

    def before_next_page(self):
        self.player.set_payoff_HL()  # see in models in Player class
        self.participant.vars['a_value'] = self.participant.vars['inc_fut_ist_1_s1'][self.participant.vars['HL_row'] - 1]
        self.participant.vars['aa_value'] = self.participant.vars['inc_fut_ist_2_s1'][self.participant.vars['HL_row'] - 1]
        self.participant.vars['b11_value'] = self.participant.vars['inc_fut_1_s1']
        self.participant.vars['b12_value'] = self.participant.vars['inc_fut_2_s1']

class HL_Page2(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['s2_HL_1',
                   's2_HL_2',
                   's2_HL_3',
                   's2_HL_4',
                   's2_HL_5',
                   's2_HL_6',
                   's2_HL_7',
                   ] # all 10 options

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        self.player.vars_for_template()
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        return {
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

            's2_a1_1': self.participant.vars['inc_fut_ist_1_s2'][0],
            's2_a1_2': self.participant.vars['inc_fut_ist_1_s2'][1],
            's2_a1_3': self.participant.vars['inc_fut_ist_1_s2'][2],
            's2_a1_4': self.participant.vars['inc_fut_ist_1_s2'][3],
            's2_a1_5': self.participant.vars['inc_fut_ist_1_s2'][4],
            's2_a1_6': self.participant.vars['inc_fut_ist_1_s2'][5],
            's2_a1_7': self.participant.vars['inc_fut_ist_1_s2'][6],

            's2_a2_1': self.participant.vars['inc_fut_ist_2_s2'][0],
            's2_a2_2': self.participant.vars['inc_fut_ist_2_s2'][1],
            's2_a2_3': self.participant.vars['inc_fut_ist_2_s2'][2],
            's2_a2_4': self.participant.vars['inc_fut_ist_2_s2'][3],
            's2_a2_5': self.participant.vars['inc_fut_ist_2_s2'][4],
            's2_a2_6': self.participant.vars['inc_fut_ist_2_s2'][5],
            's2_a2_7': self.participant.vars['inc_fut_ist_2_s2'][6],

            's2_b1': self.participant.vars['inc_fut_1_s2'],
            's2_b2': self.participant.vars['inc_fut_2_s2'],
        }

    def before_next_page(self):
        self.player.set_payoff_HL()  # see in models in Player class
        self.participant.vars['a_value'] = self.participant.vars['inc_fut_ist_1_s2'][self.participant.vars['HL_row'] - 1]
        self.participant.vars['aa_value'] = self.participant.vars['inc_fut_ist_2_s2'][self.participant.vars['HL_row'] - 1]
        self.participant.vars['b11_value'] = self.participant.vars['inc_fut_1_s2']
        self.participant.vars['b12_value'] = self.participant.vars['inc_fut_2_s2']

class HL_Page3(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['s3_HL_1',
                   's3_HL_2',
                   's3_HL_3',
                   's3_HL_4',
                   's3_HL_5'] # all 10 options

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        self.player.vars_for_template()
        var5 = Constants.var5 * 100
        var6 = Constants.var6 * 100
        var55 = Constants.var55 * 100
        var66 = Constants.var66 * 100
        return {
            'var5': var5,
            'var6': var6,
            'var55': var55,
            'var66': var66,
            'ist1': Constants.ist_s3[0],
            'ist2': Constants.ist_s3[1],
            'ist3': Constants.ist_s3[2],
            'ist4': Constants.ist_s3[3],
            'ist5': Constants.ist_s3[4],
            's3_a1_1': self.participant.vars['inc_fut_ist_1_s3'][0],
            's3_a1_2': self.participant.vars['inc_fut_ist_1_s3'][1],
            's3_a1_3': self.participant.vars['inc_fut_ist_1_s3'][2],
            's3_a1_4': self.participant.vars['inc_fut_ist_1_s3'][3],
            's3_a1_5': self.participant.vars['inc_fut_ist_1_s3'][4],
            's3_a2_1': self.participant.vars['inc_fut_ist_2_s3'][0],
            's3_a2_2': self.participant.vars['inc_fut_ist_2_s3'][1],
            's3_a2_3': self.participant.vars['inc_fut_ist_2_s3'][2],
            's3_a2_4': self.participant.vars['inc_fut_ist_2_s3'][3],
            's3_a2_5': self.participant.vars['inc_fut_ist_2_s3'][4],
            's3_b1': self.participant.vars['inc_fut_1_s3'],
            's3_b2': self.participant.vars['inc_fut_2_s3'],
        }

    def before_next_page(self):
        self.player.set_payoff_HL()  # see in models in Player class
        self.participant.vars['a_value'] = self.participant.vars['inc_fut_ist_1_s3'][self.participant.vars['HL_row_3'] - 1]
        self.participant.vars['aa_value'] = self.participant.vars['inc_fut_ist_2_s3'][self.participant.vars['HL_row_3'] - 1]
        self.participant.vars['b11_value'] = self.participant.vars['inc_fut_1_s3']
        self.participant.vars['b12_value'] = self.participant.vars['inc_fut_2_s3']

class OutcomeHL(Page):
# values needed to inform subjects about the actual outcome
    def vars_for_template(self):
        if self.participant.vars["HL_series"] == 1 :
            # retrieve values from participant.vars and store them in a dictionary
            return{
            'HL_series':1,
            'payoff_HL': self.player.participant.vars['payoff_HL'],#payoff
            'row': self.player.participant.vars['HL_row'], # randomly chosen row
            'value': self.participant.vars['HL_random'],# randomly chosen value to define outcome
            'choice': self.participant.vars['HL_choice_s1'],# actual choice
            # outcomes of the selected row
            'a_value': self.participant.vars['inc_fut_ist_1_s1'][self.participant.vars['HL_row'] - 1],
            'aa_value': self.participant.vars['inc_fut_ist_2_s1'][self.participant.vars['HL_row'] - 1],
            'b11_value': self.participant.vars['inc_fut_1_s1'],
            'b12_value': self.participant.vars['inc_fut_2_s1'],
            'p_A_1': self.participant.vars['HL_row'],
            'p_A_2': 10-self.participant.vars['HL_row'],
            'p_B_1': self.participant.vars['HL_row'],
            'p_B_2': 10-self.participant.vars['HL_row'],
            'ist_value':Constants.ist_s1[self.participant.vars['HL_row'] - 1],
            'var1': -Constants.var1 * 100,
            'var2': +Constants.var2 * 100,
            'var11': -Constants.var11 * 100,
            'var22': +Constants.var22 * 100
            }
        elif self.participant.vars["HL_series"] == 2 :
            # retrieve values from participant.vars and store them in a dictionary
            return{
            'HL_series': 2,
            'payoff_HL': self.player.participant.vars['payoff_HL'],#payoff
            'row': self.player.participant.vars['HL_row'], # randomly chosen row
            'value': self.participant.vars['HL_random'],# randomly chosen value to define outcome
            'choice': self.participant.vars['HL_choice_s2'],# actual choice
            # outcomes of the selected row
            'a_value': self.participant.vars['inc_fut_ist_1_s2'][self.participant.vars['HL_row'] - 1],
            'aa_value': self.participant.vars['inc_fut_ist_2_s2'][self.participant.vars['HL_row'] - 1],
            'b11_value': self.participant.vars['inc_fut_1_s2'],
            'b12_value': self.participant.vars['inc_fut_2_s2'],
            'p_A_1': self.participant.vars['HL_row'],
            'p_A_2': 10-self.participant.vars['HL_row'],
            'p_B_1': self.participant.vars['HL_row'],
            'p_B_2': 10-self.participant.vars['HL_row'],
            'ist_value':Constants.ist_s2[self.participant.vars['HL_row'] - 1],
            'var1': -Constants.var3 * 100,
            'var2': +Constants.var4 * 100,
            'var11': -Constants.var33 * 100,
            'var22': +Constants.var44 * 100
            }
        else :
            # retrieve values from participant.vars and store them in a dictionary
            return{
            'HL_series': 3,
            'payoff_HL': self.player.participant.vars['payoff_HL'],#payoff
            'row': self.player.participant.vars['HL_row_3'], # randomly chosen row
            'value': self.participant.vars['HL_random_3'],# randomly chosen value to define outcome
            'choice': self.participant.vars['HL_choice_s3'],# actual choice
            # outcomes of the selected row
            'a_value': self.participant.vars['inc_fut_ist_1_s3'][self.participant.vars['HL_row_3'] - 1],
            'aa_value': self.participant.vars['inc_fut_ist_2_s3'][self.participant.vars['HL_row_3'] - 1],
            'b11_value': self.participant.vars['inc_fut_1_s3'],
            'b12_value': self.participant.vars['inc_fut_2_s3'],
            'p_A_1': self.participant.vars['HL_row_3'],
            'p_A_2': 10-self.participant.vars['HL_row_3'],
            'p_B_1': self.participant.vars['HL_row_3'],
            'p_B_2': 10-self.participant.vars['HL_row_3'],
            'ist_value':Constants.ist_s3[self.participant.vars['HL_row_3'] - 1],
            'var1': -Constants.var5 * 100,
            'var2': Constants.var6 * 100,
            'var11': -Constants.var55 * 100,
            'var22': Constants.var66 * 100
            }

    def before_next_page(self):
        if self.participant.vars["HL_series"] == 1 :
            self.participant.vars['var1'] = Constants.var1 *100
            self.participant.vars['var2'] = Constants.var2 *100
            self.participant.vars['ist_value'] = Constants.ist_s1[self.participant.vars['HL_row'] - 1]
            self.participant.vars['HL_series'] = 1
            self.participant.vars['HL_choice'] =  self.participant.vars['HL_choice_s1']
            self.participant.vars['a_value'] = self.participant.vars['inc_fut_ist_1_s1'][self.participant.vars['HL_row'] - 1]
            self.participant.vars['aa_value'] = self.participant.vars['inc_fut_ist_2_s1'][self.participant.vars['HL_row'] - 1]
            self.participant.vars['b11_value'] = self.participant.vars['inc_fut_1_s1']
            self.participant.vars['b12_value'] = self.participant.vars['inc_fut_2_s1']

        elif self.participant.vars["HL_series"] == 2 :
            self.participant.vars['var1'] = Constants.var3 * 100
            self.participant.vars['var2'] = Constants.var4 * 100
            self.participant.vars['var11'] = Constants.var33 * 100
            self.participant.vars['var22'] = Constants.var44 * 100
            self.participant.vars['ist_value'] = Constants.ist_s2[self.participant.vars['HL_row'] - 1]
            self.participant.vars['HL_series'] = 2
            self.participant.vars['HL_choice'] =  self.participant.vars['HL_choice_s2']
            self.participant.vars['a_value'] = self.participant.vars['inc_fut_ist_1_s2'][self.participant.vars['HL_row'] - 1]
            self.participant.vars['aa_value'] = self.participant.vars['inc_fut_ist_2_s2'][self.participant.vars['HL_row'] - 1]
            self.participant.vars['b11_value'] = self.participant.vars['inc_fut_1_s2']
            self.participant.vars['b12_value'] = self.participant.vars['inc_fut_2_s2']

        else:
            self.participant.vars['var1'] = Constants.var5 * 100
            self.participant.vars['var2'] = Constants.var6 * 100
            self.participant.vars['var11'] = Constants.var55 * 100
            self.participant.vars['var22'] = Constants.var66 * 100
            self.participant.vars['ist_value'] = Constants.ist_s3[self.participant.vars['HL_row_3'] - 1]
            self.participant.vars['HL_series'] = 3
            self.participant.vars['HL_choice'] =  self.participant.vars['HL_choice_s3']
            self.participant.vars['a_value'] = self.participant.vars['inc_fut_ist_1_s3'][self.participant.vars['HL_row_3'] - 1]
            self.participant.vars['aa_value'] = self.participant.vars['inc_fut_ist_2_s3'][self.participant.vars['HL_row_3'] - 1],
            self.participant.vars['b11_value'] = self.participant.vars['inc_fut_1_s3']
            self.participant.vars['b12_value'] = self.participant.vars['inc_fut_2_s3']


# the coreography of pages
page_sequence = [
    Page0,
    ISTPage1,
    ISTPage2,
    ISTPage3,
    ISTPage4,
    IstruzioniPage1,
    IstruzioniPage3,
    IstruzioniPage4,
    IstruzioniPage5,
    EsempioPage1,
    EsempioPage2,
    EsempioPage3,
    EsempioPage4,
    EsempioPage5,
    Esperti,
    MyWaitPage,
    HL_Page1,
    HL_Page2,
    HL_Page3,
    OutcomeHL,
]
