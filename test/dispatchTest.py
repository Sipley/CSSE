import unittest
import math

import softwareprocess.dispatch as dispatch

class dispatchTest(unittest.TestCase):

########ACCEPTANCE TESTS###########
# dictionary containing 1(+) key-value pairs
# 'op' necessary key
# 'op' value must be either 'adjust','predict','correct','locate'
#
# If 'op' = 'adjust' then:
#   'observation' must be present
#   'height' optional default to 0
#   'horizon' optional default to 'natural'
#   'pressure' optional default to 1010
#   'temp' optional default to 72
#   'altitude' not already present
#   calculate adjusted altitude
#   return values + altitude
#
# Else: report error + values

# on dispatch parameters
#
# HAPPY PATH
#
# If input {'op': 'predict'}, return {'op': 'predict'}

 #   def test100_010_shouldReturnResultOfAdjust(self):
 #       sighting = {'op':'adjust', 'observation':'015d04.9', 'height':'6.0', 'temperature':'72','pressure':'1010', 'horizon':'artificial'}
 #       result = dispatch.dispatch(sighting)
 #       self.assertDictEqual(sighting, result)

    def test100_010_shouldReturnValuesOpPredict(self):
        sighting = {'op':'predict'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'op':'predict'}
        self.assertDictEqual(result, expectedResult)

    #def test100_020_shouldReturnSplitObservation(self):
    #    sighting = {'op':'adjust','observation':'25d50.0'}
    #    expectedAltitude = 25
    #    expectedDegrees = 50.0
    #    altitude = altitude.get(dispatch.dispatch(sighting))
    #    degrees = degrees.get(dispatch.dispatch(sighting))
    #    self.assertEquals(altitude, expectedAltitude)
    #    self.assertEquals(degrees, expectedDegrees)

  #  def test100_030_shouldReturnDefaultParameters(self):
  #      sighting = {'op':'adjust','observation':'50d50.0'}
  #      result = dispatch.dispatch(sighting)
  #      expectedResult = {'op':'adjust','observation':'50d50.0','height':'0','pressure':'1010','temperature':'72','horizon':'natural'}
  #      self.assertDictEqual(result, expectedResult)

# SAD PATH

    def test900_010_shouldReturnErrorNoOp(self):
        sighting = {}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'no op is specified'}
        self.assertDictEqual(result, expectedResult)

    def test900_020_shouldReturnErrorParameterMissing(self):
        result = dispatch.dispatch()
        expectedResult = {'error': 'parameter is missing'}
        self.assertDictEqual(result, expectedResult)

    def test900_030_shouldReturnErrorNotDict(self):
        sighting = 42
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'parameter is not a dictionary'}
        self.assertDictEqual(result, expectedResult)

    def test900_040_shouldReturnErrorNoOp(self):
        sighting = {'height':'100'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'no op is specified','height':'100'}
        self.assertDictEqual(result, expectedResult)

    def test900_050_shouldReturnErrorIllegalOp(self):
        sighting = {'op':'unknown'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'op':'unknown','error':'op is not a legal operation'}
        self.assertDictEqual(result, expectedResult)

    def test900_060_shouldReturnErrorParameterMissing(self):
        sighting = {'op':''}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error': 'op is not a legal operation', 'op':''}
        self.assertDictEqual(result, expectedResult)

    def test900_070_shouldReturnValuesNoObs(self):
        sighting = {'op':'adjust'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'mandatory information is missing','op':'adjust'}
        self.assertDictEqual(result, expectedResult)

    def test900_080_shouldReturnErrorNoObs(self):
        sighting = {'op':'adjust','observation':''}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'mandatory information is missing', 'op':'adjust','observation':''}
        self.assertDictEqual(result, expectedResult)

    def test900_090_shouldReturnErrorAltExists(self):
        sighting = {'altitude':'45d11.9','op':'adjust','observation':'45d15.2','height':'6','horizon':'natural','pressure':'1010','temperature':'71'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'altitude already exists','altitude':'45d11.9','op':'adjust','observation':'45d15.2','height':'6','horizon':'natural','pressure':'1010','temperature':'71'}
        self.assertDictEqual(result, expectedResult)

    def test900_100_shouldReturnErrorInvalidObsInt(self):
        sighting = {'op':'adjust','observation':'80.1d0.0'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'observation is invalid','op':'adjust','observation':'80.1d0.0'}
        self.assertDictEqual(result, expectedResult)

    def test900_110_shouldReturnErrorInvalidObsString(self):
        sighting = {'op':'adjust','observation':'string'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'observation is invalid','op':'adjust','observation':'string'}
        self.assertDictEqual(result, expectedResult)

    def test900_120_shouldReturnErrorInvalidObsNoMin(self):
        sighting = {'op':'adjust','observation':'0'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'observation is invalid','op':'adjust','observation':'0'}
        self.assertDictEqual(result, expectedResult)

    def test900_130_shouldReturnErrorInvalidObsNeg(self):
        sighting = {'op':'adjust','observation':'-1d0.0'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'observation is invalid','op':'adjust','observation':'-1d0.0'}
        self.assertDictEqual(result, expectedResult)

    def test900_140_shouldReturnErrorObsWhiteSpace(self):
        sighting = {'op':'adjust','observation':'059.0'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'observation is invalid','op':'adjust','observation':'059.0'}
        self.assertDictEqual(result, expectedResult)

    def test900_150_shouldReturnErrorObsMinNeg(self):
        sighting = {'op':'adjust','observation':'0d-1.0'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'observation is invalid','op':'adjust','observation':'0d-1.0'}
        self.assertDictEqual(result, expectedResult)

    def test900_160_shouldReturnErrorObsAltBig(self):
        sighting = {'op':'adjust','observation':'90d0.0'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'observation is invalid','op':'adjust','observation':'90d0.0'}
        self.assertDictEqual(result, expectedResult)

    def test900_170_shouldReturnErrorObsMinBig(self):
        sighting = {'op':'adjust','observation':'0d60.0'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'observation is invalid','op':'adjust','observation':'0d60.0'}
        self.assertDictEqual(result, expectedResult)

    def test900_180_shouldReturnErrorInvalidHeight(self):
        sighting = {'op':'adjust','observation':'0d0.1','height':'string'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'height is invalid','op':'adjust','observation':'0d0.1','height':'string'}
        self.assertDictEqual(result, expectedResult)

    def test900_190_shouldReturnErrorInvalidTemp(self):
        sighting = {'op':'adjust','observation':'0d0.1','temperature':'-21'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'temperature is invalid','op':'adjust','observation':'0d0.1','temperature':'-21'}
        self.assertDictEqual(result, expectedResult)

    def test900_200_shouldReturnErrorInvalidTemp(self):
        sighting = {'op':'adjust','observation':'0d0.1','temperature':'121'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'temperature is invalid','op':'adjust','observation':'0d0.1','temperature':'121'}
        self.assertDictEqual(result, expectedResult)

    def test900_210_shouldReturnErrorInvalidTemp(self):
        sighting = {'op':'adjust','observation':'0d0.1','temperature':'72.5'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'temperature is invalid','op':'adjust','observation':'0d0.1','temperature':'72.5'}
        self.assertDictEqual(result, expectedResult)

    def test900_220_shouldReturnErrorInvalidTemp(self):
        sighting = {'op':'adjust','observation':'0d0.1','temperature':'string'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'temperature is invalid','op':'adjust','observation':'0d0.1','temperature':'string'}
        self.assertDictEqual(result, expectedResult)

    def test900_230_shouldReturnErrorInvalidP(self):
        sighting = {'op':'adjust','observation':'0d0.1','pressure':'99'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'pressure is invalid','op':'adjust','observation':'0d0.1','pressure':'99'}
        self.assertDictEqual(result, expectedResult)

    def test900_240_shouldReturnErrorInvalidP(self):
        sighting = {'op':'adjust','observation':'0d0.1','pressure':'1101'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'pressure is invalid','op':'adjust','observation':'0d0.1','pressure':'1101'}
        self.assertDictEqual(result, expectedResult)

    def test900_250_shouldReturnErrorInvalidP(self):
        sighting = {'op':'adjust','observation':'0d0.1','pressure':'1010.5'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'pressure is invalid','op':'adjust','observation':'0d0.1','pressure':'1010.5'}
        self.assertDictEqual(result, expectedResult)

    def test900_260_shouldReturnErrorInvalidP(self):
        sighting = {'op':'adjust','observation':'0d0.1','pressure':'string'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'pressure is invalid','op':'adjust','observation':'0d0.1','pressure':'string'}
        self.assertDictEqual(result, expectedResult)

    def test900_270_shouldReturnErrorInvalidHorizon(self):
        sighting = {'op':'adjust','observation':'0d0.1','horizon':'unknown'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'horizon is invalid','op':'adjust','observation':'0d0.1','horizon':'unknown'}
        self.assertDictEqual(result, expectedResult)

    def test900_280_shouldReturnErrorInvalidHorizon(self):
        sighting = {'op':'adjust','observation':'0d0.1','horizon':'1000'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'horizon is invalid','op':'adjust','observation':'0d0.1','horizon':'1000'}
        self.assertDictEqual(result, expectedResult)

    def test900_290_shouldReturnErrorDupAlt(self):
        sighting = {'altitude':'45d11.9','op':'adjust','observation':'45d15.2','height':'6','horizon':'natural','pressure':'1010','temperature':'71'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'altitude already exists','altitude':'45d11.9','op':'adjust','observation':'45d15.2','height':'6','horizon':'natural','pressure':'1010','temperature':'71'}
        self.assertDictEqual(result, expectedResult)

    def test900_300_shouldResturnErrorObsNothing(self):
        sighting = {'op':'adjust','observation':'0d0.0'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'observation is invalid','op':'adjust','observation':'0d0.0'}
        self.assertDictEqual(result, expectedResult)

    def test900_310_shouldReturnErrorObsBig(self):
        sighting = {'observation': '101d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'observation': '101d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71', 'error':'observation is invalid'}
        self.assertDictEqual(result, expectedResult)

    def test900_320_shouldReturnErrorBadH(self):
        sighting = {'observation': '45d15.2', 'height': 'a', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'observation': '45d15.2', 'height': 'a', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71', 'error':'height is invalid'}
        self.assertDictEqual(result, expectedResult)

    def test900_330_shouldReturnErrorBadHorizon(self):
        sighting = {'observation': '45d15.2', 'height': '6', 'horizon': '   ', 'pressure': '1010', 'op': 'adjust', 'temperature': '71'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'observation': '45d15.2', 'height': '6', 'horizon': '   ', 'pressure': '1010', 'op': 'adjust', 'temperature': '71', 'error':'horizon is invalid'}
        self.assertDictEqual(result, expectedResult)

    def test900_340_shouldReturnErrorNegHeight(self):
        sighting = {'op':'adjust','observation':'0d0.1','height':'-1'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'height is invalid','op':'adjust','observation':'0d0.1','height':'-1'}
        self.assertDictEqual(result, expectedResult)

    def test900_350_shouldReturnErrorDegreeNotFloat(self):
        sighting = {'op':'adjust','observation':'0d1'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'observation is invalid','op':'0d1}
        self.assertDictEqual(result, expectedResult)
