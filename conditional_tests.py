# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 5-1 & 5-2

cool_colors = ['red', 'yellow', 'green', 'purple', 'black', 'brown', 'gray', 'pink', 'blue']
cars = ['audi', 'bmw', 'toyota', 'mazda', 'honda']

favorite_car = 'JEEP'
favorite_color = 'purple'

print('Is my favorite car a Toyota? I predict false.')
print(favorite_car == 'toyota')

print('\nIs my favorite car a Honda? I predict false.')
print(favorite_car == 'Honda')

print('\nIs my favorite car a BMW? I predict false.')
print(favorite_car == 'BMW')

print('\nIs my favorite car a Mazda? I predict false.')
print(favorite_car == 'Mazda')

print('\nIs my favorite car a Audi? I predict false.')
print(favorite_car == 'Audi')

print('\nIs my favorite car a JEEP? I predict true.')
print(favorite_car.lower() == 'jeep')

print('\nIs my favorite color purple? I predict true.')
print(favorite_color == 'purple')

print('\nMy favorite color isn\'t green. I predict true.')
print(favorite_color != 'green')

print('\nI only like nine colors! I predict true.')
print(len(cool_colors) >= 9)

print('\nPurple and Green are cool colors. I predict true.')
print('purple' and 'green' in cool_colors)

print('\nAudi\' or Benz\'s are cool cars. I predict true.')
print('benz' in cars or 'audi' in cars)


