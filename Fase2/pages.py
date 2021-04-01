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

class ISTMELE(Page):
    form_model = 'player'

class ISTMELE2(Page):
    form_model = 'player'

class ISTMELE3(Page):
    form_model = 'player'

class ISTMELE4(Page):
    form_model = 'player'


class PageHLExample(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['HL',]

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'a4': Constants.a4,
            'a12': Constants.a12,
            'b11': Constants.b11,
            'b12': Constants.b12,

        }

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    def before_next_page(self):
        # built-in method
        self.player.set_payoff_HL()# see in models in Player class


class PageHL(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['HL_1',
                   'HL_2',
                   'HL_3',
                   'HL_4',
                   'HL_5',
                   'HL_6',
                   'HL_7',
                   'HL_8',
                   'HL_9',
                   'HL_10'] # all 10 options

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'a1': Constants.a1,
            'a2': Constants.a2,
            'a3': Constants.a3,
            'a4': Constants.a4,
            'a5': Constants.a5,
            'a6': Constants.a6,
            'a7': Constants.a7,
            'a8': Constants.a8,
            'a9': Constants.a9,
            'a10': Constants.a10,
            'a12': Constants.a12,
            'b11': Constants.b11,
            'b12': Constants.b12,

        }

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    def before_next_page(self):
        # built-in method
        self.player.set_payoff_HL()# see in models in Player class
        self.participant.vars['a_value'] = Constants.a11[self.participant.vars['HL_row'] - 1]
        self.participant.vars['a12_value'] = Constants.a12
        self.participant.vars['b11_value'] = Constants.b11
        self.participant.vars['b12_value'] = Constants.b12

class OutcomeHL(WaitPage):
# values needed to inform subjects about the actual outcome
    def vars_for_template(self):
        # retrieve values from participant.vars and store them in a dictionary
        return{
        'payoff_HL': self.player.participant.vars['payoff_HL'],#payoff
        'row': self.player.participant.vars['HL_row'], # randomly chosen row
        'value': self.participant.vars['HL_random'],# randomly chosen value to define outcome
        'choice': self.participant.vars['HL_choice'],# actual choice
        # outcomes of the selected row
        'a_value': Constants.a11[self.participant.vars['HL_row'] - 1],
        'a12_value': Constants.a12,
        'b11_value': Constants.b11,
        'b12_value': Constants.b12,
        'p_A_1': self.participant.vars['HL_row'],
        'p_A_2': 10-self.participant.vars['HL_row'],
        'p_B_1': self.participant.vars['HL_row'],
        'p_B_2': 10-self.participant.vars['HL_row']
        }

    def before_next_page(self):
        self.participant.vars['a_value'] = Constants.a11[self.participant.vars['HL_row'] - 1]
        self.participant.vars['a12_value'] = Constants.a12
        self.participant.vars['b11_value'] = Constants.b11
        self.participant.vars['b12_value'] = Constants.b12


# the coreography of pages
page_sequence = [
    TitlePage,
    ISTMELE,
    ISTMELE2,
    ISTMELE3,
    ISTMELE4,
    Instructions,
    Instructions1,
    Instructions2,
    PageHLExample,
    PageHL,
]
