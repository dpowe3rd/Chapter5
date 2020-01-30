# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 5-6

age = int(input())

if age <= 2:
    print('You\'re a baby!')
elif 2 < age < 4:
    print('You\'re a toddler!')
elif 4 < age < 13:
    print('You\'re a kid!')
elif 13 < age < 20:
    print('You\'re a teenager!')
elif 20 < age < 65:
    print('You\'re an adult!')
else:
    print('You\'re an elder!')
