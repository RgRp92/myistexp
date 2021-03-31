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
    name_in_url = 'Fase2SF'
    players_per_group = None
    num_rounds = 1
    # these are the lottery payoffs, f1 and f2 refer to lottery A and f3 and f4 to lottery B
    a11 = [68, 75, 83, 93, 106, 125, 150, 185, 220, 300]
    a12 = 5500
    b11 = 3500
    b12 = 6000
    a1 = a11[0]
    a2 = a11[1]
    a3 = a11[2]
    a4 = a11[3]
    a5 = a11[4]
    a6 = a11[5]
    a7 = a11[6]
    a8 = a11[7]
    a9 = a11[8]
    a10 = a11[9]


class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):

    # This is for main choices, each variable is one row in the choice table MPL
    HL_1 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_2 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_3 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_4 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_5 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_6 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_7 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_8 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_9 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_10 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)

    # This is needed for the instructions
    HL = models.IntegerField(choices=[[1,'A'],[2,'B']],widget=widgets.RadioSelectHorizontal,initial=0)



    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff_HL(self):
        #*******************************************
        # select random row and random outcome
        #*******************************************
        self.participant.vars['HL_row'] = random.randint(1,10)
        # select one row randomly for payment (from module random)
        self.participant.vars['HL_random'] = random.randint(1,10)
        # select the number x that defines the outcome of the lottery (if x<=p, outcome is left f1 or f3, otherwise f2 or f4)
        # write it to participant.vars['HL_random']

        #*******************************************
        # select choices in correspondence to random row
        #*******************************************
        choices = [self.HL_1,
                   self.HL_2,
                   self.HL_3,
                   self.HL_4,
                   self.HL_5,
                   self.HL_6,
                   self.HL_7,
                   self.HL_8,
                   self.HL_9,
                   self.HL_10]
        # create a list with all choices of the player (see self)
        self.participant.vars['HL_choice'] = choices[self.participant.vars['HL_row']-1]
        # select from the list the choice in correspondence to the randomly drawn row (notice the offset)
        # write it to participant.vars['HL_choice']

        #*******************************************
        # Compute here the payoffs
        #*******************************************
        if self.participant.vars['HL_random'] <= self.participant.vars['HL_row']:
        # if the random number is smaller equal than the random row
            if self.participant.vars['HL_choice'] == 1: #A
            # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.a11[self.participant.vars['HL_row']-1]
                # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.b11
        else:
        # if the random number is slarger than the random row
            if self.participant.vars['HL_choice'] == 1 :#A
                # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.a12
                # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.b12

        self.payoff = self.participant.vars['payoff_HL']
        # write the payoff to player.payoff

