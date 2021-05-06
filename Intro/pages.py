from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Page0(Page):
    pass
class Page1(Page):
    pass
class Page2(Page):
    pass
class Page3(Page):
    def vars_for_template(self):
        return {
            "n_winners": self.session.vars['n_winners']
        }

class Page4(Page):
    form_model = 'player'
    form_fields = ['OP']


    def before_next_page(self):
        self.participant.vars["OP"] = self.player.OP

page_sequence = [Page0, Page1, Page2, Page3,Page4]
