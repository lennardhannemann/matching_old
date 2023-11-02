import random
import csv
import numpy
import numpy as np
from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'new'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 20
    #dictionary for pricecharts: high score chart
    DIC1 = [None]*400
    for i in range(1, 401):
        nr = str(i)
        x = ("pricechart",".png")
        DIC1[i-1] = {"ImagePath": nr.join(x)}
    # dictionary for pricecharts: low score chart
    DIC2 = [None] * 400
    for i in range(1, 401):
        nr = str(i)
        x = ("returnchart", ".png")
        DIC2[i-1] = {"ImagePath": nr.join(x)}

    ##list of prices high score charts -> first path is matched with the first path from the list in DIC6
    r2 = csv.reader(open(r"/Users/lennardhannemann/Desktop/pricelist_high.csv"), delimiter=";")
    y2 = list(r2)
    DIC5 = y2

    ##list of prices low score charts
    r2 = csv.reader(open(r"/Users/lennardhannemann/Desktop/pricelist_low.csv"), delimiter=";")
    y2 = list(r2)
    DIC6 = y2
    #payoffs
    DIC7 = []
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
#create fields

    likert_scale = models.IntegerField(label="",
                                       widget=widgets.RadioSelectHorizontal,
                                       choices=[
                                           [1, '1'],
                                           [2, '2'],
                                           [3, '3'],
                                           [4, '4'],
                                           [5, '5']

                                       ])

    decision = models.IntegerField(label="",
                                       widget=widgets.RadioSelectHorizontal,
                                       choices=[
                                           [0, 'Asset A'],
                                           [1, 'Asset B']
                                       ])
# PAGES
class MyPage(Page):
    def is_displayed(player: Player):
        p = player.participant
        if p.treat==0 or p.treat==1:
            return True
        else:
            return False

    form_model = "player"
    form_fields = ['decision']

    def vars_for_template(player: Player):
        session = player.session
        p = player.participant
        x = session.liste[player.id_in_group-1][player.round_number-1]-1
        b = player.round_number
        if p.treat == 0:
            if session.order[player.id_in_group-1][player.round_number-1] == 0: #if value=0 -> high score chart is displayed on the left

                ImagePath = C.DIC1[x]['ImagePath']

                c = "prices"


                ImagePath2 = C.DIC2[x]['ImagePath']

            else:

                ImagePath = C.DIC2[x]['ImagePath']

                c = "prices"


                ImagePath2 = C.DIC1[x]['ImagePath']


        else:
            if session.order[player.id_in_group - 1][player.round_number - 1] == 0:  # if value=0 -> high score chart is displayed on the left

                ImagePath = C.DIC3[x]['ImagePath']

                c = "returns"


                ImagePath2 = C.DIC4[x]['ImagePath']

            else:

                ImagePath = C.DIC4[x]['ImagePath']

                c = "returns"


                ImagePath2 = C.DIC3[x]['ImagePath']




        return dict(
            ImagePath=ImagePath,
            c=c,
            ImagePath2=ImagePath2,
            b=b
            )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):#save investment decision
        session = player.session
        if session.order == 0:
            p = player.participant
            p.decision.append(player.decision)
        else:
            p = player.participant
            if player.decision == 0:
                p.decision.append(1)
            else:
                p.decision.append(0)
        ###decision=1 if the convex path was chosen
class MyPage2(Page):
    def is_displayed(player: Player):
        p = player.participant
        if p.treat==0 or p.treat==1:
            return True
        else:
            return False

    form_model = "player"
    form_fields = ['likert_scale']

    def vars_for_template(player: Player):
        b = player.round_number
        session = player.session
        p = player.participant
        x = session.liste[player.id_in_group - 1][player.round_number-1]-1
        if p.treat == 0:
            if session.order[player.id_in_group - 1][player.round_number-1] == 0:  # if value=0 -> high score chart is displayed on the left

                ImagePath = C.DIC1[x]['ImagePath']
                c = "prices"
                ImagePath2 = C.DIC2[x]['ImagePath']

            else:

                ImagePath = C.DIC2[x]['ImagePath']
                c = "prices"
                ImagePath2 = C.DIC1[x]['ImagePath']


        else:
            if session.order[player.id_in_group - 1][player.round_number - 1] == 0:  # if value=0 -> high score chart is displayed on the left

                ImagePath = C.DIC3[x]['ImagePath']
                c = "returns"
                ImagePath2 = C.DIC4[x]['ImagePath']

            else:

                ImagePath = C.DIC4[x]['ImagePath']
                c = "returns"
                ImagePath2 = C.DIC3[x]['ImagePath']



        return dict(
            ImagePath=ImagePath,
            c=c,
            ImagePath2=ImagePath2,
            b=b

        )


    def before_next_page(player: Player, timeout_happened):# calculate payoff
        p = player.participant
        if player.round_number==C.NUM_ROUNDS:
            p.a = random.randint(0, player.round_number-1)  # randomly select an investment decision
            s = player.session
            p.dec = p.decision[p.a]
            numberchart = s.liste[player.id_in_group - 1][p.a]  # save picture number of selected round
            p.returns = round(C.DIC7[p.dec][numberchart-1] * 100, 2)  # calculate payoff ->use matrix in which in the left column payoff of the high score chart is saved
            returns2 = 1 + C.DIC7[p.dec][numberchart-1]
            p.wealth = round(returns2 * 1000, 2)
            p.payoff = p.wealth * 0.0005  # save payoff in participant field so that participant can get the variable payout
        else:
            p.payoff = 0


class MyPage3 (Page):
    def is_displayed(player: Player):
        p = player.participant
        if p.treat==2:
            return True
        else:
            return False
    form_model = "player"
    form_fields = ["decision"]
    def vars_for_template(player: Player):
        b = player.round_number
        session = player.session
        x = session.liste[player.id_in_group-1][player.round_number-1]
        if session.order[player.id_in_group-1][player.round_number-1]==0:
            pricelist1_1 = C.DIC5[x]
            pricelist1_2 = C.DIC6[x]


        else:
            pricelist1_1 = C.DIC6[x]
            pricelist1_2 = C.DIC5[x]


        return dict(
            pricelist1_1=pricelist1_1,
            pricelist1_2=pricelist1_2,
            b=b,


        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):  # save investment decision
        p = player.session
        if p.order == 0:
            p = player.participant
            p.decision.append(player.decision)
        else:
            p = player.participant
            if player.decision == 0:
                p.decision.append(1)
            else:
                p.decision.append(0)

class MyPage4(Page):
    def is_displayed(player: Player):
        p = player.participant
        if p.treat==2:
            return True
        else:
            return False

    form_model = "player"
    form_fields = ["likert_scale"]

    def vars_for_template(player: Player):
        b = player.round_number
        session = player.session
        x = session.liste[player.id_in_group - 1][player.round_number - 1]
        if session.order[player.id_in_group - 1][player.round_number - 1] == 0:
            pricelist1_1 = C.DIC5[x]
            pricelist1_2 = C.DIC6[x]

        else:
            pricelist1_1 = C.DIC6[x]
            pricelist1_2 = C.DIC5[x]

        return dict(
            pricelist1_1=pricelist1_1,
            pricelist1_2=pricelist1_2,
            b=b,

        )

    def before_next_page(player: Player, timeout_happened):  # calculate payoff
        p = player.participant
        if player.round_number == C.NUM_ROUNDS:
            p.a = random.randint(0, player.round_number - 1)  # randomly select a investment decision
            s = player.session
            p.dec = p.decision[p.a]
            numberchart = s.liste[player.id_in_group - 1][p.a]  # save picture number of selected round
            p.returns = round(C.DIC7[p.dec][numberchart - 1] * 100,
                              2)  # calculate payoff ->use matrix in which in the left column payoff of the high score chart is saved
            returns2 = 1 + C.DIC7[p.dec][numberchart - 1]
            p.wealth = round(returns2 * 1000, 2)
            p.payoff = p.wealth * 0.0005  # save payoff in participant field so that participant can get the variable payout
        else:
            p.payoff = 0
            #note -> decision is 0 if the concave path is chosen and 1 otherwise -> in the first column of DIC7 the payoffs of the concave paths are saved


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    def is_displayed(player: Player):

        if player.round_number == C.NUM_ROUNDS:
            return True
        else:
            return False

    def vars_for_template(player: Player):
        p = player.participant
        b = p.a + 1
        wealth = p.wealth
        returns = p.returns
        x = p.payoff


        return dict(
            b=b,
            returns=returns,
            wealth=wealth,
            x=cu(x),
            z=x + cu(2),
            y=2
        )


page_sequence = [MyPage, MyPage2, MyPage3, MyPage4, Results]
