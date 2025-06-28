class Calculator:
    def add(self, x, y, z=0):
        print("Sum:", x + y + z)
    def multiply(self,x=1,y=1,z=1):
        print('Product:',x*y*z)
    def divide(self,x=1,y=1,z=1):
        print('division:',x/y/z)
    def square(self,x=1):
        print('sqaure:',x**2)
    def cube(self,x=1):
        print('cube:',x**3)
    def expo(self,p,b):
        print('exponent:',p**b)
    def subtract(self,p=0,b=0,c=0):
        print('difference:',p-b-c)
c = Calculator()
c.add(2, 8)
c.add(9, 5, 2)
c.square(5)
c.multiply(8,5,2)
c.divide(56349/3)
c.subtract(0,99,55)
