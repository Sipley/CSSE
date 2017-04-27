import unittest
import softwareprocess.prod.dispatch as DP

class MyTestCase(unittest.TestCase):
    def test900_010_shouldReturnErrorMissingInfo(self):
        values={'op':'correct'}
        expectedResult={'op':'correct','error':'mandatory information is missing'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_020_shouldReturnErrorMissingInfo(self):
        values={'op':'correct', 'long':'95d41.6', 'altitude':'13d42.4', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'long':'95d41.6', 'altitude':'13d42.4', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'mandatory information is missing'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_030_shouldReturnErrorInvLat(self):
        values={'op':'correct','lat':'16.0d32.3', 'long':'95.41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct','lat':'16.0d32.3', 'long':'95.41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'invalid lat'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_040_shouldReturnErrorInvAssumedLat(self):
        values={'op':'correct','lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-153d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct','lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-153d38.4', 'assumedLong':'74d35.3', 'error':'invalid assumedLat'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_050_shouldReturnErrorNoLong(self):
        values={'op':'correct', 'lat': '16d32.3', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'mandatory information is missing'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_060_shouldReturnErrorNoAlt(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'mandatory information is missing'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_070_shouldReturnErrorNoAssumedLat(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3','assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3','assumedLong':'74d35.3', 'error':'mandatory information is missing'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_080_shouldReturnErrorNoAssumedLong(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'error':'mandatory information is missing'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_090_shouldReturnErrorInvLong(self):
        values={'op':'correct','lat':'16d32.3', 'long':'-1d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct','lat':'16d32.3', 'long':'-1d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'invalid long'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_100_shouldReturnErrorInvLong(self):
        values={'op':'correct','lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct','lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'invalid long'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_110_shouldReturnErrorInvLong(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'360d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'360d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'invalid long'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_120_shouldReturnErrorInvLong(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95.0d41.6', 'altitude':'13d42.3','assumedLong':'74d35.3','assumedLat':'-53d38.4'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95.0d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'invalid long'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_130_shouldReturnErrorInvLat(self):
        values={'op':'correct', 'lat': '-90d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '-90d32.3', 'long':'95d41.6', 'altitude':'13d42.3','assumedLong':'74d35.3','assumedLat':'-53d38.4', 'error':'invalid lat'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_140_shouldReturnErrorInvLat(self):
        values={'op':'correct', 'lat': '90d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '90d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'invalid lat'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_150_shouldReturnErrorInvLat(self):
        values={'op':'correct', 'lat': '89d-32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '89d-32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'invalid lat'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_160_shouldReturnErrorInvLat(self):
        values={'op':'correct', 'lat': '90d60.0', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '90d60.0', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3','error':'invalid lat'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_170_shouldReturnErrorInvLat(self):
        values={'op':'correct', 'lat': '8960.0', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '8960.0', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3','error':'invalid lat'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'1342.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'1342.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'invalid altitude'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'0d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'0d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'invalid altitude'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'90d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'90d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'invalid altitude'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13.0d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13.0d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3','error':'invalid altitude'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d-1.0', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d-1.0', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3','error':'invalid altitude'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d60.0', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3','error':'invalid altitude'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

if __name__ == '__main__':
    unittest.main()
