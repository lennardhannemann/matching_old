import random
import time

from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'financialliteracy'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question1 = models.IntegerField(label="Suppose you had £100 in a savings account and the interest rate was 2 percent per year. After 5 years, how much do you think you would have in the account if you left the money to grow?",
                                       widget=widgets.RadioSelectHorizontal,
                                       choices=[
                                           [1, 'More than £102'],
                                           [2, 'exactly £102'],
                                           [3, 'less than £102'],
                                           [4, 'do not know']
                                       ],
                                    blank=True)
    question2 = models.IntegerField(
        label="Suppose you had £100 in a savings account and the interest rate is 20 percent per year and you never withdraw money or interest payments. After 5 years, how much would you have on this account in total? ",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, 'More than £200'],
            [2, 'exactly £200'],
            [3, 'less than £200'],
            [4, 'do not know']
             ],
            blank=True)
    question3 = models.IntegerField(
        label="Imagine that the interest rate on your savings account was 1 percent per year and inflation was 2 percent per year. After 1 year, how much would you be able to buy with the money in this account? ",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, 'More than today'],
            [2, 'exactly as much as today'],
            [3, 'less than today'],
            [4, 'do not know']
        ],
        blank=True)

    question4 = models.IntegerField(
        label="Asumme a friend inherits £10,000 today and his sibling inherits £10,000 3 years from now. Who is richer because of the inheritance? ",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, 'My friend'],
            [2, 'his sibling'],
            [3, 'they are equally rich'],
            [4, 'do not know']
        ],
        blank=True)

    question5 = models.IntegerField(
        label='To show that you are paying attention, please select "Less than one year".',
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, 'More than one year'],
            [2,'Less than one year'],
            [3,'Exactly one year'],
            [4, 'do not know'],


        ],
        blank=True
    )

    time_check = models.FloatField(blank=True)


# PAGES
class MyPage(Page):
    form_model ='player'
    form_fields = ['question1', 'question2', 'question3','question4', 'question5', 'time_check']
    @staticmethod
    def error_message(player, value):
        w = value['question1']
        x = value['question2']
        y = value['question3']
        z = value['question4']
        a = value['question5']

        if w==None or x==None or y==None or z==None or a==None:

            return 'Please select an option for all questions!'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        p = player.participant
        player.time_check = time.time() - p.time
        p.time = time.time()

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):


    pass

page_sequence = [MyPage]
