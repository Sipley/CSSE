import math

#values = {'op':'correct'}


#class Values(object):
#    def __init__(self, op=None):
#        self.op = op


#result = Values(**values)
#print result.op

values={'op':'correct','lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}


class Values(object):
    def __init__(self, lat, long, altitude, assumedLat, assumedLong, op=None):
        self.op = op
        self.lat = lat
        self.long = long
        self.altitude = altitude
        self.assumedLat = assumedLat
        self.assumedLong = assumedLong

    def convert(self):
        latDeg = convertAngleFromDeg(self.lat)
        longDeg = convertAngleFromDeg(self.long)
        altitudeDeg = convertAngleFromDeg(self.altitude)
        assumedLatDeg = convertAngleFromDeg(self.assumedLat)
        assumedLongDeg = convertAngleFromDeg(self.assumedLong)

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

def calcIntDist(values):
    A = math.sin(math.radians(Values(**values).latDeg))
    B = math.sin(math.radians(Values(**values).assumedLatDeg))
    C = math.cos(math.radians(Values(**values).latDeg))
    D = math.cos(math.radians(Values(**values).assumedLatDeg))
    E = math.cos(convertAngleFromDeg(calcLHA(values)))
    return A
    return B
    return C
    return D
    return E

result = calcIntDist(values)
print result
