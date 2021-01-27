print('MENU \n')
print('For Addition  1')
print('For Subtraction  2')
print('For Multiplication  3')
print('For Division  4')
print('For Exit  5')

ch = int(input('Enter you choice :'))
a = int(input('Enter a : '))
b = int(input('Enter b : '))

if(ch == 1):
    print('Addition : ',a+b)
elif(ch == 2):
    print('Subtraction : ', a-b)
elif(ch == 3):
    print('Multiplication : ', a*b)
elif(ch == 4):
    print('Division : ', a/b)
elif(ch == 5):
    print('Exit')
    exit(0)
else:
    printf('Wrong number')
    
    
