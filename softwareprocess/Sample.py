class Sample():
    def __init__(self,n=None):
        if(not(isinstance(n,int))):
            raise ValueError("Sample.__init__:  invalid n")
        if(n == None):
            raise ValueError('Sample.__init__:  invalid n')
        if((n<2) or (n>29)):
            raise ValueError('Sample.__init__:  invalid n')
        self.n = n

    def getN(self):
        return self.n

    def gamma(self, x):
        return 1
