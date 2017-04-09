import unittest

import softwareprocess.prod.dispatch as DP

class dispatchPredict(unittest.TestCase):

##############ACCEPTANCE TESTS##############
#body should be string
#body should match "stars"
#body should be case-insensitive
#MANDATORY
#
#date string
#date format yyyy-mm-dd
#2001 >= yyyy >= 2100
#01 <= mm <= 12
#00 <= dd <= 31
#optional
#defaults to 2001-01-01
#
#time string
#time format hh:mm:ss
#00 <= hh <= 24
#00 <= mm <= 59
#00 <= ss <= 59
#time <= 24:00:00
#time <= 23:59:00
#time <= 23:59:59
#
#if lat &/or long exist, return error

####happy path
    def test100_010_shouldReturnPredictLatLong(self):
        values={'op':'predict','body':'Betelgeuse','date':'2016-01-17','time':'03:15:42'}
        expectedResult={'op':'predict','body':'Betelgeuse','date':'2016-01-17','time':'03:15:42','long':'75d53.6','lat':'7d24.3'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test100_010_shouldReturnAngleConvertedFromDeg(self):
        angle = '100d42.6'
        expectedResult = 100.71
        self.assertEqual(DP.convertAngleFromDeg(angle),expectedResult)

    def test100_020_shouldReturnAngleConvertedToDeg(self):
        angle = 100.71
        expectedResult = '100d42.6'
        self.assertEqual(DP.convertAngleToDeg(angle),expectedResult)

    def test100_030_shouldReturnCumProg(self):
        values = {'op':'predict','body':'Betelgeuse','date':'2016-01-17','time':'03:15:42'}
        expectedResult = -3.5791675
        self.assertEqual(DP.calcCumProgression(values),expectedResult)

    def test100_040_shouldReturnNumLeapYear(self):
        values = {'op':'predict','body':'Betelgeuse','date':'2016-01-17','time':'03:15:42'}
        expectedResult = 3
        self.assertEqual(DP.calcNumLeapYear(values),expectedResult)

    def test100_050_shouldReturnTotalLeapProg(self):
        values = {'op':'predict','body':'Betelgeuse','date':'2016-01-17','time':'03:15:42'}
        expectedResult = 2.94875
        self.assertAlmostEqual(DP.calcTotalLeapProg(values),expectedResult,10)

####sad path

    def test900_010_shouldReturnErrorMissingInfo(self):
        values={'op':'predict'}
        expectedResult={'op':'predict','error':'mandatory information is missing'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_020_shouldReturnErrorInvalidStar(self):
        values={'op':'predict','body':'unknown','date':'2016-01-17','time':'03:15:42'}
        expectedResult={'op':'predict','body':'unknown','date':'2016-01-17','time':'03:15:42','error':'star not in catalog'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_030_shouldReturnErrorInvalidDate(self):
        values={'op':'predict','body':'Betelgeuse','date':'2016-99-17','time':'03:15:42'}
        expectedResult={'op':'predict','body':'Betelgeuse','date':'2016-99-17','time':'03:15:42','error':'invalid date'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_040_shouldReturnErrorInvalidTime(self):
        values={'op':'predict','body':'Betelgeuse','date':'2016-01-17','time':'03:99:42'}
        expectedResult={'op':'predict','body':'Betelgeuse','date':'2016-01-17','time':'03:99:42','error':'invalid time'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_040_shouldReturnErrorLatLongInDict(self):
        values={'op':'predict','body':'Betelgeuse','date':'2016-01-17','time':'03:15:42','long':'75d53.6','lat':'7d24.3'}
        expectedResult={'op':'predict','body':'Betelgeuse','date':'2016-01-17','time':'03:15:42','long':'75d53.6','lat':'7d24.3','error':'lat and/or long already in dict'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

if __name__ == '__main__':
    unittest.main()
