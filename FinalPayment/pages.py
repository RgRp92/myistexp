from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random
class MyPage(Page):


    def vars_for_template(self):
        return {
        "winner": self.session.vars["winner"],
        'app' : self.session.vars["app"],
        'id':   self.session.vars['id']
        }


class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    def vars_for_template(self):
        return{
        "beliefs": self.participant.vars["beliefs_results"],
        }

    def is_displayed(self):
        return self.session.vars["app"] == 1 and self.session.vars["winner"] == self.player.id_in_group


class Results2(Page):
    def vars_for_template(self):
        # retrieve values from participant.vars and store them in a dictionary
        return {
            'payoff_HL': self.player.participant.vars['payoff_HL'],  # payoff
            'row': self.player.participant.vars['HL_row'],  # randomly chosen row
            'value': self.participant.vars['HL_random'],  # randomly chosen value to define outcome
            'choice': self.participant.vars['HL_choice'],  # actual choice
            # outcomes of the selected row
            'a_value': self.participant.vars['a_value'],
            'a12_value': self.participant.vars['a12_value'],
            'b11_value':self.participant.vars['b11_value'],
            'b12_value': self.participant.vars['b12_value'],
            'p_A_1': self.participant.vars['HL_row'],
            'p_A_2': 10 - self.participant.vars['HL_row'],
            'p_B_1': self.participant.vars['HL_row'],
            'p_B_2': 10 - self.participant.vars['HL_row']
        }

    def is_displayed(self):
        return self.session.vars["app"] == 2 and self.session.vars["winner"] == self.player.id_in_group
class Results3(Page):
    def vars_for_template(self):
        # retrieve values from participant.vars and store them in a dictionary
        return {
            'rpayoff_HL': self.player.participant.vars['rpayoff_HL'],  # payoff
            'rrow': self.player.participant.vars['rHL_row'],  # randomly chosen row
            'rvalue': self.participant.vars['rHL_random'],  # randomly chosen value to define outcome
            'rchoice': self.participant.vars['rHL_choice'],  # actual choice
            # outcomes of the selected row
            'ra_value': self.participant.vars['ra_value'],
            'ra12_value': self.participant.vars['ra12_value'],
            'rb11_value':self.participant.vars['rb11_value'],
            'rb12_value': self.participant.vars['rb12_value'],
            'rp_A_1': self.participant.vars['rHL_row'],
            'rp_A_2': 10 - self.participant.vars['rHL_row'],
            'rp_B_1': self.participant.vars['rHL_row'],
            'rp_B_2': 10 - self.participant.vars['rHL_row']
        }

    def is_displayed(self):
        return self.session.vars["app"] == 3 and self.session.vars["winner"] == self.player.id_in_group


class goodbye(Page):
    def is_displayed(self):
        return self.session.vars["winner"] != self.player.id_in_group


page_sequence = [MyPage, Results, Results2,Results3, goodbye]
