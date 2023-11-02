import random
import csv
import numpy
import numpy as np
import time

from otree.api import *
oc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

def creating_session(subsession:Subsession):
    session = Subsession.session
    liste = []
    ###
    p = Subsession.session
    p.treatment = []

    treat = []
    x2 = list([0, 1, 2] * 200)
    for i in range(0, 600):
        random.shuffle(x2)
        b = x2.pop(0)
        p.treatment.append(b)
        treat.append(b)

    for i in range(200):
        y = list(range(1,401,2))
        x = random.sample(y,5)
        z = []
        for i in x:
            z.append(i + 1)
        for i in list(range(0,5)):
            x.append(z[i])
        random.shuffle(x)
        liste.append(x)
        ####get lists together
        # one list for all participants
    seq_list = [None] * 600
    k1 = 0
    k2 = 0
    k3 = 0

    for i in range(0, 600):
        if treat[i] == 0:
            seq_list[i] = liste[k1][0:10]
            k1 = k1 + 1
        elif treat[i] == 1:
            seq_list[i] = liste[k2][0:10]
            k2 = k2 + 1
        else:
            seq_list[i] = liste[k3][0:10]
            k3 = k3 + 1

    session.liste = seq_list
    r2 = csv.reader(open(r"/Users/lennardhannemann/Desktop/Exp_Matching/pricelist_all.csv"), delimiter=";")
    y2 = list(r2)
    session.pricelist = y2





class Group(BaseGroup):
    pass


class Player (BasePlayer):
    time_check = models.FloatField(blank=True)



# PAGES
class General(Page):
    pass
class Investment(Page):
    # create words and sentences which depend on treatment

    def vars_for_template(player:Player):
        p = player.participant
        session = Subsession.session
        p.decision = []
        p.treat = session.treatment[player.id_in_group-1]

        if p.treat == 0:
            c = "a price chart of an asset will be displayed"
            d = "In a price chart, the historical development of an asset's price over the last year can be seen."
            a = "Each price chart starts at a price of 100."

        elif p.treat == 1:
            c = "a return chart of an asset will be displayed"
            d = "In a return chart, the historical sequence of returns over the last year can be seen."
            a = ""
        else:
            c = "the weekly prices over the last year of an asset are displayed in a list"
            d = ""
            a = ""
        p = player.session
        p.liste = session.liste
        p.pricelist = session.pricelist

        p = player.participant
        s = player.session
        p.list1 = s.liste[player.id_in_group-1][0]
        p.list2 = s.liste[player.id_in_group - 1][1]
        p.list3 = s.liste[player.id_in_group - 1][2]
        p.list4 = s.liste[player.id_in_group - 1][3]
        p.list5 = s.liste[player.id_in_group - 1][4]
        p.list6 = s.liste[player.id_in_group - 1][5]
        p.list7 = s.liste[player.id_in_group - 1][6]
        p.list8 = s.liste[player.id_in_group - 1][7]
        p.list9 = s.liste[player.id_in_group - 1][8]
        p.list10 = s.liste[player.id_in_group - 1][9]

        return dict(
            c=c,
            d=d,
            a=a,


        )
class Payout(Page):
    form_model = "player"
    form_fields = ['time_check']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.time_check = time.time()
        p = player.participant
        p.time = player.time_check
class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [General, Investment, Payout]
