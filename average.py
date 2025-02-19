sp1=int(input("enter a speed: "))
sp2=int(input("enter another speed: "))
sp3=int(input("enter another speed: "))
sum=(sp1+sp2+sp3)
print("the sum is",sum)
ave=(sum/3)
print("and the average is",ave)
if ave>sp1 and ave>sp2 and ave>sp3:
    print("%d is higher than %d,%d,%d"%(ave,sp1,sp2,sp3))
elif ave>sp1 and ave>sp2:
    print("%d is higher than %d,%d"%(ave,sp1,sp2))
elif ave>sp1 and ave>sp3:
    print("%d is higher than %d,%d"%(ave,sp3))
elif ave>sp2 and ave>sp3:
    print("%d is higher than %d,%d"%(ave,sp2,sp3))
elif ave>sp1:
    print("%d is higher than %d"%(ave,sp1))
elif ave>sp2:
    print("%d is higher than %d"%(ave,sp2))
elif ave>sp3:
    print("%d is higher than %d"%(ave,sp3))
else:
    print("invalid input")