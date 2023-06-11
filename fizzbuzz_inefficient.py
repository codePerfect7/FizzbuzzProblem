# The EASY WAY
from time import time
t=[]
for j in range(5):
    start = time()
    for i in range(1, 31):
        if i%15==0:
            print('fizzbuzz')
            continue
        if i%3==0:
            print('fizz')
            continue
        if i%5 == 0:
            print('buzz')
            continue
        print(i)
    end = time()
    t.append(end-start)
print(sum(t)/5)