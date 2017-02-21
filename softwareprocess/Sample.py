import math
class Sample(object):

# outward facing methods
    def __init__(self, n=None):
        functionName = "Sample.__init__: "
        if(n == None):
            raise ValueError(functionName + "invalid n")
        if(not(isinstance(n, int))):
            raise ValueError(functionName + "invalid n")
        if((n < 2) or (n >= 30)):
            raise ValueError(functionName + "invalid n")
        self.n = n

    def getN(self):
        return self.n


    def p(self, t=None, tails=1):
        functionName = "Sample.p: "
        if(t == None):
            raise ValueError(functionName + "missing t")
        if(not(isinstance(t, float))):
            raise ValueError(functionName + "invalid t")
        if(t < 0.0):
            raise ValueError(functionName + "invalid t")

        if(not(isinstance(tails, int))):
            raise ValueError(functionName + "invalid tails")
        if((tails != 1) & (tails != 2)):
            raise ValueError(functionName + "invalid tails")

        constant = self.calculateConstant(self.n)
        integration = self.integrate(t, self.n, self.f)
        if(tails == 1):
            result = constant * integration + 0.5
        else:
            result = constant * integration * 2

        if(result > 1.0):
            raise ValueError(functionName + "result > 1.0")

        return result

# internal methods
    def gamma(self, x):
        if(x == 1):
            return 1
        if(x == 0.5):
            return math.sqrt(math.pi)
        return (x - 1) * self.gamma(x - 1)

    def calculateConstant(self, n):
        n = float(n)
        numerator = self.gamma((n + 1.0) / 2.0)
        denominator = self.gamma(n / 2.0) * math.sqrt(n * math.pi)
        result = numerator / denominator
        return result

    def f(self, u, n):
        n = float(n)
        base = (1 + (u ** 2) / n)
        exponent = -(n + 1.0) / 2
        result = base ** exponent
        return result

    #def f(self, u, n):
    #    n = float(n)
    #    return u

#    def getF(self):
#        return self.f

#    def integrate(self, t, n, f=None):
#        if f is None:
#            f = self.f
#        epsilon = 0.001
#        sOld = 0
#        sNew = epsilon
#        s = 4.0
#        while (abs((sNew - sOld)/ sNew )) > epsilon:
#            sOld = sNew
#            sNew = f(0.0, n) + f(t, n)
#            w = (t - 0.0)/s
#            term = 1
#            while term < s:
#                if term % 2 == 0:
#                    sNew += 2 * f(0.0 + term * w, n)
#                else:
#                    sNew += 4 * f(0.0 + term * w, n)
#                term += 1
#            sNew *= w / 3
#            s = s * 2
#        return sNew

    def integrate(self, lowBound, highBound, n, f):
        slices = 4
        w = (highBound - lowBound) / slices
        simpsonNew = f(lowBound, n)
        simpsonNew += 4.0 * f(lowBound + 1.0 * w, n) + \
                        2.0 * f(lowBound + 2.0 * w, n) + \
                        4.0 * f(lowBound + 3.0 * w, n)
        simpsonNew += f(highBound, n)
        simpsonNew *= w / 3
        return simpsonNew
