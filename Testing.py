import unittest
from dayoftheweek import DayOfTheWeek
class TestDayOfTheWeek(unittest.TestCase):
    def testinitwithabbreviation(self):
        d = DayOfTheWeek(F)
        self.assertEquals(d.name(), Friday)
        d = DayOfTheWeek(Th)
        self.assertEquals(d.name(), Thursday)
unittest.main()