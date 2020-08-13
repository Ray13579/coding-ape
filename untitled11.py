import random

a = random.randrange(0,101)

if a >= 90:
    print("A+")
    
elif a >= 80 and a <=90:
    print("A")
    
elif a >= 70 and a <=80:
    print("B")

elif a >= 60 and a <=70:
    print("C")
    
else:
    print("F")
    
print(a)