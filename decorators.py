'''def first(x):
    return x+1
def second(x):
    return x-1

def operations(func):
    result = func
    return result

print(operations(first(5)))
'''

'''def outer(a):
    print("outer function::",a)
    def inner(x):
        print("inner function::",x)
    return inner

obj = outer(10)(6)
# obj(6)
'''

'''def first(func):
    def inner(x):
        print("innner function::",x)
    return inner

def second():
    print("second function::")

obj = second()
print(obj)
obj1= first(second())(5)'''
#function based decorator without arguments
def validate(func):
    def hello(a,b):
        if a>0 and b>0:
            print(func(a,b))
        else:
            print("a and b values must be greater than 0")

    return hello
@validate
def add(x,y):
    return x+y

add(5,5)

#class based decorators:
class squares:
    def __init__(self,x):
        self.x = x
    def __call__(self,a):
        print("squares of a is:",a)
        print(self.x(a))

@squares
def square(y):
    return y**2

square(5)


