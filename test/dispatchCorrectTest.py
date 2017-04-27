import unittest
import softwareprocess.prod.dispatch as DP

class MyTestCase(unittest.TestCase):
    def test100_010_shouldReturnErrorMissingInfo(self):
        values={'op':'correct'}
        expectedResult={'op':'correct','error':'mandatory information is missing'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test100_020_shouldReturnErrorMissingInfo(self):
        values={'op':'correct', 'long':'95d41.6', 'altitude':'13d42.4', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'long':'95d41.6', 'altitude':'13d42.4', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'mandatory information is missing'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

if __name__ == '__main__':
    unittest.main()
