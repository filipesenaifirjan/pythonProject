v = int(input())
p = int(input())


pB = v // p

pA = v % p

for i in range(p):

    if pA > 0:
        
        pA -= 1
       
        print(pB + 1)
   
    else:

        print(pB)
