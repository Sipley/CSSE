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

####sad path

    def test900_010_shouldReturnErrorMissingInfo(self):
        values={'op':'predict'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test900_020_shouldReturnErrorInvalidStar(self):
        values=
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    
if __name__ == '__main__':
    unittest.main()
