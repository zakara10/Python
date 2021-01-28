n = int (input('Enter n :'))
i = 2
while i <= n:
    print(i,end='  ')
      i = i + 2

n = int (input('Enter n :'))
i = 2
while i < n:
    if(n%i==0):
        prime(n,'is not prime')
        break
    else:
        i = i+1
else:
    prime(n,'is a prime')



    
        