import math
heightt=5
base1=5
base2=6
def myfunc():
    trapezoidd=(heightt*(base1+base2))/2
    print(trapezoidd)

myfunc()

import math
numofsides=4
lengthofaside=25

def myfunc():
    x=lengthofaside/2
    y=numofsides*lengthofaside
    z=(x*y)/2
    print(z)

myfunc()

import math
base=5
heightt=6

def myfunc():
    x=base*heightt
    print(x)

myfunc()

import datetime

x = datetime.datetime.now() - datetime.timedelta(days=5)
print(x)

import datetime

x = datetime.datetime.now() - datetime.timedelta(days = 1)
y = datetime.datetime.now()
z = datetime.datetime.now() + datetime.timedelta(days = 1)
print(x)
print(y)
print(z)

import datetime
x = datetime.datetime.now()
print(x.strftime("%f"))

import datetime
x = datetime.datetime.now()-datetime.timedelta(days=1)

print(x.strftime("%S"))

import math
n=10
def myfunc():
    x = 1
    while True:
        if x >= n:
            break
        yield x*x
        x+=1

for x in myfunc():
    print(x)

import math
n=int(input())
def myfunc():
    x=0
    while True:
        if x >= n:
            break
        if x%2==0:
            yield x
        x+=1

for x in myfunc():
   print(x, end=', ')

import math
n=10
def myfunc():
    x=0
    while True:
        if x >= n:
            break
        if x%3==0:
            yield x
        elif x%4==0:
            yield x
        x+=1

for x in myfunc():
   print(x)


