# find sum of all the number inputted by user and stop inputting when pressed zero

s = 0
n = int(input('Enter a number : '))
while n!= 0 :
    s = s + n
    n = int(input('Enter a number : '))
else :
    print('sum : ',s)
