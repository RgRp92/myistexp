from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
class TitlePage(Page):

    def is_displayed(self):
        return self.round_number == 1

class Instructions(Page):
    form_model = 'player'

class Instructions1(Page):
    form_model = 'player'

class Instructions2(Page):
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

class ISTMELE(Page):
    form_model = 'player'

class ISTMELE2(Page):
    form_model = 'player'

class ISTMELE3(Page):
    form_model = 'player'

class ISTMELE4(Page):
    form_model = 'player'

class Payment(Page):
    form_model = 'player'
class Payment2(Page):
    form_model = 'player'

class PageHLExample(Page):
# which forms are needed from class player
    form_model = 'player'

    # values that are to be displayed (dictionary)
    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)

class PageHLExample1(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'a4': Constants.s1_a1_4,
            'aa4': Constants.s1_a2_4,
        }

class PageHLExample2(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'b11': Constants.s1_b1,
            'b12': Constants.s1_b2,
        }
class PageHLExample3(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'b11': Constants.s1_b1,
            'b12': Constants.s1_b2,
        }
class PageHLExample3a(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'b11': Constants.s1_b1,
            'b12': Constants.s1_b2,
        }
class PageHLExample3b(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'b11': Constants.s1_b1,
            'b12': Constants.s1_b2,
        }

class Instructions3(Page):
    form_model = 'player'

class MyWaitPage(Page):
    form_model = 'player'

class PageHL(Page):
    # which forms are needed from class player
    form_model = 'player'
    form_fields = ['HL_1', 'HL_2', 'HL_3', 'HL_4', 'HL_5', 'HL_6', 'HL_7', 'HL_8', 'HL_9', 'HL_10'] # all 10 options

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var2 = Constants.var2 * 100
        return {
            'var1': var1,
            'var2': var2,
            'ist1': Constants.ist[0],
            'ist2': Constants.ist[1],
            'ist3': Constants.ist[2],
            'ist4': Constants.ist[3],
            'ist5': Constants.ist[4],
            'ist6': Constants.ist[5],
            'ist7': Constants.ist[6],
            'ist8': Constants.ist[7],
            'ist9': Constants.ist[8],
            'ist10': Constants.ist[9],
            's1_a1_1': Constants.s1_a1_1,
            's1_a1_2': Constants.s1_a1_2,
            's1_a1_3': Constants.s1_a1_3,
            's1_a1_4': Constants.s1_a1_4,
            's1_a1_5': Constants.s1_a1_5,
            's1_a1_6': Constants.s1_a1_6,
            's1_a1_7': Constants.s1_a1_7,
            's1_a1_8': Constants.s1_a1_8,
            's1_a1_9': Constants.s1_a1_9,
            's1_a1_10': Constants.s1_a1_10,
            's1_a2_1': Constants.s1_a2_1,
            's1_a2_2': Constants.s1_a2_2,
            's1_a2_3': Constants.s1_a2_3,
            's1_a2_4': Constants.s1_a2_4,
            's1_a2_5': Constants.s1_a2_5,
            's1_a2_6': Constants.s1_a2_6,
            's1_a2_7': Constants.s1_a2_7,
            's1_a2_8': Constants.s1_a2_8,
            's1_a2_9': Constants.s1_a2_9,
            's1_a2_10': Constants.s1_a2_10,
            's1_b1': Constants.s1_b1,
            's1_b2': Constants.s1_b2,

        }

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    def before_next_page(self):
        # built-in method
        self.player.set_payoff_HL()# see in models in Player class
        self.participant.vars['a_value'] = Constants.s1_a1[self.participant.vars['HL_row'] - 1]
        self.participant.vars['aa_value'] = Constants.s1_a2[self.participant.vars['HL_row'] - 1]
        self.participant.vars['b11_value'] = Constants.s1_b1
        self.participant.vars['b12_value'] = Constants.s1_b2

class PageHL_2(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['s2_HL_1',
                   's2_HL_2',
                   's2_HL_3',
                   's2_HL_4',
                   's2_HL_5',
                   's2_HL_6',
                   's2_HL_7',
                   's2_HL_8',
                   's2_HL_9',
                   's2_HL_10'] # all 10 options

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        var3 = Constants.var3 * 100
        var4 = Constants.var4 * 100
        return {
            'var3': var3,
            'var4': var4,
            'ist1': Constants.ist[0],
            'ist2': Constants.ist[1],
            'ist3': Constants.ist[2],
            'ist4': Constants.ist[3],
            'ist5': Constants.ist[4],
            'ist6': Constants.ist[5],
            'ist7': Constants.ist[6],
            'ist8': Constants.ist[7],
            'ist9': Constants.ist[8],
            'ist10': Constants.ist[9],
            's2_a1_1': Constants.s2_a1_1,
            's2_a1_2': Constants.s2_a1_2,
            's2_a1_3': Constants.s2_a1_3,
            's2_a1_4': Constants.s2_a1_4,
            's2_a1_5': Constants.s2_a1_5,
            's2_a1_6': Constants.s2_a1_6,
            's2_a1_7': Constants.s2_a1_7,
            's2_a1_8': Constants.s2_a1_8,
            's2_a1_9': Constants.s2_a1_9,
            's2_a1_10': Constants.s2_a1_10,
            's2_a2_1': Constants.s2_a2_1,
            's2_a2_2': Constants.s2_a2_2,
            's2_a2_3': Constants.s2_a2_3,
            's2_a2_4': Constants.s2_a2_4,
            's2_a2_5': Constants.s2_a2_5,
            's2_a2_6': Constants.s2_a2_6,
            's2_a2_7': Constants.s2_a2_7,
            's2_a2_8': Constants.s2_a2_8,
            's2_a2_9': Constants.s2_a2_9,
            's2_a2_10': Constants.s2_a2_10,
            's2_b1': Constants.s2_b1,
            's2_b2': Constants.s2_b2,

        }

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    def before_next_page(self):
        # built-in method
        self.player.set_payoff_HL()# see in models in Player class
        self.participant.vars['a_value'] = Constants.s2_a1[self.participant.vars['HL_row'] - 1]
        self.participant.vars['aa_value'] = Constants.s2_a2[self.participant.vars['HL_row'] - 1]
        self.participant.vars['b11_value'] = Constants.s2_b1
        self.participant.vars['b12_value'] = Constants.s2_b2

class PageHL_3(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['s3_HL_1',
                   's3_HL_2',
                   's3_HL_3',
                   's3_HL_4',
                   's3_HL_5']

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        var5 = Constants.var5 * 100
        var6 = Constants.var6 * 100
        return {
            'var6': var5,
            'var5': var6,
            'ist1': Constants.ist[0],
            'ist2': Constants.ist[1],
            'ist3': Constants.ist[2],
            'ist4': Constants.ist[3],
            'ist5': Constants.ist[4],
            's3_a1_1': Constants.s3_a1_1,
            's3_a1_2': Constants.s3_a1_2,
            's3_a1_3': Constants.s3_a1_3,
            's3_a1_4': Constants.s3_a1_4,
            's3_a1_5': Constants.s3_a1_5,
            's3_a2_1': Constants.s3_a2_1,
            's3_a2_2': Constants.s3_a2_2,
            's3_a2_3': Constants.s3_a2_3,
            's3_a2_4': Constants.s3_a2_4,
            's3_a2_5': Constants.s3_a2_5,
            's3_b1': Constants.s3_b1,
            's3_b2': Constants.s3_b2,

        }

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    def before_next_page(self):
        # built-in method
        self.player.set_payoff_HL()# see in models in Player class
        self.participant.vars['a_value'] = Constants.s3_a1[self.participant.vars['HL_row_3'] - 1]
        self.participant.vars['aa_value'] = Constants.s3_a2[self.participant.vars['HL_row_3'] - 1]
        self.participant.vars['b11_value'] = Constants.s3_b1
        self.participant.vars['b12_value'] = Constants.s3_b2

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
            'a_value': Constants.s1_a1[self.participant.vars['HL_row'] - 1],
            'aa_value': Constants.s1_a2[self.participant.vars['HL_row'] - 1],
            'b11_value': Constants.s1_b1,
            'b12_value': Constants.s1_b2,
            'p_A_1': self.participant.vars['HL_row'],
            'p_A_2': 10-self.participant.vars['HL_row'],
            'p_B_1': self.participant.vars['HL_row'],
            'p_B_2': 10-self.participant.vars['HL_row'],
            'ist_value':Constants.ist[self.participant.vars['HL_row'] - 1],
            'var1': -Constants.var1 * 100,
            'var2': +Constants.var2 * 100
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
            'a_value': Constants.s2_a1[self.participant.vars['HL_row'] - 1],
            'aa_value': Constants.s2_a2[self.participant.vars['HL_row'] - 1],
            'b11_value': Constants.s2_b1,
            'b12_value': Constants.s2_b2,
            'p_A_1': self.participant.vars['HL_row'],
            'p_A_2': 10-self.participant.vars['HL_row'],
            'p_B_1': self.participant.vars['HL_row'],
            'p_B_2': 10-self.participant.vars['HL_row'],
            'ist_value':Constants.ist[self.participant.vars['HL_row'] - 1],
            'var1': -Constants.var3 * 100,
            'var2': +Constants.var4 * 100
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
            'a_value': Constants.s3_a1[self.participant.vars['HL_row_3'] - 1],
            'aa_value': Constants.s3_a2[self.participant.vars['HL_row_3'] - 1],
            'b11_value': Constants.s3_b1,
            'b12_value': Constants.s3_b2,
            'p_A_1': self.participant.vars['HL_row_3'],
            'p_A_2': 10-self.participant.vars['HL_row_3'],
            'p_B_1': self.participant.vars['HL_row_3'],
            'p_B_2': 10-self.participant.vars['HL_row_3'],
            'ist_value':Constants.ist[self.participant.vars['HL_row_3'] - 1],
            'var1': -Constants.var5 * 100,
            'var2': -Constants.var6 * 100
            }

    def before_next_page(self):
        if self.participant.vars["HL_series"] == 1 :
            self.participant.vars['var1'] = Constants.var1 *100
            self.participant.vars['var2'] = Constants.var2 *100
            self.participant.vars['ist_value'] = Constants.ist[self.participant.vars['HL_row'] - 1]
            self.participant.vars['HL_series'] = 1
            self.participant.vars['HL_choice'] =  self.participant.vars['HL_choice_s1']
            self.participant.vars['a_value'] = Constants.s1_a1[self.participant.vars['HL_row'] - 1]
            self.participant.vars['aa_value'] = Constants.s1_a2[self.participant.vars['HL_row'] - 1]
            self.participant.vars['b11_value'] = Constants.s1_b1
            self.participant.vars['b12_value'] = Constants.s1_b2

        elif self.participant.vars["HL_series"] == 2 :
            self.participant.vars['var1'] = Constants.var3 * 100
            self.participant.vars['var2'] = Constants.var4 * 100
            self.participant.vars['ist_value'] = Constants.ist[self.participant.vars['HL_row'] - 1]
            self.participant.vars['HL_series'] = 2
            self.participant.vars['HL_choice'] =  self.participant.vars['HL_choice_s2']
            self.participant.vars['a_value'] = Constants.s2_a1[self.participant.vars['HL_row'] - 1]
            self.participant.vars['aa_value'] = Constants.s2_a2[self.participant.vars['HL_row'] - 1]
            self.participant.vars['b11_value'] = Constants.s2_b1
            self.participant.vars['b12_value'] = Constants.s2_b2
        else:
            self.participant.vars['var1'] = Constants.var5 * 100
            self.participant.vars['var2'] = Constants.var6 * 100
            self.participant.vars['ist_value'] = Constants.ist[self.participant.vars['HL_row_3'] - 1]
            self.participant.vars['HL_series'] = 3
            self.participant.vars['HL_choice'] =  self.participant.vars['HL_choice_s3']
            self.participant.vars['a_value'] = Constants.s3_a1[self.participant.vars['HL_row_3'] - 1]
            self.participant.vars['aa_value'] = Constants.s3_a2[self.participant.vars['HL_row_3'] - 1]
            self.participant.vars['b11_value'] = Constants.s3_b1
            self.participant.vars['b12_value'] = Constants.s3_b2


# the coreography of pages
page_sequence = [
    TitlePage,
    ISTMELE,
    ISTMELE2,
    ISTMELE3,
    ISTMELE4,
    Instructions,
    Instructions2,
    PageHLExample,
    Payment,
    Payment2,
    PageHLExample1,
    PageHLExample2,
    PageHLExample3,
    PageHLExample3a,
    PageHLExample3b,
    Instructions3,
    MyWaitPage,
    PageHL,
    PageHL_2,
    PageHL_3,
    OutcomeHL,
]
