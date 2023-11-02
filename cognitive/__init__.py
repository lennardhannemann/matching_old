import posix

from otree.api import *
import time

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'cognitive'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    REDIRECTLINK = 'https: // app.prolific.co / submissions / complete?cc = [COMPLETION CODE]'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question1 = models.IntegerField(label="", blank=True)
    question2 = models.IntegerField(label="", blank=True)
    question3 = models.IntegerField(label="", blank=True)
    time_check = models.FloatField(blank=True)

    feedback = models.StringField(label="", blank=True)




# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['question1', 'question2', 'question3', 'time_check']

    @staticmethod
    def error_message(player, value):
        x = value['question1']
        y = value['question2']
        z = value['question3']

        if x == None or y == None or z == None:
            return 'Please answer all the questions!'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        p = player.participant
        player.time_check = time.time() - p.time


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    form_model = 'player'
    form_fields = ['feedback']

    def vars_for_template(player: Player):
        p = player.participant
        b = p.a + 1
        wealth = round(p.wealth, 2)
        returns = p.returns
        returns2 = round(1 + p.returns/100, 2)
        x = p.payoff
        o = p.dec*1000
        o2 = 1000 - o
        link = C.REDIRECTLINK

        return dict(
            b=b,
            returns=returns,
            returns2 =returns2,
            wealth=wealth,
            x=cu(x),
            z=x + cu(1.5),
            y=2,
            o = o,
            o2 = o2,
            link=link
        )


page_sequence = [MyPage, Results]
