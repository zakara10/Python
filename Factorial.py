n = int(input('Enter n :'))
fact =1
for i in range (1, n+1):
    fact= fact * i
else:
    print('%d! = %d'%(n,fact))
