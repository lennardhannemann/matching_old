from otree.api import Currency as c, currency_range, expect, Bot, SubmissionMustFail
from . import *
from otree.models import Participant, Session


class PlayerBot(Bot):

    def play_round(player:Player):
        p = player.participant
        if p.treat ==0 or p.treat==1:
            yield MyPage, dict(decision=0)
            yield MyPage2, dict(likert_scale=1)
        else:
            yield MyPage3, dict(decision=0)
            yield MyPage4, dict(likert_scale=1)

