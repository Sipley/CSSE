'''
From unittest import TestCase
import math

import softwareprocess.dispatch as dispatch

class dispatchTest(TestCase):

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

    def test100_010_shouldReturnResultOfPredict(self):
        input = {'op':'predict'}
        expectedResult = {'op':'predict'}
        self.assertDictEqual(dispatch(input), expectedResult)
'''
