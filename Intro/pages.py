from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class WelcomePage(Page):
    pass

class Intro(Page):
    pass
class Intro2(Page):
    pass
class Intro3(Page):
    pass

page_sequence = [WelcomePage, Intro, Intro2, Intro3]
