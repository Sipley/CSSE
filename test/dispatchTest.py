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

    def test100_030_shouldReturnDefaultParameters(self):
        sighting = {'op':'adjust','observation':'test'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'op':'adjust','observation':'test','height':'0','pressure':'1010','temperature':'72'}
        self.assertDictEqual(result, expectedResult)

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
        expectedResult = {'error':'mandatory information is missing'}
        self.assertDictEqual(result, expectedResult)

    def test900_080_shouldReturnErrorNoObs(self):
        sighting = {'op':'adjust','observation':''}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'mandatory information is missing'}
        self.assertDictEqual(result, expectedResult)

    def test900_090_shouldReturnErrorAltExists(self):
        sighting = {'altitude':'45d11.9','op':'adjust','observation':'45d15.2','height':'6','horizon':'natural','pressure':'1010','temperature':'71'}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'altitude already exists','altitude':'45d11.9','op':'adjust','observation':'45d15.2','height':'6','horizon':'natural','pressure':'1010','temperature':'71'}
        self.assertDictEqual(result, expectedResult)
