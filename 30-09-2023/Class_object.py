class A:
    z=input("Enter String:")
    x=int(input("Enter a number:"))
    y=int(input("Enter a number:"))
    def add(self,a,b):
        print("reverse:",a[::-1])
        print("square:",b*b)
    def displayresult(self):
        print("lenght of string",len(self.z))
        print("modulus:",self.x%self.y)
obj=A()
a=input("Enter string:")
b=int(input("Enter number"))
obj.add(a,b)
obj.displayresult()