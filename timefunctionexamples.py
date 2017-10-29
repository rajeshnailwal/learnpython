#Time functions
from time import clock, sleep

print("=============Example of System clock timing===============")

start = clock()

x = eval(input("Insert anything Rajesh : "))

end = clock()

timetaken = end - start

print("Time taken by Rajesh in giving input : ",timetaken)

print("\n\n=================Example of sleep================")

for n in range(10, 0, -1):
    print("starting sleep on",n)
    sleep(1)
    print("came out of sleep for",n)
