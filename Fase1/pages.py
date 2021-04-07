from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import pandas as pd
import random
import json
from random import choices

def get_beldat(page_obj):

    farm_dat = page_obj.session.vars["beliefs_farm_dat"]

    bin_labels = [str(farm_dat["alt" + str(b)].iloc[0]) for b in range(1, 11) if str(farm_dat["alt" + str(b)].iloc[0]) != "nan"]
    alt_labels = [str(farm_dat["alt" + str(b)].iloc[0]) for b in range(1, 11) if str(farm_dat["alt" + str(b)].iloc[0]) != "nan"]

    # If bin_button is empty, don't show the button to toggle alt labels
    bin_button = str(farm_dat["bin_button"].iloc[0]).strip()
    bin_button = bin_button if bin_button != "nan" else ""
    pay_by = str(farm_dat["pay_by"].iloc[0]).strip()

    beldat = {
        "tokens": int(farm_dat["tokens"].iloc[0]),
        "alpha": float(farm_dat["alpha"].iloc[0]),
        "delta": float(farm_dat["delta"].iloc[0]),
        "currency": str(farm_dat["currency"].iloc[0]),
        "text": str(farm_dat["text"].iloc[0]),
        "alt_text": str(farm_dat["alt_text"].iloc[0]),
        "bin_button": bin_button,
        "alt_button": str(farm_dat["alt_button"].iloc[0]),
        "pay_by": pay_by,
        "bin_labels": bin_labels,
        "alt_labels": alt_labels,
        "num_bins": len(bin_labels),
    }

    # Store this data in the round data
    page_obj.participant.vars["beliefs_round_data"].append(beldat)
    return(beldat)

def set_beliefs_data(page_obj):
    nrounds = [1,2,3]
    nrounds = len(nrounds)
    page_obj.participant.vars["beliefs_num_rounds"] = nrounds

class TitlePage(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Intro(Page):
    def vars_for_template(self):
        # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Instructions2(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class TaskPageExample(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    form_model = "player"

    def initial_values(self):
        rnum = self.round_number
        if rnum == 1 and "beldat_is_set" not in self.participant.vars:
            # Record the choices for every round here
            self.participant.vars["beliefs_choice"] = []
            # Record the data for each choice
            self.participant.vars["beliefs_round_data"] = []

    def get_form_fields(self):
        # Set initial values for this participant
        self.initial_values()
        # The belief data
        beldat = get_beldat(self)
        # Add the labelset val as wel
        form_fields = ["bin" + str(i) for i in range(1, len(beldat["alt_labels"]) + 1)] + ["labelset"]
        return(form_fields)

    def vars_for_template(self):
        # Set initial values for this participant
        self.initial_values()

        # The lottery data for this row
        beldat = get_beldat(self)

        beliefs = {"round_number"    : self.round_number,
                   "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
                   "hex_colors"      : self.session.vars["beliefs_hex_colors"],
                   "beldat"          : beldat,
                   "tokens"          : beldat["tokens"],
                   "currency"        : beldat["currency"],
                   "task_number"     : 1,
                   }
        return {
            "beliefs": beliefs,
        }

    def is_displayed(self):
        return self.round_number <= 1

class TaskPageExample2(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class TaskPageExample3(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class QuizPage(Page):
    form_model = 'player'
    form_fields = ['quiz','quiz2']

    def quiz_error_message(self, value):
        if value != '1':
            return 'La risposta non è corretta. La preghiamo di correggere la sua risposta.'
        else:
            'La risposta  è corretta'

    def quiz2_error_message(self, value):
        if value != '1':
            return 'La risposta non è corretta. La preghiamo di correggere la sua risposta.'
        else:
            pass


    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Instructions3(Page):
    def is_displayed(self):
        return self.round_number == 1

class Instructions4(Page):
    def is_displayed(self):
        return self.round_number == 1

class Instructions5(Page):
    def is_displayed(self):
        return self.round_number == 1

class TaskPageExample4(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class TaskPageExample5(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class TaskPageExample5b(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class TaskPageExample5c(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class TaskPageExample5d(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class TaskPageExample6(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class TaskPageExample6b(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class TaskPageExample6c(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class MyWaitPage(Page):
    template_name = 'Fase1/MyWaitPage.html'

    def is_displayed(self):

        return self.round_number == 1

class FarmerChoice(Page):
    form_model  = "player"

    def initial_values(self):
        rnum = self.round_number
        # Randomize the data if we're in the first round
        if rnum == 1 and "beldat_is_set" not in self.participant.vars:
            self.participant.vars["beldat_is_set"] = True
            # Record the choices for every round here
            self.participant.vars["beliefs_choice"] = []
            # Record the data for each choice
            self.participant.vars["beliefs_round_data"] = []

    def get_form_fields(self):
        # Set initial values for this participant
        self.initial_values()
        # The belief data
        beldat = get_beldat(self)
        # Add the labelset val as wel
        form_fields = ["bin" + str(i) for i in range(1, len(beldat["bin_labels"]) + 1)] + ["labelset"]
        return(form_fields)

    def vars_for_template(self):
        # Set initial values for this participant
        self.initial_values()

        # The lottery data for this row
        beldat = get_beldat(self)


        beliefs = {"round_number"    : self.round_number,
                   "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
                   "hex_colors"      : self.session.vars["beliefs_hex_colors"],
                   "beldat"          : beldat,
                   "tokens"          : beldat["tokens"],
                   "currency"        : beldat["currency"],
                   "task_number"     : 1,
               }


        return {
            "beliefs": beliefs,
            }

    def is_displayed(self):
        return self.round_number <= self.participant.vars["beliefs_num_rounds"]

    def before_next_page(self):
        choice = [getattr(self.player, "bin" + str(b)) for b in range(1, 11)]
        self.participant.vars["beliefs_choice"].append(choice)

class Repeat1(Page):
    form_model = "player"
    form_fields = ["rep_1"]

    def is_displayed(self):
        return self.round_number == round(1)

class Repeat2(Page):
    form_model = "player"
    form_fields = ["rep_2"]

    def is_displayed(self):
        return self.round_number == round(2)

class FarmerChoices1(Page):
    form_model = "player"

    def vars_for_template(self):
        # The saved choices made by the subject
        choices_made = self.participant.vars["beliefs_choice"]

        pay_choices = choices_made[0]
        pay_round = pay_choices

        # The lottery data for this row
        beldat = self.participant.vars["beliefs_round_data"][0]

        # Not really used anywhere
        final_payment = {
            "currency": beldat["currency"],
            "amounts": [],
            "when": [beldat["pay_by"]],
            "choices": pay_choices,
        }
        self.participant.vars["beliefs_final_payment"] = final_payment
        setattr(self.player, "final_payment", json.dumps(final_payment))

        beliefs_results = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat": beldat,
            "tokens": beldat["tokens"],
            "currency": beldat["currency"],
            "task_number": 6,
            "pay_round": pay_round,
            "pay_choices": pay_choices,
            "final_payment": final_payment,
        }
        # Save this data for use in the final results page
        self.participant.vars["beliefs_results"] = beliefs_results

        return {
            "beliefs": beliefs_results,
        }

    def is_displayed(self):
        return self.player.rep_1 == 'NO'

    def app_after_this_page(self, upcoming_apps):
        if self.player.rep_1 == 'NO':
            return 'Fase2'

class FarmerChoices2(Page):
    form_model = "player"

    def vars_for_template(self):
        # The saved choices made by the subject
        choices_made = self.participant.vars["beliefs_choice"]

        pay_choices = choices_made[0]
        pay_round = pay_choices

        pay_choices_2 = choices_made[1]
        pay_round_2 = pay_choices_2

        # The lottery data for this row
        beldat = self.participant.vars["beliefs_round_data"][0]


        beliefs_results = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat": beldat,
            "tokens": beldat["tokens"],
            "currency": beldat["currency"],
            "task_number": 6,
            "pay_round": pay_round,
            "pay_choices": pay_choices,
        }
        beliefs_results_2 = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat": beldat,
            "tokens": beldat["tokens"],
            "currency": beldat["currency"],
            "task_number": 6,
            "pay_round": pay_round_2,
            "pay_choices": pay_choices_2,
        }

        # Save this data for use in the final results page
        self.participant.vars["beliefs_results"] = beliefs_results

        return {
            "beliefs": beliefs_results,
            "beliefs_2": beliefs_results_2,
        }

    def before_next_page(self):
        self.player.sum_token = sum([self.player.pref1, self.player.pref2])
        self.participant.vars["weights"] = [self.player.pref1,self.player.pref2]

    def is_displayed(self):
        return self.player.rep_2 == 'NO'

class FarmerChoices3(Page):
    form_model = "player"
    form_fields = ['pref1', 'pref2','pref3']

    def vars_for_template(self):
        # The saved choices made by the subject
        choices_made = self.participant.vars["beliefs_choice"]

        pay_choices = choices_made[0]
        pay_round = pay_choices

        pay_choices_2 = choices_made[1]
        pay_round_2 = pay_choices_2

        pay_choices_3 = choices_made[2]
        pay_round_3 = pay_choices_3

        # The lottery data for this row
        beldat = self.participant.vars["beliefs_round_data"][0]

        # Not really used anywhere
        final_payment = {
                "currency" : beldat["currency"],
                "amounts": [],
                "when": [beldat["pay_by"]],
                "choices": pay_choices,
                }
        self.participant.vars["beliefs_final_payment"] = final_payment
        setattr(self.player, "final_payment", json.dumps(final_payment))

        beliefs_results = {
                "round_number"    : self.round_number,
                "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
                "hex_colors"      : self.session.vars["beliefs_hex_colors"],
                "beldat"          : beldat,
                "tokens"          : beldat["tokens"],
                "currency"        : beldat["currency"],
                "task_number"     : 6,
                "pay_round": pay_round,
                "pay_choices": pay_choices,
                "final_payment" : final_payment,
               }
        beliefs_results_2 = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat": beldat,
            "tokens": beldat["tokens"],
            "currency": beldat["currency"],
            "task_number": 6,
            "pay_round": pay_round_2,
            "pay_choices": pay_choices_2,
            "final_payment": final_payment,
        }

        beliefs_results_3 = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat": beldat,
            "tokens": beldat["tokens"],
            "currency": beldat["currency"],
            "task_number": 6,
            "pay_round": pay_round_3,
            "pay_choices": pay_choices_3,
            "final_payment": final_payment,
        }

        # Save this data for use in the final results page
        self.participant.vars["beliefs_results"] = beliefs_results

        return {
            "beliefs": beliefs_results,
            "beliefs_2": beliefs_results_2,
            "beliefs_3": beliefs_results_3,
        }

    def is_displayed(self):
        return self.round_number == self.participant.vars["beliefs_num_rounds"]

    def before_next_page(self):
        self.player.sum_token = sum([self.player.pref1, self.player.pref2, self.player.pref3])
        self.participant.vars["weights"] = [self.player.pref1, self.player.pref2, self.player.pref3]



class Result1(Page):
    form_model  = "player"

    def vars_for_template(self):
        # The number of rounds
        num_rounds = self.participant.vars["beliefs_num_rounds"]
        # Select a round at random for payment
        if "beliefs_pay_round" not in self.participant.vars:
            pay_round = [0]
            pay_round = random.choice(pay_round)
            self.participant.vars["beliefs_pay_round"] = pay_round
        else:
            pay_round = self.participant.vars["beliefs_pay_round"]

        # The saved choices made by the subject
        choices_made = self.participant.vars["beliefs_choice"]
        pay_choices = choices_made[pay_round]

        # The lottery data for this row
        beldat = self.participant.vars["beliefs_round_data"][pay_round]

        # Not really used anywhere
        final_payment = {
                "currency" : beldat["currency"],
                "amounts": [],
                "when": [beldat["pay_by"]],
                "choices": pay_choices,
                }
        self.participant.vars["beliefs_final_payment"] = final_payment
        setattr(self.player, "final_payment", json.dumps(final_payment))

        beliefs_results = {
                "round_number"    : self.round_number,
                "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
                "hex_colors"      : self.session.vars["beliefs_hex_colors"],
                "beldat"          : beldat,
                "tokens"          : beldat["tokens"],
                "currency"        : beldat["currency"],
                "task_number"     : 6,
                "pay_round": pay_round + 1,
                "pay_choices": pay_choices,
                "final_payment" : final_payment,
               }

        # Save this data for use in the final results page
        self.participant.vars["beliefs_results"] = beliefs_results

        return {
            "beliefs" : beliefs_results,
        }

    def is_displayed(self):
        return self.player.rep_1 == "NO"


    def app_after_this_page(self, upcoming_apps):
        if self.player.rep_1 == 'NO':
            return 'Fase2'

class Result2(Page):
    form_model  = "player"

    def vars_for_template(self):
        weights = self.participant.vars["weights"]
        # The number of rounds
        num_rounds = [0, 1]
        # Select a round at random for payment
        if "beliefs_pay_round" not in self.participant.vars:
            pay_round = choices(num_rounds, weights)
            self.participant.vars["beliefs_pay_round"] = pay_round
        else:
            pay_round = self.participant.vars["beliefs_pay_round"]

        pay_round = pay_round[0]
        # The saved choices made by the subject
        choices_made = self.participant.vars["beliefs_choice"]
        pay_choices = choices_made[pay_round]

        # The lottery data for this row
        beldat = self.participant.vars["beliefs_round_data"][pay_round]

        # Not really used anywhere
        final_payment = {
                "currency" : beldat["currency"],
                "amounts": [],
                "when": [beldat["pay_by"]],
                "choices": pay_choices,
                }
        self.participant.vars["beliefs_final_payment"] = final_payment
        setattr(self.player, "final_payment", json.dumps(final_payment))

        beliefs_results = {
                "round_number"    : self.round_number,
                "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
                "hex_colors"      : self.session.vars["beliefs_hex_colors"],
                "beldat"          : beldat,
                "tokens"          : beldat["tokens"],
                "currency"        : beldat["currency"],
                "task_number"     : 6,
                "pay_round": pay_round + 1,
                "pay_choices": pay_choices,
                "final_payment" : final_payment,
               }

        # Save this data for use in the final results page
        self.participant.vars["beliefs_results"] = beliefs_results

        return {
            "beliefs" : beliefs_results,
        }

    def is_displayed(self):
        return self.player.rep_2 == "NO"


    def app_after_this_page(self, upcoming_apps):
        if self.player.rep_2 == 'NO':
            return 'Fase2'

class Results(Page):
    form_model  = "player"

    def vars_for_template(self):
        weights = self.participant.vars["weights"]
        # The number of rounds
        num_rounds = [0,1,2]
        # Select a round at random for payment
        if "beliefs_pay_round" not in self.participant.vars:
            pay_round = choices(num_rounds, weights)
            self.participant.vars["beliefs_pay_round"] = pay_round
        else:
            pay_round = self.participant.vars["beliefs_pay_round"]

        pay_round = pay_round[0]
        # The saved choices made by the subject
        choices_made = self.participant.vars["beliefs_choice"]
        pay_choices = choices_made[pay_round]

        # The lottery data for this row
        beldat = self.participant.vars["beliefs_round_data"][pay_round]

        # Not really used anywhere
        final_payment = {
                "currency" : beldat["currency"],
                "amounts": [],
                "when": [beldat["pay_by"]],
                "choices": pay_choices,
                }
        self.participant.vars["beliefs_final_payment"] = final_payment
        setattr(self.player, "final_payment", json.dumps(final_payment))

        beliefs_results = {
                "round_number"    : self.round_number,
                "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
                "hex_colors"      : self.session.vars["beliefs_hex_colors"],
                "beldat"          : beldat,
                "tokens"          : beldat["tokens"],
                "currency"        : beldat["currency"],
                "task_number"     : 6,
                "pay_round": pay_round + 1,
                "pay_choices": pay_choices,
                "final_payment" : final_payment,
               }

        # Save this data for use in the final results page
        self.participant.vars["beliefs_results"] = beliefs_results

        return {
            "beliefs" : beliefs_results,
        }

    def is_displayed(self):
        return self.round_number == self.participant.vars["beliefs_num_rounds"] and self.player.rep_2 != 'NO'

    def before_next_page(self):
        self.participant.vars["w_round"]= self.participant.vars["beliefs_results"]["pay_round"]


page_sequence = [
    TitlePage,
    Intro,
    Instructions2,
    TaskPageExample2,
    TaskPageExample3,
    QuizPage,
    TaskPageExample,
    Instructions3,
    Instructions4,
    Instructions5,
    TaskPageExample4,
    TaskPageExample5,
    TaskPageExample5b,
    TaskPageExample5c,
    TaskPageExample5d,
    TaskPageExample6,
    TaskPageExample6b,
    TaskPageExample6c,
    MyWaitPage,
    FarmerChoice,
    Repeat1,
    FarmerChoices1,
    Repeat2,
    FarmerChoices2,
    FarmerChoices3,
    Result2,
    Results
]
