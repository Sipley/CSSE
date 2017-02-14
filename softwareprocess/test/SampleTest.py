from unittest import TestCase
import softwareprocess.Sample as S

class SampleTest(TestCase):
    pass

#---------------
#--- Acceptance tests
#    100 constructor
#       Desired level of confidence:    Boundary Value Analysis
#       Input/Output analysis:
#           input:  n -> integer .GE. 2 and .LT. 30, mandatory, unvalidated
#           output: instance of Sample
#       Happy path analysis:
#           n:  nominal value       4   expected result:    instance of Sample
#               low bound       2   expected result:    instance of Sample
#               high bound      29  expected result:    instance of Sample
#       Sad path analysis:
#           n:  non-int n       4.2 expected result:    exception
#           n:  out of bounds n     1   expected result:    exception
#           n:  out of bounds n     30  expected result:    exception
#           n is missing        missing n   expected result:    exception
#
#   Happy path
    def test100_010_ShouldConstructInstanceWithNominalValue(self):
        self.assertIsInstance(S.Sample(4),S.Sample)

    def test100_020_ShouldConstructInstanceWithLowBound(self):
        myS = S.Sample(2)
        self.assertIsInstance(myS,S.Sample)
        self.assertEquals(myS.getN(), 2)
        #want to get number of degrees of freedom.
        #would like to get n back & see if equal to 2
        #red light: no attritube 'n'
        #bad smell violating n

    def test100_020_ShouldConstructInstanceWithHighBound(self):
        myS = S.Sample(29)
        self.assertIsInstance(myS,S.Sample)
        self.assertEquals(myS.getN(), 29)
