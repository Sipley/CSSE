values = {'op':'correct'}


class Values(object):
    def __init__(self, op=None):
        self.op = op


result = Values(**values)
print result.op
