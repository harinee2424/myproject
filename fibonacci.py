nterms= int(input("how many terms? " ))
n1, n2 = 0, 1
if nterms <=0:
    print("please enter a positive integer")
elif nterms== 1:
     print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

