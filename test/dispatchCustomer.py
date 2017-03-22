import softwareprocess.dispatch as dispatch
sighting = {'op':'adjust', 'observation':'015d04.9', 'height':'6.0', 'temperature':'72','pressure':'1010', 'horizon':'artificial'}
result = dispatch.dispatch(sighting)
