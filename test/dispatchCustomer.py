import softwareprocess.dispatch as dispatch
sighting = {'altitude':'45d11.9','op':'adjust','observation':'45d15.2','height':'6','horizon':'natural','pressure':'1010','temperature':'71'}
result = dispatch.dispatch(sighting)
print result



