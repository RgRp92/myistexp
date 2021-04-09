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

class Instructions4(Page):
    form_model = 'player'


class PageHLExample(Page):
# which forms are needed from class player
    form_model = 'player'

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'ra4': Constants.ra4,
            'ra12': Constants.ra12,
            'rb11': Constants.rb11,
            'rb12': Constants.rb12,

        }

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)



class MyWaitPage(Page):
    form_model = 'player'

    def before_next_page(self):
        # built-in method
        self.player.set_payoff_rHL()# see in models in Player class


class PageHL(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['rHL_1',
                   'rHL_2',
                   'rHL_3',
                   'rHL_4',
                   'rHL_5',
                   'rHL_6',
                   'rHL_7',
                   'rHL_8',
                   'rHL_9',
                   'rHL_10'] # all 10 options

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'ra1': Constants.ra1,
            'ra2': Constants.ra2,
            'ra3': Constants.ra3,
            'ra4': Constants.ra4,
            'ra5': Constants.ra5,
            'ra6': Constants.ra6,
            'ra7': Constants.ra7,
            'ra8': Constants.ra8,
            'ra9': Constants.ra9,
            'ra10': Constants.ra10,
            'raa1': Constants.raa1,
            'raa2': Constants.raa2,
            'raa3': Constants.raa3,
            'raa4': Constants.raa4,
            'raa5': Constants.raa5,
            'raa6': Constants.raa6,
            'raa7': Constants.raa7,
            'raa8': Constants.raa8,
            'raa9': Constants.raa9,
            'raa10': Constants.raa10,
            'rb11': Constants.rb11,
            'rb12': Constants.rb12,

        }

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)


    def before_next_page(self):
    # built-in method
        self.player.set_payoff_rHL()  # see in models in Player class
        self.participant.vars['ra_value'] = Constants.ra11[self.participant.vars['rHL_row'] - 1]
        self.participant.vars['raa_value'] = Constants.ra12[self.participant.vars['rHL_row'] - 1]
        self.participant.vars['rb11_value'] = Constants.rb11
        self.participant.vars['rb12_value'] = Constants.rb12

class OutcomeHL(WaitPage):
# values needed to inform subjects about the actual outcome
    def vars_for_template(self):
        # retrieve values from participant.vars and store them in a dictionary
        return{
        'rpayoff_HL': self.player.participant.vars['rpayoff_HL'],#payoff
        'rrow': self.player.participant.vars['rHL_row'], # randomly chosen row
        'rvalue': self.participant.vars['rHL_random'],# randomly chosen value to define outcome
        'rchoice': self.participant.vars['rHL_choice'],# actual choice
        # outcomes of the selected row
        'ra_value': Constants.ra11[self.participant.vars['rHL_row'] - 1],
        'raa_value': Constants.ra12[self.participant.vars['rHL_row'] - 1],
        'rb11_value': Constants.rb11,
        'rb12_value': Constants.rb12,
        'rp_A_1': self.participant.vars['rHL_row'],
        'rp_A_2': 10-self.participant.vars['rHL_row'],
        'rp_B_1': self.participant.vars['rHL_row'],
        'rp_B_2': 10-self.participant.vars['rHL_row']
        }

    def before_next_page(self):
        self.participant.vars['ra_value'] = Constants.ra11[self.participant.vars['rHL_row'] - 1]
        self.participant.vars['raa_value'] = Constants.ra12[self.participant.vars['rHL_row'] - 1]
        self.participant.vars['rb11_value'] = Constants.rb11
        self.participant.vars['rb12_value'] = Constants.rb12



# the coreography of pages
page_sequence = [
                    TitlePage,
                    Instructions,
                    Instructions1,
                    Instructions2,
                    Instructions4,
                    PageHLExample,
                    MyWaitPage,
                    PageHL
]
