from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random
class NotWinner(Page):


    def vars_for_template(self):
        return {
        "winners": self.session.vars["winners"],
        'app' : self.session.vars["app"],
        'id':   self.player.id_in_group
        }

    def is_displayed(self):
        return self.player.id_in_group not in self.session.vars["winners"]

class Winner(Page):


    def vars_for_template(self):
        return {
        "winners": self.session.vars["winners"],
        'app' : self.session.vars["app"],
        'id':   self.player.id_in_group
        }

    def is_displayed(self):
        return self.player.id_in_group in self.session.vars["winners"]

class ResultsWaitPage(WaitPage):
    pass

class Fase1(Page):
    def vars_for_template(self):
        return{
        "beliefs": self.participant.vars["beliefs_results"],
        "w_amt": self.participant.vars["w_amt"]

        }

    def is_displayed(self):
        return self.session.vars["app"] == 1 and self.player.id_in_group in self.session.vars["winners"]

    def before_next_page(self):
        self.player.payoff = round(self.participant.vars["w_amt"],2)

class Fase2(Page):
    def vars_for_template(self):
        payoff_HLc = round((self.player.participant.vars['payoff_HL']/1000) * (self.participant.vars['rate']),1)

        # retrieve values from participant.vars and store them in a dictionary
        return {
            'HL_series':  self.participant.vars['HL_series'],
            'payoff_HL': self.player.participant.vars['payoff_HL'],  # payoff
            'payoff_HLc': payoff_HLc,  # payoff
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
        return self.session.vars["app"] == 2 and self.player.id_in_group in self.session.vars["winners"]
    def before_next_page(self):
        self.player.payoff = round((self.participant.vars["payoff_HL"]/1000)* self.participant.vars['rate'],1)

class Fase3(Page):
    def vars_for_template(self):
        rpayoff_HLc = round((self.player.participant.vars['rpayoff_HL']/1000) * (self.participant.vars['rrate']),1)

        # retrieve values from participant.vars and store them in a dictionary
        return {
            'rHL_series': self.participant.vars['rHL_series'],
            'rpayoff_HL': self.player.participant.vars['rpayoff_HL'],
            'rpayoff_HLc':rpayoff_HLc, # payoff
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
            'rvar11': self.participant.vars['rvar11'],
            'rvar22': self.participant.vars['rvar22'],
            'rist_value': self.participant.vars['rist_value'],
            'prb1': self.participant.vars['prb1'],
            'prb2': self.participant.vars['prb2']
        }

    def is_displayed(self):
        return self.session.vars["app"] == 3 and self.player.id_in_group in self.session.vars["winners"]

    def before_next_page(self):
        self.player.payoff = round((self.participant.vars["rpayoff_HL"]/1000) * self.participant.vars['rrate'],1)

class goodbye(Page):
    form_model = 'player'



page_sequence = [NotWinner, Winner, Fase1, Fase2,Fase3, goodbye]
