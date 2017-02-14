import softwareprocess.convertString2Dictionary as cs2d
import urllib

# convert human-readable key=value to percent-encoded string
inputValue = urllib.quote('key1=value1,key2=value2')
# convert percent-encoded string to dictionary
outputValue = cs2d.convertString2Dictionary(inputString=inputValue)
# iterate through keys, print key and corresponding value
for key in outputValue.keys():
    print('key={0}, value={1}'.format(key, outputValue[key]))

'''testing
#these should pass
goodString = 'abc%3D123'
goodString2 = 'function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse'

#these should fail
inputIllegal = 'function%20%3D%20get_stars'
inputDupKey = 'key%3Dvalue%2C%20key%3Dvalue'
inputMissingValue = 'key%3D'
inputMissingKey = 'value'
inputKeyInvalid = '1key%3Dvalue'
inputBlankChar = 'k%20e%20y%20%3D%20value'
inputNo = ''
inputIllegalSep = 'key1%3Dvalue%3B%20key2%3Dvalue'
'''


