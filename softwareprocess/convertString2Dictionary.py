"""
    Created to convert url-encoded string 2 dictionary
    Baselined:  YYYY-MM-DD

    @author:    Breanna Sipley
"""

def convertString2Dictionary(inputString = ''):
    import re
    import urllib
    errorDict = {'error':'true'}
    string = urllib.unquote(inputString)
    output = []
    #test for illegal sep
    if not re.match('^[A-Za-z0-9=/., ]*$', string):
        return errorDict
    #test for non-empty input
    elif len(string) <= 1:
        return errorDict
    #test for presence of 1+ key=value pair
    elif "=" not in string:
        return errorDict
    #test for alpha first char
    elif not string[0].isalpha():
        return errorDict
    #remove legal whitespace
    string = string.replace('= ','=')
    string = string.replace(', ',',')
    #test for embedded whitespace
    if ' ' in string:
        return errorDict
    #for each pair, split key & value
    for key in string.split(','):
        output.append(key.split('='))
    #test for duplicate key
    listKey = [key[0] for key in output]
    isDupKey = list(set(listKey))
    if listKey != isDupKey:
        return errorDict
    #create dictionary
    outputValue = dict(output)
    #test for non-empty values
    if outputValue.values() == ['']:
        return errorDict
    return outputValue
