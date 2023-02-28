class FACT:
    n=0
    def fact(self,n):
        if (self,n==0):
            return(1)
        else:
            return(self.n*self.fact(self.n-1))
        class NPR(FACt):
            r=0
            def npr(self,n,r):
                self.r=r
                self.n=n
                t=self.n-self.r
                return(self.fact(self.n)/self.fact(t))

            fl=FACT()
            x=int(input())
            y=int(input())
            print(fl.fact(x))
            
