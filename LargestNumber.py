a = int(input ('Enter the 1st number: '))
b = int(input ('Enter the 2nd number '))
c = int(input ('Enter the 3nd number '))

if a > b:
    if a > c:
        print('1st number is the largest')
    else:
        print('3rd number is the largest')
else:
    if b > c:
        print('2nd number is the largest')
    else:
        print('3rd number is the largest')
