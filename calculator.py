#calculator
def add(x,y):
    result=x+y
    print(x+y)
    return result
def subtract(x,y):
    result=x-y
    print(x-y)
    return result
def multiply(x,y):
    result=x*y
    print(x*y)
    return result
def divide(x,y):
    try:
        result=x/y
        print(x/y)
    except EOFError :
        print("sorry 0 can't be a denominator")
    return result
print('Welcome! Thank you for choosing us')
n=int(input('Please enter a number:'))
k=int(input('Please enter another number too:'))
while True:
            m=input('''choose one: a-Add
                        s-subtract
                        d-divide
                        m-multiply''')
            if m=='a':
                result=add(n,k)
            if m=='s':
                result=subtract(n,k)
            if m=='d':
                result=divide(n,k)
            if m=='m':
                result=multiply(n,k)
            ch=input('do you want to enter more records?:yes or no')
            if ch=='no':
                print('Thank You!')
                break
            else:
                l=int(input('Please enter new number:'))
                k=l
                n=result
