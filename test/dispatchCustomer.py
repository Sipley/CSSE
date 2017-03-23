

import softwareprocess.dispatch as dispatch
sighting = {'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
result = dispatch.dispatch(sighting)
print result

'''
import re
observation = '10d1.1'

if re.match('\d+d\d+\.\d', observation):
    print 'yes'
else:
    print 'no'
'''

'''
test = '12d'
left = test.split('d')[0]
right = test.split('d')[1]
print left
print len(right)

'''
'''
print '%dd%.1f' %(12, 12.5)
'''
'''
%d integer
%1.3f (float d.ddd)
%s string
'''
