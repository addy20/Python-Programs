class Person():
    count=0
    def __init__ (self, name, DOB, address):
        self.name=name
        self.DOB=DOB
        self.address=address
        Person.count+=1
    def __del__(self):
        Person.count-=1    
    def getName(self):
        return self.name
    def getDOB(self):
        return self.DOB
    def getAddress(self):
        return self.address
    def setName(self,name):
        self.name=name
    def setDOB(self,DOB):
        self.DOB=DOB
    def setAddress(self,address):
        self.address=address
    def getCount(self):
        return Person.count
    def __str__ (self):
        return 'Name:'+self.name+'\nDOB:'+str(self.DOB)+'\nAddress:'+self.address
def main():
    p1=Person('Aditya','20 Feb 2001','ITER,Bhubaneswar')
    p2=Person('Soumyashree','24 Nov 2004','ODM Bhubaneswar')
    p3=p2
    print(p1)
    print(p2)
    del p1
    del p2
    del p3
    print(Person.count)
if __name__=='__main__':
    main()    

