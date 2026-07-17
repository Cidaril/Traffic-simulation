import random
import math

dist=int(input("Insert the point the vehicle has to travel to: "))
Vlist=[]
class Vehicle:
    def __init__(self,number):
        self.number=number
        self.name="v"+str(number)
        self.speed=random.randint(1,5)
        self.position=random.randint(1,10)
        self.iposition=random.randint(1,10)
    
    def can_move(self):
       for i in range(0,self.speed):
           for j in range(0,len(Vlist)):
               if Vlist[j].position==self.position+1:
                   return 0
           else:
               self.position+=1
for k in range(1,6):
    for x in Vlist:
        x.can_move()
        if x.position>=dist:
           print("the",x.name,"vehicle has reached its destination")
           Vlist.remove(x)
    Vlist.append(Vehicle(k))
for x in Vlist:
    print("This vehicle has the speed",x.speed,"and has started at",x.iposition,"with the name",x.name)
while Vlist:
    for x in Vlist:
        x.can_move()
        if x.position>=dist:
           print("the",x.name,"vehicle has reached its destination")
           Vlist.remove(x)