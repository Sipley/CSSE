from unittest import TestCase
import softwareprocess.Sample as S
import math

class SampleTest(TestCase):
    pass
'''
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
'''
'''
    #if __name__ == '__main__':
    def test100_910_ShouldRaiseExceptionOnMissingN(self):
                #decide what string going to raise
                #'invalid n'
        expectedString = "Sample.__init__:  invalid n"
                #want to raise an exception with name of class & name of method that raises exception
        with self.assertRaises(ValueError) as context:
                #within next statements, should raise value error.  If doesn't, bad
                #if does, good
                #and if does, should assign to variable called context
                #now instantiate
            myS = S.Sample()
        self.assertEqual(expectedString, context.exception.args[0][0:len(expectedString)])
                #if doesn't, fail right here & gimme red light
                #check to make sure that argument problem is string
                #red light
                #good, is red light
                #now, let's write production code to fix this


            #boundary level analysis.  So want to have tests that test boundaries
            #look at nominal value.  Then lower boundary & upper boundary
            #HAPPY PATH == nominal operation of software.  Normal stuff w/o delving into any problem areas
                #only thing we have going in is n
                #start with nominal value (e.g., 4)
                #expected result: get instance of sample
                #also want to expect boundary (e.g., 2 & 29)
                #but wait, what are we trying to accomplish there
            #SAD PATH == something that could arise
                #what happens if n is not an integer?
                #Need to check n
                #Is it there?
                #Is it an integer?
                #Also boundaries
            #when being: want failing test case
                #want to fail first time around, but we want it to provide us some information
                #construct test case that will take us a little further
                #ask what isn't there, then it'll give us some info, so we can add production code
                #ran okay, but we expected red light, but got green light
                #couldn't differ btwn n of 2 versus 4
                #add in a method to test whether it works
            #we're gonna stay away from void functions: functions that return nothing
                #we want to return something
                #will give us more info than if we got nothing back
            #added my.S, S.sample, but didn't tell us anything
                #so we added getN, & that was cool
            #then we started on Sad path
                #what happened if we leave n out?
                #we said, if this happens, then we expect exception to be raised
                #if raised, assign to variable called context, then peel off string to see whether it's actually what we want
            #now, let's work on bounds


        #want to exercise BDD.  what behavior do we want to drive this?
            #we want to raise an exception should n be out of bounds

            def test100_920_ShouldRaiseExceptionOnLowN(self):
                expectedString = "Sample.__init__: invalid n"
                with self.assertRaises(ValueError) as context:
                    myS = S.Sample(1)
                self.assertEqual(expectedString, context.exception.args[0][0:len(expectedString)])

            def test100_930_ShouldRaiseExceptionOnNonIntN(self):
                expectedString = "Sample.__init__: invalid n"
                with self.assertRaises(ValueError) as context:
                    myS = S.Sample(1)
                self.assertEqual(expectedString, context.exception.args[0][0:len(expectedString)])

'''
'''
#-------
#---- Acceptance tests

# Happy path tests
    if __name__ == '__main__':
        if __name__ == '__main__':
            def test200_010_ShouldCalculatePWithNominalT(self):
                myS = S.Sample(6)
                self.assertAlmostEquals(myS.p(1.4398,1), 0.9, 3)
                #we need to find the answer first
                #retrieved from t-distribution guides resource
                #This is different than if working with function we don't know the answer to
                #so, for 6 degrees of freedom: 1.4398.  If one with 1 tail, should get .9.  If 2 tails should get .8
                #this would test for 0.9 exactly, but we're not going to get that back, since this is an approx to begin with
                #so need to adjust code to almost equals rather than equals
                #need to put number of digits of accuracy
                #how do we decide number of digits?  Ask the customer.  What is amount of accuracy?
                #not something i decide.  Something customer decides
                #NOTE:  THIS IS AN ACCEPTANCE TEST.
                #acceptance test: an outward facing method.  & for those we test those with acceptance tests
                #customer says 3 (after .9)
                #we know we're done after we have enough Happy test & sad tests to satisfy boundary level analysis

    #WE SHOULD HAVE 10 HAPPY PATH TESTS
        #1 tail
            # nominal value
            #low t, low n
            #low t, high n
            #high t, low n
            #high t, high n
        #2 tail
            # nominal value
            #low t, low n
            #low t, high n
            #high t, low n
            #high t, high n
        #Determined from that table
'''
#-------
#--- 300 gamma
#       inputs: x -> numeric
#       output: float
#
#   Happy path analysis
#       input
#           x:

    def test300_010_ShouldReturn1(self):
        self.assertEquals(S.gamma(1), 1)
        self.assertEquals(myS.gamma(1), 1)



