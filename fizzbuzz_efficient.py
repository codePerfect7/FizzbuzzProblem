# The EFFICIENT WAY
from time import time
t=[]
for j in range(5):
    start = time()
    c3, c5 = 0, 0
    d=''
    for i in range(1, 31):
        c3+=1
        c5+=1
        if c3==3:
            d+='fizz'
            c3=0
        if c5==5:
            d+='buzz'
            c5=0
        print(i if d=='' else d)
        d=''
    end = time()
    t.append(end-start)
print(sum(t)/5)