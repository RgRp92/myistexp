from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Ruggiero Rippo'

doc = """
Fase 4 Questionario
"""


class Constants(BaseConstants):
    name_in_url = 'Fase4'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.IntegerField(label='1. Età', min=18, max=125)
    q2 = models.StringField(
        choices=[['M', 'M'], ['F', 'F']],
        label='2. Genere',
        widget=widgets.RadioSelect,
    )
    q3 = models.StringField(
        choices=[['Scuola elementare', 'Scuola elementare'], ['Diploma scuola superiore', 'Diploma scuola superiore'],
                 ['Laurea 3 anni', 'Laurea 3 anni'], ['Laurea 5 anni', 'Laurea 5 anni'], ['Master', 'Master'],
                 ['Dottorato', 'Dottorato']],
        label='3. Titolo di studio',
        widget=widgets.RadioSelect,
    )
    q4 = models.StringField(
        choices=[['Fino a 5 anni', 'Fino a 5 anni'], ['Da 5 a 9 anni', 'Da 5 a 9 anni'],
                 ['Da 10 a 20 anni', 'Da 10 a 20 anni'],
                 ['Più di 20 anni', 'Più di 20 anni']],
        label='4. Da quanti anni è coinvolto nella coltivazione delle mele?',
        widget=widgets.RadioSelect,
    )
    q5 = models.IntegerField(min=1, max=100,
                             label='5. A quanti ettari corrisponde la superfice agricola della sua azienda?'
                             )
    q6 = models.IntegerField(min=1, max=100,
                             label='6.	Quanti ettari occupa la coltivazione a mele??'
                             )
    q7 = models.StringField(
        choices=[['1', 'Alta val di Non, Val di Sole'],
                 ['2', 'Bassa Val di non'],
                 ['3', 'Bleggio, Alto Garda, Ledro, Paganella'],
                 ['4', 'Valle dei Laghi'],
                 ['5', 'Piana Rotaliana'],
                 ['6', 'Valsugana'],
                 ['7', 'Territori dell Adige, Vallagarina, Valle di Cembra']],
        label='7. Zona di produzione',
        widget=widgets.RadioSelect,
    )
    q8_a = models.BooleanField(blank=True, initial=False)
    q8_b = models.BooleanField(blank=True, initial=False)
    q8_c = models.BooleanField(blank=True, initial=False)

    q9_a = models.BooleanField(blank=True, initial=False)
    q9_b = models.BooleanField(blank=True, initial=False)
    q9_c = models.BooleanField(blank=True, initial=False)
    q9_d = models.BooleanField(blank=True, initial=False)
    q9_e = models.BooleanField(blank=True, initial=False)
    q9_f = models.BooleanField(blank=True, initial=False)
    q9_g = models.BooleanField(blank=True, initial=False)
    q9_h = models.BooleanField(blank=True, initial=False)
    q9_i = models.BooleanField(blank=True, initial=False)

    q10_a1 = models.BooleanField(blank=True, initial=False)
    q10_a2 = models.BooleanField(blank=True, initial=False)
    q10_a3 = models.BooleanField(blank=True, initial=False)
    q10_a4 = models.BooleanField(blank=True, initial=False)
    q10_a5 = models.BooleanField(blank=True, initial=False)

    q10_b1 = models.BooleanField(blank=True, initial=False)
    q10_b2 = models.BooleanField(blank=True, initial=False)
    q10_b3 = models.BooleanField(blank=True, initial=False)
    q10_b4 = models.BooleanField(blank=True, initial=False)
    q10_b5 = models.BooleanField(blank=True, initial=False)

    q10_c1 = models.BooleanField(blank=True, initial=False)
    q10_c2 = models.BooleanField(blank=True, initial=False)
    q10_c3 = models.BooleanField(blank=True, initial=False)
    q10_c4 = models.BooleanField(blank=True, initial=False)
    q10_c5 = models.BooleanField(blank=True, initial=False)

    q10_d1 = models.BooleanField(blank=True, initial=False)
    q10_d2 = models.BooleanField(blank=True, initial=False)
    q10_d3 = models.BooleanField(blank=True, initial=False)
    q10_d4 = models.BooleanField(blank=True, initial=False)
    q10_d5 = models.BooleanField(blank=True, initial=False)

    q10_e1 = models.BooleanField(blank=True, initial=False)
    q10_e2 = models.BooleanField(blank=True, initial=False)
    q10_e3 = models.BooleanField(blank=True, initial=False)
    q10_e4 = models.BooleanField(blank=True, initial=False)
    q10_e5 = models.BooleanField(blank=True, initial=False)

    q10_f1 = models.BooleanField(blank=True, initial=False)
    q10_f2 = models.BooleanField(blank=True, initial=False)
    q10_f3 = models.BooleanField(blank=True, initial=False)
    q10_f4 = models.BooleanField(blank=True, initial=False)
    q10_f5 = models.BooleanField(blank=True, initial=False)

    q11 = models.StringField(
        choices=[['SI', 'SI'], ['NO', 'NO']],
        label='11. Fa parte di una OP?',
        widget=widgets.RadioSelect)

    q12 = models.StringField(
        choices=[['Tra € 0 e € 24.999', 'Tra € 0 e € 24.999'],
                 ['Tra € 25.000 e € 49.999 ', 'Tra € 25.000 e € 49.999 '],
                 ['Tra € 50.000 e € 74.999', 'Tra € 50.000 e € 74.999'],
                 ['Tra € 75.000 e € 100.000', 'Tra € 75.000 e € 100.000'],
                 ['Oltre € 100.000', 'Oltre € 100.000']],
        label='12. Negli ultimi 3 anni quale è stato il suo reddito ad ettaro netto? ',
        widget=widgets.RadioSelect)


    q13 = models.IntegerField(label='13. Negli ultimi 3 anni, quale percentuale del suo reddito è derivata da mele?'
                                    '', min=0, max=100)

    q14 = models.IntegerField(label='14. Negli ultimi 3 anni, quanto hanno inciso i costi per la produzione di mele ad ettaro?'
                                    '', min=0)

    q15 = models.StringField(
        choices=[['SI', 'SI'], ['NO', 'NO'],['Non saprei','Non saprei']],
        label='15. Pensa che la sua attività melicola sarà continuata nel futuro da un familiare?',
        widget=widgets.RadioSelect)

    q16 = models.StringField(
        choices=[['SI', 'SI'], ['NO', 'NO']],
        label='16. Nel 2021 ha sottoscritto la partecipazione e la copertura mutualisitca Fondo IST-Mele?',
        widget=widgets.RadioSelect)

    q16_a = models.BooleanField(blank=True, initial=False)
    q16_b = models.BooleanField(blank=True, initial=False)
    q16_c = models.BooleanField(blank=True, initial=False)
    q16_d = models.BooleanField(blank=True, initial=False)

    q17_a = models.BooleanField(blank=True, initial=False)
    q17_b = models.BooleanField(blank=True, initial=False)
    q17_c = models.BooleanField(blank=True, initial=False)
    q17_d = models.BooleanField(blank=True, initial=False)
    q17_e = models.BooleanField(blank=True, initial=False)

    q18_a = models.BooleanField(blank=True, initial=False)
    q18_b = models.BooleanField(blank=True, initial=False)
    q18_c = models.BooleanField(blank=True, initial=False)
    q18_d = models.BooleanField(blank=True, initial=False)
    q18_e = models.BooleanField(blank=True, initial=False)

    q19_a = models.BooleanField(blank=True, initial=False)
    q19_b = models.BooleanField(blank=True, initial=False)
    q19_c = models.BooleanField(blank=True, initial=False)
    q19_d = models.BooleanField(blank=True, initial=False)
    q19_e = models.BooleanField(blank=True, initial=False)

    q20 = models.StringField(
        choices=[['Su base triennale', 'Su base triennale'], ['Su base quinquennale', 'Su base quinquennale']],
        label='20. Preferirebbe che il reddito medio sia calcolato:',
        widget=widgets.RadioSelect )

    q21 = models.StringField(
        choices=[['Dipendando dal Trigger Event', 'Dipendando dal Trigger Event'], ['Non dipendano dal Trigger Event',
                                                                                    'Non dipendano dal Trigger Event']],
        label='21. Preferirebbe che le richieste di risarcimento al Fondo IST Mele:',
        widget=widgets.RadioSelect )