# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 5-3, 5-4, & 5-5
import random
colors = ['green', 'red', 'yellow']
alien_colors = colors[random.randint(0, 2)]

if alien_colors == 'green':
    print('It was a green alien!')
    print('You just earned 5 points!')
elif alien_colors == 'red':
    print('It was a red alien!')
    print('You just earned 10 points!')
else:
    print('It was a yellow alien!')
    print('You just earned 15 points!')

