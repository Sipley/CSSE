values = {'op':'correct'}


class Values(values):
    def __init__(self, values):
        if "op" in values:
            self.op = op
        else:
            return "error"

result = Values(values)
print result
