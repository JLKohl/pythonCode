import math; import datetime

pi = math.pi
date = datetime.datetime.now()

print()

tire_width = int(input(f'what is the width of the tire? '))
tire_aspect_ratio = int(input(f'what is the aspect ratio of the tire? '))
tire_diameter = int(input(f'what is the diameter of the tire? '))

volume = round((pi * tire_width**2 * tire_aspect_ratio * (tire_width*tire_aspect_ratio + 2540 * tire_diameter))/ 10000000000, 2)

print()

print(f'the approximate volume is {volume:.2f} liters')
print()
user_tires = input(f'Would you like to buy a set of tires with these dementions? ')

if user_tires == 'yes':
    user_name = input('please enter your first and last name: ')
    user_phone_number = input('please enter your phone number so we can contact you: ')
    print('Thank you for your information. A representative will be with you shortly.')
    with open("volume.txt", "at") as volume_file:
        print(f'{user_name}: {user_phone_number}', file=volume_file)
else:
    print('have a nice day!')


with open("volume.txt", "at") as volume_file:
    print(f'{date:%Y-%m-%d}, {tire_width}, {tire_aspect_ratio}, {tire_diameter}, {volume}', file=volume_file)
