import math
import re
import datetime
import calendar


def dispatch(values=None):
    # Validate parm
    if (values == None):
        return {'error': 'parameter is missing'}
        return values
    if (not (isinstance(values, dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not ('op' in values)):
        values['error'] = 'no op is specified'
        return values

    # Perform designated function
    if (values['op'] == 'adjust'):
        if (not ('observation' in values) or (values['observation'] == '')):
            values['error'] = 'mandatory information is missing'
            return values
        if ('altitude' in values):
            values['error'] = 'altitude already exists'
            return values
        observation = values['observation']
        if re.match('\d+d\d+\.\d$', observation):
            altitude = int(observation.split('d')[0])
            degrees = float(observation.split('d')[1])
            if ((not (0 <= altitude < 90)) or not (0 <= degrees < 60) or (altitude == degrees == 0)):
                values['error'] = 'observation is invalid'
                return values
            if ('height' in values):
                if not (re.match('\d+\.*\d*$', values['height'])):
                    values['error'] = 'height is invalid'
                    return values
            if ('temperature' in values):
                try:
                    int(values['temperature'])
                except ValueError:
                    values['error'] = 'temperature is invalid'
                    return values
                if not (-20 <= int(values['temperature']) <= 120):
                    values['error'] = 'temperature is invalid'
                    return values
            if ('pressure' in values):
                try:
                    int(values['pressure'])
                except ValueError:
                    values['error'] = 'pressure is invalid'
                    return values
                if not (100 <= int(values['pressure']) <= 1100):
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
            dip = -0.97 * math.sqrt(float(height)) / 60
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
            refraction3 = math.tan(math.radians(altitude + (degrees / 60)))
            refraction = round((refraction1 / refraction2 / refraction3), 3)
            altitudeAdjusted = (altitude + (degrees / 60)) + dip + refraction
            altitudeAdjustedNew = int(altitudeAdjusted // 1)
            altitudeAdjustedDegrees = round(float((altitudeAdjusted % 1) * 60), 1)
            altitudeRounded = str(altitudeAdjustedNew) + 'd' + str(altitudeAdjustedDegrees)
            values['altitude'] = altitudeRounded
            return values
        else:
            values['error'] = 'observation is invalid'
        return values
    elif (values['op'] == 'predict'):
        if not ('body' in values):
            values['error'] = 'mandatory information is missing'
            return values
        body = values['body']
        if not (body.lower() in Stars.starsInsensitive):
            values['error'] = 'star not in catalog'
            return values
        if 'date' in values:
            date = values['date']
            try:
                datetime.datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                values['error'] = 'invalid date'
                return values
        if 'time' in values:
            time = values['time']
            try:
                datetime.datetime.strptime(time, '%H:%M:%S')
            except ValueError:
                values['error'] = 'invalid time'
                return values
        if ('lat' or 'long') in values:
            values['error'] = 'lat and/or long already in dict'
            return values

        index = Stars.starsInsensitive.index(body.lower())
        latitude = Stars.declination[index]
        values['lat'] = latitude
        SHA = Stars.siderealHour[index]
        GHAstar = calcAmtRotAries(values) + convertAngleFromDeg2(SHA)
        while GHAstar > 360:
            GHAstar = GHAstar - 360
        values['long'] = convertAngleToDeg(GHAstar)

        return values
    elif (values['op'] == 'correct'):

        if not (all(key in values for key in ['lat', 'long', 'altitude', 'assumedLat', 'assumedLong'])):
            values['error'] = 'mandatory information is missing'
            return values
        if 'correctedDistance' in values:
            values['error'] = 'correctedDistance and/or correctedAzimuth already present'
            return values
        if 'correctedAzimuth' in values:
            values['error'] = 'correctedDistance and/or correctedAzimuth already present'
            return values

        lat = values['lat']
        long = values['long']
        altitude = values['altitude']
        assumedLat = values['assumedLat']
        assumedLong = values['assumedLong']

        if not (re.match('\-*\d+d\d+\.\d$', lat)):
            values['error'] = 'invalid lat'
            return values
        degreeLat = int(lat.split('d')[0])
        arcminuteLat = float(lat.split('d')[1])
        if not (isinstance(degreeLat, int)):
            values['error'] = 'invalid lat'
            return values
        if not (isinstance(arcminuteLat, float)):
            values['error'] = 'invalid lat'
            return values
        if not (-90 < degreeLat < 90):
            values['error'] = 'invalid lat'
            return values
        if not (0 <= arcminuteLat < 60.0):
            values['error'] = 'invalid lat'
            return values

        if not (re.match('\d+d\d+\.\d$', long)):
            values['error'] = 'invalid long'
            return values
        degreeLong = int(long.split('d')[0])
        arcminuteLong = float(long.split('d')[1])
        if not (isinstance(degreeLong, int)):
            values['error'] = 'invalid long'
            return values
        if not (isinstance(arcminuteLong, float)):
            values['error'] = 'invalid long'
            return values
        if not (0 <= degreeLong < 360):
            values['error'] = 'invalid long'
            return values

        if not (re.match('\d+d\d+\.\d$', altitude)):
            values['error'] = 'invalid altitude'
            return values
        degreeAlt = int(altitude.split('d')[0])
        arcminuteAlt = float(altitude.split('d')[1])
        if not (isinstance(degreeAlt, int)):
            values['error'] = 'invalid altitude'
            return values
        if not (isinstance(arcminuteAlt, float)):
            values['error'] = 'invalid altitude'
            return values
        if not (0 < degreeAlt < 90):
            values['error'] = 'invalid altitude'
            return values
        if not (0 <= arcminuteAlt < 60.0):
            values['error'] = 'invalid altitude'
            return values

        if not (re.match('\-*\d+d\d+\.\d$', assumedLat)):
            values['error'] = 'invalid assumedLat'
            return values
        degreeAssumedLat = int(assumedLat.split('d')[0])
        arcminuteAssumedLat = float(assumedLat.split('d')[1])
        if not (isinstance(degreeAssumedLat, int)):
            values['error'] = 'invalid assumedLat'
            return values
        if not (isinstance(arcminuteAssumedLat, float)):
            values['error'] = 'invalid assumedLat'
            return values
        if not (-90 < degreeAssumedLat < 90):
            values['error'] = 'invalid assumedLat'
            return values
        if not (0 <= arcminuteAssumedLat < 60.0):
            values['error'] = 'invalid assumedLat'
            return values

        if not (re.match('\d+d\d+\.\d$', assumedLong)):
            values['error'] = 'invalid assumedLong'
            return values
        degreeAssumedLong = int(assumedLong.split('d')[0])
        arcminuteAssumedLong = float(assumedLong.split('d')[1])
        if not (isinstance(degreeAssumedLong, int)):
            values['error'] = 'invalid assumedLong'
            return values
        if not (isinstance(arcminuteAssumedLong, float)):
            values['error'] = 'invalid assumedLong'
            return values
        if not (0 < degreeAssumedLong < 360):
            values['error'] = 'invalid assumedLong'
            return values
        if not (0 <= arcminuteAssumedLong < 60.0):
            values['error'] = 'invalid assumedLong'
            return values

        values['correctedDistance'] = str(calcCorrectedAlt(values))
        values['correctedAzimuth'] = str(calcCorrectedAzimuth(values))
        return values

    elif (values['op'] == 'locate'):
        return values  # This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values


class Stars():
    def __init__(self):
        pass

    stars = ['Alpheratz', 'Ankaa', 'Schedar', 'Diphda', 'Achernar', 'Hamal', 'Polaris', 'Akamar', 'Menkar', 'Mirfak',
             'Aldebaran', 'Rigel', 'Capella', 'Bellatrix', 'Elnath', 'Alnilam', 'Betelgeuse', 'Canopus', 'Sirius',
             'Adara', 'Procyon', 'Pollux', 'Avior', 'Suhail', 'Miaplacidus', 'Alphard', 'Regulus', 'Dubhe', 'Denebola',
             'Gienah', 'Acrux', 'Gacrux', 'Alioth', 'Spica', 'Alcaid', 'Hadar', 'Menkent', 'Arcturus', 'Rigil Kent.',
             'Zubenelg.', 'Kochab', 'Alphecca', 'Antares', 'Atria', 'Sabik', 'Shaula', 'Rasalhague', 'Etamin',
             'Kaus Aust.', 'Vega', 'Nunki', 'Altair', 'Peacock', 'Deneb', 'Enif', 'Alnair', 'Fomalhaut', 'Scheat',
             'Markab']
    starsInsensitive = [star.lower() for star in stars]
    declination = ['29d10.9', '-42d13.4', '56d37.7', '-17d54.1', '-57d09.7', '23d32.3', '89d20.1', '-40d14.8', '4d09.0',
                   '49d55.1', '16d32.3', '-8d11.3', '46d00.7', '6d21.6', '28d37.1', '-1d11.8', '7d24.3', '-52d42.5',
                   '-16d44.3', '-28d59.9', '5d10.9', '27d59.0', '-59d33.7', '-43d29.8', '-69d46.9', '-8d43.8',
                   '11d53.2', '61d39.5', '14d28.9', '-17d37.7', '-63d10.9', '-57d11.9', '55d52.1', '-11d14.5',
                   '49d13.8', '-60d26.6', '-36d26.6', '19d06.2', '-60d53.6', '-16d06.3', '74d05.2', '26d39.7',
                   '-26d27.8', '-69d03.0', '-15d44.4', '-37d06.6', '12d33.1', '51d29.3', '-34d22.4', '38d48.1',
                   '-26d16.4', '8d54.8', '-56d41.0', '45d20.5', '9d57.0', '-46d53.1', '-29d32.3', '28d10.3', '15d17.6']
    siderealHour = ['357d41.7', '353d14.1', '349d38.4', '348d54.1', '335d25.5', '327d58.7', '316d41.3', '315d16.8',
                    '314d13.0', '308d37.4', '290d47.1', '281d10.1', '280d31.4', '278d29.8', '278d10.1', '275d44.3',
                    '270d59.1', '263d54.8', '258d31.7', '255d10.8', '244d57.5', '243d25.2', '234d16.6', '222d50.7',
                    '221d38.4', '217d54.1', '207d41.4', '193d49.4', '182d31.8', '175d50.4', '173d07.2', '171d58.8',
                    '166d19.4', '158d29.5', '152d57.8', '148d45.5', '148d05.6', '145d54.2', '139d49.6', '137d03.7',
                    '137d21.0', '126d09.9', '112d24.4', '107d25.2', '102d10.9', '96d20.0', '96d05.2', '90d45.9',
                    '83d41.9', '80d38.2', '75d56.6', '62d06.9', '53d17.2', '49d30.7', '33d45.7', '27d42.0', '15d22.4',
                    '13d51.8', '13d36.7']

def convertAngleFromDeg2(angle):
    degree = angle.split('d')[0]
    arcminute = float(angle.split('d')[1]) / 60
    convertedAngle = abs(float(degree)) + arcminute
    if '-' in degree:
        convertedAngle = -convertedAngle
    return convertedAngle

def convertAngleToDeg(angle):
    angle = str(angle)
    degree = angle.split('.')[0]
    arcminute = round((abs(float(angle)) - abs(int(degree))) * 60, 1)
    convertedAngle = str(degree) + 'd' + str(arcminute)
    return convertedAngle

def calcCumProgression(values):
    GHAariesAnnualDecrease = '-0d14.31667'
    date = '2001-01-01'
    if 'date' in values:
        date = values['date']
    obsYear = datetime.datetime.strptime(date, '%Y-%m-%d').year
    diffYear = obsYear - 2001
    cumProgression = diffYear * convertAngleFromDeg2(GHAariesAnnualDecrease)
    return cumProgression

def calcNumLeapYear(values):
    date = '2001-01-01'
    if 'date' in values:
        date = values['date']
    obsYear = datetime.datetime.strptime(date, '%Y-%m-%d').year
    numLeapYear = 0
    for year in range(2001, obsYear):
        if calendar.isleap(year):
            numLeapYear += 1
    return numLeapYear

def calcTotalLeapProg(values):
    rotPeriod = 86164.1
    clockPeriod = 86400
    dailyDeg = convertAngleFromDeg2('360d0.00')
    dailyRot = abs(dailyDeg - (rotPeriod / clockPeriod * dailyDeg))
    totalLeapProg = calcNumLeapYear(values) * dailyRot
    return totalLeapProg

def calcTotalSeconds(values):
    refYear = 2001

    date = '2001-01-01'
    if 'date' in values:
        date = values['date']
    time = '00:00:00'
    if 'time' in values:
        time = values['time']
    obsYear = datetime.datetime.strptime(date, '%Y-%m-%d').year
    refDate = str(obsYear) + '-01-01' + ' ' + '00:00:00'
    obsDate = date + ' ' + time
    refDateDate = datetime.datetime.strptime(refDate, '%Y-%m-%d %H:%M:%S')
    obsDateDate = datetime.datetime.strptime(obsDate, '%Y-%m-%d %H:%M:%S')
    deltaSeconds = (obsDateDate - refDateDate).total_seconds()
    return deltaSeconds

def calcAmtRot(values):
    rotPeriod = 86164.1
    amtRot = calcTotalSeconds(values) / rotPeriod * 360
    while amtRot > 360:
        amtRot = amtRot - 360
    return amtRot

def calcAmtRotAries(values):
    GHAaries = '100d42.6'
    GHAariesObs = convertAngleFromDeg2(GHAaries) + calcCumProgression(values) + calcTotalLeapProg(values)
    GHAariesTotal = GHAariesObs + calcAmtRot(values)
    return GHAariesTotal

class Values(object):
    def __init__(self, lat, long, altitude, assumedLat, assumedLong, op=None, correctedDistance=None):
        self.op = op
        self.lat = convertAngleFromDeg2(lat)
        self.long = convertAngleFromDeg2(long)
        self.altitude = convertAngleFromDeg2(altitude)
        self.assumedLat = convertAngleFromDeg2(assumedLat)
        self.assumedLong = convertAngleFromDeg2(assumedLong)

def calcLHA(values):
    LHA = Values(**values).long + Values(**values).assumedLong
    LHAdeg = convertAngleToDeg(LHA)
    return LHAdeg

def calcIntDist(values):
    A = math.sin(math.radians(Values(**values).lat))
    B = math.sin(math.radians(Values(**values).assumedLat))
    C = math.cos(math.radians(Values(**values).lat))
    D = math.cos(math.radians(Values(**values).assumedLat))
    E = math.cos(math.radians(convertAngleFromDeg2(calcLHA(values))))
    intDist = (A * B) + (C * D * E)
    return intDist

def calcCorrectedAlt(values):
    correctedAlt = math.degrees(math.asin(calcIntDist(values)))
    correctDistance = (Values(**values).altitude - correctedAlt) * 60
    return int(round(correctDistance))

def calcCorrectedAzimuth(values):
    A = math.sin(math.radians(Values(**values).lat))
    B = math.sin(math.radians(Values(**values).assumedLat))
    C = calcIntDist(values)
    D = math.cos(math.radians(Values(**values).assumedLat))
    E = math.cos(math.asin(calcIntDist(values)))
    correctedAzimuth = math.acos((A - (B * C))/(D * E))
    return convertAngleToDeg(math.degrees(correctedAzimuth))
