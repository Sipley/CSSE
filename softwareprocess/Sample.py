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
        integration = self.integrate(0.0, t, self.n, self.f)
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

    #def f(self, u, n):
    #    n = float(n)
    #    base = (1 + (u ** 2) / n)
    #    exponent = -(n + 1.0) / 2
    #    result = base ** exponent
    #    return result

    def f(self, u, n):
        n = float(n)
        return u


    '''
    def integrate(self, lowerBound, upperBound, n, f):
        n = float(n)
        epsilon = .001
        simpsonOld = 0.0
        simpsonNew = epsilon
        S=4
        while (abs((simpsonNew - simpsonOld)/simpsonNew) > epsilon):
            w=(upperBound-lowerBound)/S
            simpsonNew = (w/3) * (f(lowerBound, n) + 4(f(lowerBound + w, n)) + \
               2*(f(lowerBound + 2 * w,n)) + 4*(f(lowerBound + 3 * w, n)) + 2*(f(lowerBound + 4 * w, n))
                   ... + 4(f(higherBound - w, n)) + f((higherBound, n)))
            S=S*2
        return simpsonNew
    '''

    #def integrate(self, lowerBound, upperBound):
    #    s=4.0
    #    w=(upperBound-lowerBound)/s
    #    s = s*2
    #    return s
    #    pass

    def getF(self):
        return self.f

    def simpsonBuild(self, lowerBound, upperBound):
        sNew = self.f(lowerBound, 5) + self.f(upperBound, 5)
        s = 4.0
        w = (upperBound - lowerBound)/s
        term = 1
        while term < s:
            if term % 2 == 0:
                sNew += 2 * self.f(lowerBound + term * w, 5)
                term += 2
            else:
                sNew += 4 * self.f(lowerBound + term * w, 5)
                term += 2
        return sNew

