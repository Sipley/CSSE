values = {'op':'correct'}


class Values(object):
    def __init__(self, op, lat, long, altitude, assumedLat, assumedLong):
        self.op = op
        self.lat = lat
        self.long = long
        self.altitude = altitude
        self.assumedLat = assumedLat
        self.assumedLong = assumedLong

result = Values(**values)
print result
