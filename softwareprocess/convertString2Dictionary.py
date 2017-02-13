"""
    Created to convert url-encoded string 2 dictionary
    Baselined:  2017-02-13

    @author:    Breanna Sipley
"""
import re
import urllib


def convertString2Dictionary(inputString=''):
    errorDict = {'error':'true'}
    inputString = str(inputString)
    string = urllib.unquote(inputString)
    output = []
    # test for illegal char
    if not re.match('^[A-Za-z0-9=/., ]*$', string):
        return errorDict
    if re.match('.*[=,]$', string):
        return errorDict
    # test for at least 1 key=value pair
    if '=' not in string:
        return errorDict
    # remove valid whitespace if present
    string = string.replace('= ', '=')
    string = string.replace(', ', ',')
    # test for embedded whitespace
    if ' ' in string:
        return errorDict
    # for each pair, split key & value
    for key in string.split(','):
        output.append(key.split('='))
    # test for duplicate key
    listKey = [key[0] for key in output]
    dupKeyChecker = list(set(listKey))
    if len(listKey) != len(dupKeyChecker):
        return errorDict
    # test key 2+ characters, begin with alpha
    for key in listKey:
        if len(key) < 2:
            return errorDict
        if not key[0].isalpha():
            return errorDict
    # check for each key having a value
    listValue = [value[1] for value in output]
    for value in listValue:
        if len(value) < 1:
            return errorDict
    # create dictionary
    outputValue = dict(output)
    return outputValue
