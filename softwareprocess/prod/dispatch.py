import math
import re
import datetime

class Stars():
    def __init__(self, body, SiderealHourAngle, Declination):
        self.SiderealHourAngle = SiderealHourAngle
        self.Declination = Declination

    stars = {'Alpheratz', 'Ankaa', 'Schedar', 'Diphda', 'Achernar', 'Hamal', 'Polaris', 'Akamar', 'Menkar', 'Mirfak', 'Aldebaran', 'Rigel', 'Capella', 'Bellatrix', 'Elnath','Alnilam','Betelgeuse','Canopus','Sirius','Adara','Procyon','Pollux','Avior','Suhail','Miaplacidus','Alphard','Regulus','Dubhe','Denebola','Gienah','Acrux','Gacrux','Alioth','Spica','Alcaid','Hadar','Menkent','Arcturus','Rigil Kent.','Zubenelg.','Kochab','Alphecca','Antares','Atria','Sabik','Shaula','Rasalhague','Etamin','Kaus Aust.','Vega','Nunki','Altair','Peacock','Deneb','Enif','Alnair','Fomalhaut','Scheat','Markab'}
    declination= {'29d10.9','-42d13.4','56d37.7','-17d54.1','-57d09.7','23d32.3','89d20.1','-40d14.8','4d09.0','49d55.1','16d32.3','-8d11.3','46d00.7','6d21.6','28d37.1','-1d11.8','7d24.3','-52d42.5','-16d44.3','-28d59.9','5d10.9','27d59.0','-59d33.7','-43d29.8','-69d46.9','-8d43.8','11d53.2','61d39.5','14d28.9','-17d37.7','-63d10.9','-57d11.9','55d52.1','-11d14.5','49d13.8','-60d26.6','-36d26.6','19d06.2','-60d53.6','-16d06.3','74d05.2','26d39.7','-26d27.8','-69d03.0','-15d44.4','-37d06.6','12d33.1','51d29.3','-34d22.4','38d48.1','-26d16.4','8d54.8','-56d41.0','45d20.5','9d57.0','-46d53.1','-29d32.3','28d10.3','15d17.6'}

   # def findAngRelAries(body)

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
            if((not(0 <= altitude < 90)) or not(0 <= degrees < 60) or (altitude == degrees == 0)):
                values['error'] = 'observation is invalid'
                return values
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
                    return values
            if ('pressure' in values):
                try: int(values['pressure'])
                except ValueError:
                    values['error'] = 'pressure is invalid'
                    return values
                if not(100 <= int(values['pressure']) <= 1100):
                    values['error'] = 'pressure is invalid'
                    return values
            if 'horizon' in values:
                if values['horizon'] == 'natural':
                    pass
                elif values['horizon'] == 'Natural':
                    pass
                elif values['horizon'] == 'artificial':
                    pass
                elif values['horizon'] == 'Artificial':
                    pass
                else:
                    values['error'] = 'horizon is invalid'
                    return values

            height = 0
            if 'height' in values:
                height = values['height']
            dip = -0.97 * math.sqrt(float(height))/60
            if ('horizon' in values) and (values['horizon'] == ('artificial' or 'Artificial')):
                dip = 0
            pressure = '1010'
            if 'pressure' in values:
                pressure = values['pressure']
            temperature = '72'
            if 'temperature' in values:
                temperature = values['temperature']
            refraction1 = -0.00452 * int(pressure)
            refraction2 = 273 + int(temperature)
            refraction3 = math.tan(math.radians(altitude + (degrees/60)))
            refraction = round((refraction1/ refraction2 / refraction3),3)
            altitudeAdjusted = (altitude + (degrees/60)) + dip + refraction
            altitudeAdjustedNew = int(altitudeAdjusted // 1)
            altitudeAdjustedDegrees = round(float((altitudeAdjusted % 1)*60),1)
            altitudeRounded = str(altitudeAdjustedNew)+'d'+str(altitudeAdjustedDegrees)
            values['altitude'] = altitudeRounded
            return values
        else:
            values['error'] = 'observation is invalid'
        return values
    elif(values['op'] == 'predict'):
        if not('body' in values):
            values['error'] = 'mandatory information is missing'
            return values
        body = values['body']
        if not(body in Stars.stars):
            values['error'] = 'star not in catalog'
            return values
        if 'date' in values:
            date = values['date']
            try:
                datetime.datetime.strptime(date,'%Y-%m-%d')
            except ValueError:
                values['error'] = 'invalid date'
                return values
        if 'time' in values:
            time = values['time']
            try:
                datetime.datetime.strptime(time,'%H:%M:%S')
            except ValueError:
                values['error'] = 'invalid time'
                return values
        if ('lat' or 'long') in values:
            values['error'] = 'lat and/or long already in dict'
            return values
        index = Stars.stars.index('Betelgeuse')
        dec = Star.stars.declination[index]
        latitude = dec
        values['lat'] = latitude
        return values
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values


