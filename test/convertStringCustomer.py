import softwareprocess.convertString2Dictionary as cs2d
import urllib

# convert human-readable key=value to percent-encoded string
inputValue = urllib.quote("key1=value, key2=value")
# convert percent-encoded string to dictionary
outputValue = cs2d.convertString2Dictionary(inputString = inputValue)
# iterate through keys, print key and corresponding value
for key in outputValue.keys():
    print('key={0}, value={1}'.format(key, outputValue[key]))
