import random
n = random.randint(1,100)
a = -1
gusses = 1
while(a != n):
    
    a = int(input("guess a number: "))
    if(a > n):
        print("loweer number please")
        gusses += 1
    elif(a < n):
        print("higher number please")
        gusses += 1
    

print(f"you have gussed the number {n} correctly in {gusses} attempt")
