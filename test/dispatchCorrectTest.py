import unittest
import softwareprocess.prod.dispatch as DP

class MyTestCase(unittest.TestCase):

############happy path tests############

    def test100_010_shouldReturnLHA(self):
        values={'op':'correct','lat':'89d20.1','long':'154d5.4','altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d35.3'}
        expectedResult='228d40.7'
        self.assertEqual(DP.calcLHA(values), expectedResult)

    def test100_020_shouldReturnIntDistance(self):
        values={'op':'correct','lat':'89d20.1','long':'154d5.4','altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d35.3'}
        expectedResult=0.581474846
        self.assertAlmostEqual(DP.calcIntDist(values), expectedResult,2)

    def test100_030_shouldResultCorrectedDist(self):
        values={'op':'correct','lat':'89d20.1','long':'154d5.4','altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d35.3'}
        expectedResult=104
        self.assertAlmostEquals(DP.calcCorrectedAlt(values),expectedResult,0)

    def test100_040_shouldReturnCorrectedAzi(self):
        values={'op':'correct','lat':'89d20.1','long':'154d5.4','altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d35.3'}
        expectedResult='0d36.8'
        self.assertAlmostEquals(DP.calcCorrectedAzimuth(values),expectedResult)

    def test100_050_shouldReturnDisAndAziInValues(self):
        values={'op':'correct','lat':'89d20.1','long':'154d5.4','altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d35.3'}
        expectedResult={'op':'correct','lat':'89d20.1','long':'154d5.4','altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d35.3','correctedDistance':'104','correctedAzimuth':'0d36.8'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test100_060_shouldReturnCorrect(self):
        values={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d35.3', 'correctedDistance':'104','correctedAzimuth':'0d36.8'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test100_070_shouldReturnCorrect2(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'correctedDistance':'3950', 'correctedAzimuth':'164d42.9'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test100_080_shouldReturnIntDistance(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult=-0.789410565
        self.assertAlmostEqual(DP.calcIntDist(values), expectedResult)

    def test100_090_shouldReturnCorrectDist2(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult=3950
        self.assertEqual(DP.calcCorrectedAlt(values), expectedResult)

    def test100_100_shouldReturnCorrectedAzi(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult='164d42.9'
        self.assertAlmostEquals(DP.calcCorrectedAzimuth(values),expectedResult)

############sad path tests##############

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

    def test900_180_shouldReturnErrorInvAlt(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'1342.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'1342.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'invalid altitude'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_190_shouldReturnErrorInvAlt(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'0d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'0d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'invalid altitude'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_200_shouldReturnErrorInvAlt(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'90d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'90d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'invalid altitude'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_210_shouldReturnErrorInvAlt(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13.0d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13.0d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3','error':'invalid altitude'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_220_shouldReturnErrorInvAlt(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d-1.0', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d-1.0', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3','error':'invalid altitude'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_230_shouldReturnErrorInvAlt(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d100.0', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d100.0', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'error':'invalid altitude'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_240_shouldReturnErrorInvAssumedLat(self):
        values={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'-90d59.7','assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'-90d59.7','assumedLong':'74d35.3','error':'invalid assumedLat'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_250_shouldReturnErrorInvAssumedLat(self):
        values={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'90d59.7','assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'90d59.7','assumedLong':'74d35.3','error':'invalid assumedLat'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_260_shouldReturnErrorInvAssumedLat(self):
        values={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'35.0d59.7','assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'35.0d59.7','assumedLong':'74d35.3','error':'invalid assumedLat'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_270_shouldReturnErrorInvAssumedLat(self):
        values={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'35d-59.7','assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'35d-59.7','assumedLong':'74d35.3','error':'invalid assumedLat'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_280_shouldReturnErrorInvAssumedLong(self):
        values={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d60.0'}
        expectedResult={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d60.0','error':'invalid assumedLong'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_290_shouldReturnErrorInvAssumedLat(self):
        values={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'3559.7','assumedLong':'74d35.3'}
        expectedResult={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'3559.7','assumedLong':'74d35.3','error':'invalid assumedLat'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_300_shouldReturnErrorInvassumedLong(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74.0d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74.0d35.3', 'error':'invalid assumedLong'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_310_shouldReturnErrorInvassumedLong(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35', 'error':'invalid assumedLong'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_320_shouldReturnErrorInvassumedLong(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'7435.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'7435.3','error':'invalid assumedLong'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_330_shouldReturnErrorInvassumedLong(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'-74d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'-74d35.3','error':'invalid assumedLong'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_340_shouldReturnErrorInvassumedLong(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'360d35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'360d35.3','error':'invalid assumedLong'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_350_shouldReturnErrorInvassumedLong(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d-35.3'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d-35.3','error':'invalid assumedLong'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_360_shouldReturnErrorInvassumedLong(self):
        values={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d60.0'}
        expectedResult={'op':'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d60.0','error':'invalid assumedLong'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_370_shouldReturnErrorAlreadyThere(self):
        values={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d35.3','correctedDistance':'93d209.1'}
        expectedResult={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d35.3','correctedDistance':'93d209.1','error':'correctedDistance and/or correctedAzimuth already present'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_380_shouldReturnErrorAlreadyThere(self):
        values={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d35.3','correctedAzimuth':'93d209.1'}
        expectedResult={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d35.3','correctedAzimuth':'93d209.1','error':'correctedDistance and/or correctedAzimuth already present'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)

    def test900_390_shouldReturnErrorAlreadyThere(self):
        values={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d35.3','correctedAzimuth':'93d209.1','correctedDistance':'93d023.1'}
        expectedResult={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d35.3','correctedAzimuth':'93d209.1','correctedDistance':'93d023.1','error':'correctedDistance and/or correctedAzimuth already present'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)


if __name__ == '__main__':
    unittest.main()
