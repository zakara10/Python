n = int(input('Enter the number you want to check'))
s = 0
temp = n
while temp > 0:
    rem = temp % 10
    s = s + rem*rem*rem
    temp = temp//10

if n == s:
    print('This number is an armstrong number')
else:
    print('This number is not armstrong number')
