#Nested if-else
a = int(input('Enter a:'))
b = int(input('Enter b:'))
if a > b:  
    print('a is big')
else:
    if a < b:
        print('b is big')
    else:
        print('a = b')
