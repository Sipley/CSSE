import unittest
import softwareprocess.prod.dispatch as DP

class MyTestCase(unittest.TestCase):
    def test100_010_shouldReturnErrorMissingInfo(self):
        values={'op':'correct'}
        expectedResult={'op':'correct','error':'mandatory information is missing'}
        self.assertDictEqual(DP.dispatch(values),expectedResult)


if __name__ == '__main__':
    unittest.main()
