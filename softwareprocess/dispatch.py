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
        observation = values['observation']
        if re.match('\d+d\d+\.\d$', observation):
            altitude = int(observation.split('d')[0])
            degrees = float(observation.split('d')[1])
            if(not(0 <= altitude < 90)):
                values['error'] = 'observation is invalid'
                return values
            if(not(0 <= degrees < 60)):
                values['error'] = 'observation is invalid'
                return values
            if(altitude == degrees == 0):
                values['error'] = 'observation is invalid'
                return values
        else:
            values['error'] = 'observation is invalid'
        if ('height' in values):
            if not(re.match('\d+\.*\d*$', values['height'])):
                values['error'] = 'height is invalid'
                return values
        if ('temperature' in values):
            try: int(values['temperature'])
            except ValueError:
                values['error'] = 'temperature is invalid'
                return values
            if not(-20 <= int(values['temperature']) <= 120):
                values['error'] = 'temperature is invalid'
        if ('pressure' in values):
            try: int(values['pressure'])
            except ValueError:
                values['error'] = 'pressure is invalid'
                return values
            if not(100 <= int(values['pressure']) <= 1100):
                values['error'] = 'pressure is invalid'
                return values
        if ('horizon' in values):
            if(values['horizon'] != ('artificial' or 'Artificial' or 'natural' or 'Natural')):
                values['error'] = 'horizon is invalid'
                return values
    #    if values['horizon'] == ('artificial' or 'Artificial'):
    #        dip = 0
    #    if 'horizon' not in values:
    #        values['horizon'] == 'natural'
    #    if 'height' not in values:
    #        values['height'] == '0'
    #    if 'pressure' not in values:
    #        values['pressure'] == '1010'
    #    if 'temperature' not in values:
    #        values['temperature'] == '72'
    #    if values['horizon'] == ('natural' or 'Natural'):
    #        dip = -0.97 * sqrt(values['height'])/60
    #    refraction1 = -0.00452 * values['pressure']
    #    refraction2 = 273 + values['temperature']
    #    refraction3 = tan(altitude)
    #    refraction = refraction1/refraction2/refraction3
    #    values['altitude'] = refraction
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
