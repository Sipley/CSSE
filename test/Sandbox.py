#values = {'op':'correct'}


#class Values(object):
#    def __init__(self, op=None):
#        self.op = op


#result = Values(**values)
#print result.op

values={'op':'correct','lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}


class Values(object):
    def __init__(self, op=None, lat=None, long=None, altitude=None, assumedLat=None, assumedLong=None):
        self.op = op
        self.lat = lat
        self.long = long
        self.altitude = altitude
        self.assumedLat = assumedLat
        self.assumedLong = assumedLong

#result = Values(**values)
#print result.lat

def checkDict(values):
    result = Values(**values)
    return result.lat

result = checkDict(values)
print result
