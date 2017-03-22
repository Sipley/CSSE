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

# SAD PATH

    def test900_010_shouldReturnErrorNoOp(self):
        sighting = {}
        result = dispatch.dispatch(sighting)
        expectedResult = {'error':'no op is specified'}
        self.assertDictEqual(result, expectedResult)
'''
    def test900_020_shouldReturnErrorNotDict(self):
        sighting = hello
        result = dispatch.dispatch(sighting)
        expectedResult = {'error': 'parameter is not a dictionary'}
'''
