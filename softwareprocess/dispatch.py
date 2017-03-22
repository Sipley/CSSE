import math
import re

def dispatch(values=None):

    #Validate parm
    if(values == None):
        return {'error':'parameter is missing'}
        return values
    if(not(isinstance(values,dict))):
        return {'error':'parameter is not a dictionary'}
    if(not('op' in values)):
        values['error'] = 'no op is specified'
        return values

    #Perform designated function
    if(values['op'] == 'adjust'):
        if(not('observation' in values) or (values['observation'] == '')):
            values['error'] = 'mandatory information is missing'
            return values
        if('altitude' in values):
            values['error'] = 'altitude already exists'
            return values
#        if(not('height' in values) or (values['height'] == '')):
#            values['height'] = '0'
#        if(not('horizon' in values) or (values['horizon'] != 'natural' or 'Natural' or 'artificial' or 'Artificial')):
#            values['horizon'] = 'natural'
#        if(not('pressure' in values) or (values['pressure'] == '')):
#            values['pressure'] = '1010'
#        if(not('temperature' in values) or (values['temperature'] == '')):
#            values['temperature'] = '72'
        observation = values['observation']
        if re.match('\d+d\d+\.\d', observation):
            altitude = int(observation.split('d')[0])
            degrees = float(observation.split('d')[1])
            if(not(0 <= altitude < 90)):
                values['error'] = 'observation is invalid'
            if(not(0 <= degrees < 60)):
                values['error'] = 'observation is invalid'
        else:
            values('error') = 'observation is invalid'
 #           elif(altitude >= 90):
 #               values['error'] = 'observation is invalid'
 #       else:
 #           values['error'] = 'observation is invalid'
        return values    #<-------------- replace this with your implementation
    elif(values['op'] == 'predict'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values
