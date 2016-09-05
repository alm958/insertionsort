import random
import time
isortsum = 0
isortruntimedist = []
#def insertionsort():
arr = []
for k in range(0,1000):  # since i tested the other sorts witk 1000 elements I maintained that here as well
        arr.append(int(round(random.random()*10000)))
#arr = [0,9,8,7,0,6,7,8,9,0] #smaller list for initial testing
#print arr
start_time = time.time()
for i in range(1,len(arr)):
    value = arr[i]
    for j in range(i-1,-1,-1):
        if value < arr[j]:
            arr[j+1]=arr[j]
            arr[j]=value
        else:
            break
    #print arr #during testing print array for each loop
end_time = time.time()
run_time = (end_time - start_time)*1000
print arr
print run_time # average run time for 10runs was 167ms.
#return run_time #return value if implemented in a function
