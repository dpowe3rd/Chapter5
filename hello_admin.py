# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 5-8 & 5-9

user_names = ['DPowe', 'KHunter', 'NAndino', 'VAnatusi', 'DGreige', 'GEslea', 'admin', ]

for i in user_names:
    if i == 'admin':
        print('Hello admin, would you like a status report?')
    elif i in user_names:
        print('Hello ' + str(i) + ', how are you today?')
    else:
        print('We need users!')