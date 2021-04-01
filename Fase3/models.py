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
    ra11 = [4550, 4500, 4450 , 4400 , 4350, 4330, 4300, 4200, 4280, 4230]
    ra12 = 4000
    rb11 = 5000
    rb12 = 6000
    ra1 = ra11[0]
    ra2 = ra11[1]
    ra3 = ra11[2]
    ra4 = ra11[3]
    ra5 = ra11[4]
    ra6 = ra11[5]
    ra7 = ra11[6]
    ra8 = ra11[7]
    ra9 = ra11[8]
    ra10 = ra11[9]

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

    # This is needed for the instructions
    rHL = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)



    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff_rHL(self):
        #*******************************************
        # select random row and random outcome
        #*******************************************
        self.participant.vars['rHL_row'] = random.randint(1,10)
        # select one row randomly for payment (from module random)
        self.participant.vars['rHL_random'] = random.randint(1,10)
        # select the number x that defines the outcome of the lottery (if x<=p, outcome is left f1 or f3, otherwise f2 or f4)
        # write it to participant.vars['HL_random']

        #*******************************************
        # select choices in correspondence to random row
        #*******************************************
        rchoices = [self.rHL_1,
                   self.rHL_2,
                   self.rHL_3,
                   self.rHL_4,
                   self.rHL_5,
                   self.rHL_6,
                   self.rHL_7,
                   self.rHL_8,
                   self.rHL_9,
                   self.rHL_10]
        # create a list with all choices of the player (see self)
        self.participant.vars['rHL_choice'] = rchoices[self.participant.vars['rHL_row']-1]
        # select from the list the choice in correspondence to the randomly drawn row (notice the offset)
        # write it to participant.vars['HL_choice']

        #*******************************************
        # Compute here the payoffs
        #*******************************************
        if self.participant.vars['rHL_random'] <= self.participant.vars['rHL_row']:
        # if the random number is smaller equal than the random row
            if self.participant.vars['rHL_choice'] == 1: #A
            # if the choice was A
                self.participant.vars['rpayoff_HL'] = Constants.ra11[self.participant.vars['rHL_row']-1]
                # because HL_row is the same as p in the MPL
            else : self.participant.vars['rpayoff_HL'] = Constants.rb11
        else:
        # if the random number is slarger than the random row
            if self.participant.vars['rHL_choice'] == 1 :#A
                # if the choice was A
                self.participant.vars['rpayoff_HL'] = Constants.ra12
                # because HL_row is the same as p in the MPL
            else :
                self.participant.vars['rpayoff_HL'] = Constants.rb12

        self.payoff = self.participant.vars['rpayoff_HL']
        # write the payoff to player.payoff

