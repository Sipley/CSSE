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

    def test100_030_shouldReturnErrorInvLat(self):
        values={'op':'correct','lat':'16.0d32.3', 'long':'95.41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct','lat':'16.0d32.3', 'long':'95.41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'invalid lat'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test100_040_shouldReturnErrorInvAssumedLat(self):
        values={'op':'correct','lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-153d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct','lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-153d38.4', 'assumedLong':'74d35.3', 'error':'invalid assumedLat'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test100_050_shouldReturnErrorNoLong(self):
        values={'op':'correct', 'lat': '16d32.3', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'mandatory information is missing'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test100_060_shouldReturnErrorNoAlt(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult=

if __name__ == '__main__':
    unittest.main()
