import math

#values = {'op':'correct'}


#class Values(object):
#    def __init__(self, op=None):
#        self.op = op


#result = Values(**values)
#print result.op

values={'op':'correct','lat':'89d20.1','long':'154d5.4','altitude':'37d17.4','assumedLat':'35d59.7','assumedLong':'74d35.3'}


class Values(object):
    def __init__(self, lat, long, altitude, assumedLat, assumedLong, op=None):
        self.op = op
        self.lat = convertAngleFromDeg(lat)
        self.long = convertAngleFromDeg(long)
        self.altitude = convertAngleFromDeg(altitude)
        self.assumedLat = convertAngleFromDeg(assumedLat)
        self.assumedLong = convertAngleFromDeg(assumedLong)

#def checkDict(values):
#    result = Values(**values).lat
#    return result

def convertAngleFromDeg(angle):
    degree = angle.split('d')[0]
    arcminute = float(angle.split('d')[1]) / 60
    convertedAngle = float(degree) + arcminute
    if '-' in degree:
        convertedAngle = -convertedAngle
    return convertedAngle

def calcLHA(values):
    LHA = Values(**values).long + Values(**values).assumedLong
  #  LHAdeg = convertAngleToDeg(LHA)
    return LHA

def calcIntDist(values):
    A = math.sin(math.radians(Values(**values).lat))
    B = math.sin(math.radians(Values(**values).assumedLat))
    C = math.cos(math.radians(Values(**values).lat))
    D = math.cos(math.radians(Values(**values).assumedLat))
    E = math.cos(calcLHA(values))
    intDist = (A * B) + (C * D * E)
    return intDist

result = calcIntDist(values)
print result
