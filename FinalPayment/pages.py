from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random
class MyPage(Page):


    def vars_for_template(self):
        return {
        "winner": self.session.vars["winner"],
        'app' : self.session.vars["app"],
        }

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage]
