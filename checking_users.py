# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 5-10

current_users = ['john', 'bobby', 'johnny', 'cat', 'rich', 'poster', ]
new_users = ['cup', 'John', 'ricky', 'Bobby', 'dog']

for user in new_users:
    if user.lower() in current_users:
        print('Im sorry but that name is taken. Please try another.')
    else:
        print('That name is available. PLease wait while we redirect you.')