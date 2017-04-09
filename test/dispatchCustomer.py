

import softwareprocess.prod.dispatch as DP
values = {'observation': '45d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}

result = DP.dispatch(values)
print result
