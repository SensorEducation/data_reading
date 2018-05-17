import unittest

from read_all import testTemperature, testPressure, testHumidity

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestData(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testTemperatureInBoun(self): 
        self.assertEqual(testTemperature(50), True,'54 F is in bounds')

    def testTemperatureOutOfBoundsUpper(self): 
        self.assertEqual(testTemperature(190), False,'190 F is out of bounds')

    def testTemperatureOutOfBoundsLower(self): 
        self.assertEqual(testTemperature(-50), False,'-50 F is out of bounds')

    def testPressureInBounds(self): 
        self.assertEqual(testPressure(1000), True,'1000 hPa is in bounds')

    def testPressureOutOfBoundsUpper(self): 
        self.assertEqual(testPressure(100), False,'120 hPa is out of bounds')

    def testPressureOutOfBoundsLower(self): 
        self.assertEqual(testPressure(10), False,'10 hPa is out of bounds')

    def testHumidityInBounds(self): 
        self.assertEqual(testHumidity(20),True,'20% is in bounds')

    def testHumidityOutOfBoundsUpper(self): 
        self.assertEqual(testHumidity(110),False,'110% is out of bounds')

    def testHumidityOutOfBoundsLower(self): 
        self.assertEqual(testHumidity(-100),False,'-100% is out of bounds')

    '''
    def testGasInBounds(self): 
        self.assertEqual(testGas()),'In Bounds','54 F is in bounds')

    def testGasOutOfBoundsUpper(self): 
        self.assertEqual(testGas(120),'Out Bounds','120 F is out of bounds')

    def testGasOutOfBoundsLower(self): 
        self.assertEqual(testGas(-10),'Out Bounds','120 F is out of bounds')
    '''


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
