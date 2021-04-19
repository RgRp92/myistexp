from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random
class MyPage1(Page):


    def vars_for_template(self):
        return {
        "winner": self.session.vars["winner"],
        'app' : self.session.vars["app"],
        'id':   self.session.vars['id']
        }

    def is_displayed(self):
        return self.session.vars["winner"] != self.player.id_in_group

class MyPage(Page):


    def vars_for_template(self):
        return {
        "winner": self.session.vars["winner"],
        'app' : self.session.vars["app"],
        'id':   self.session.vars['id']
        }

    def is_displayed(self):
        return self.session.vars["winner"] == self.player.id_in_group

class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    def vars_for_template(self):
        return{
        "beliefs": self.participant.vars["beliefs_results"],
        "w_amt": self.participant.vars["w_amt"]

        }

    def is_displayed(self):
        return self.session.vars["app"] == 1 and self.session.vars["winner"] == self.player.id_in_group

    def before_next_page(self):
        self.player.payoff = round(self.participant.vars["w_amt"],2)

class Results2(Page):
    def vars_for_template(self):
        # retrieve values from participant.vars and store them in a dictionary
        return {
            'HL_series':  self.participant.vars['HL_series'],
            'payoff_HL': self.player.participant.vars['payoff_HL'],  # payoff
            'row': self.player.participant.vars['HL_row'],  # randomly chosen row
            'value': self.participant.vars['HL_random'],  # randomly chosen value to define outcome
            'choice': self.participant.vars['HL_choice'],  # actual choice
            # outcomes of the selected row
            'a_value': self.participant.vars['a_value'],
            'aa_value': self.participant.vars['aa_value'],
            'b11_value':self.participant.vars['b11_value'],
            'b12_value': self.participant.vars['b12_value'],
            'p_A_1': self.participant.vars['HL_row'],
            'p_A_2': 10 - self.participant.vars['HL_row'],
            'p_B_1': self.participant.vars['HL_row'],
            'p_B_2': 10 - self.participant.vars['HL_row'],
            'var1' : self.participant.vars['var1'],
            'var2' : self.participant.vars['var2'],
            'ist_value': self.participant.vars['ist_value']
        }

    def is_displayed(self):
        return self.session.vars["app"] == 2 and self.session.vars["winner"] == self.player.id_in_group
    def before_next_page(self):
        self.player.payoff = round(self.participant.vars["payoff_HL"],2)

class Results3(Page):
    def vars_for_template(self):
        # retrieve values from participant.vars and store them in a dictionary
        return {
            'rHL_series': self.participant.vars['rHL_series'],
            'rpayoff_HL': self.player.participant.vars['rpayoff_HL'],  # payoff
            'rrow': self.player.participant.vars['rHL_row'],  # randomly chosen row
            'rvalue': self.participant.vars['rHL_random'],  # randomly chosen value to define outcome
            'rchoice': self.participant.vars['rHL_choice'],  # actual choice
            # outcomes of the selected row
            'ra_value': self.participant.vars['ra_value'],
            'raa_value': self.participant.vars['raa_value'],
            'rb11_value':self.participant.vars['rb11_value'],
            'rb12_value': self.participant.vars['rb12_value'],
            'rp_A_1': self.participant.vars['rHL_row'],
            'rp_A_2': 10 - self.participant.vars['rHL_row'],
            'rp_B_1': self.participant.vars['rHL_row'],
            'rp_B_2': 10 - self.participant.vars['rHL_row'],
            'rvar1': self.participant.vars['rvar1'],
            'rvar2': self.participant.vars['rvar2'],
            'rist_value': self.participant.vars['rist_value'],
            'prb1': self.participant.vars['prb1'],
            'prb2': self.participant.vars['prb2']
        }

    def is_displayed(self):
        return self.session.vars["app"] == 3 and self.session.vars["winner"] == self.player.id_in_group

    def before_next_page(self):
        self.player.payoff = round(self.participant.vars["rpayoff_HL"],2)

class goodbye(Page):
    form_model = 'player'



page_sequence = [MyPage1, MyPage, Results, Results2,Results3, goodbye]
