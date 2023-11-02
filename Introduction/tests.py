from otree.api import Currency as c, currency_range, expect, Bot, SubmissionMustFail
from . import *


class PlayerBot(Bot):

    def play_round(self):
        yield General
        yield Investment
        yield Payout