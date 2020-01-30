# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 5-11

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', ]

for num in numbers:
    if num == '1':
        print(str(num) + 'st\n')
    elif num == '2':
        print(str(num) + 'nd\n')
    elif num == '3':
        print(str(num) + 'rd\n')
    else:
        print(str(num) + 'th\n')
