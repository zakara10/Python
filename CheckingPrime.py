n = int(input('Enter the number you want to check whether its prime or not  :'))
i = 2
while  i<n:
    if n%i==0 :
         print('The number is not prime ')
         break
    else:
        i = i+1
else:
    print('The number is prime ')
