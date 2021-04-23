import unittest
import datetime

from lunar_python import Lunar


def 咦():
    today = datetime.datetime.today()
    lunar = Lunar.fromYmd(today.year, today.month, today.day)
    # return '诸事不宜' not in lunar.getTimeJi()
    return False


class _(unittest.TestCase):
    def test(self):
        assert 咦(), '今日诸事不宜！'
