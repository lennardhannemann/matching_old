from otree.api import Currency as c, currency_range, expect, Bot, SubmissionMustFail
from . import *


class PlayerBot(Bot):

    def play_round(self):
        yield Submission(MyPage, {'question1': 1, 'question2': 1, 'question3': 1})
