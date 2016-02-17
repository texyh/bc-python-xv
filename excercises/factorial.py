from functools import reduce

#to calculate the factorial of any number n
n = 5
ls =[x for x in range (1,n+1)]
factorial = reduce(lambda x,y:x*y,ls)
print (factorial)