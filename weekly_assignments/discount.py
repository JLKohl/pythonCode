import datetime

date = datetime.datetime.now()
weekday = date.weekday()
 

subtotal = float(input('what is your subtotal? '))

if subtotal >= 50 and (weekday == 1 or weekday() == 2):
    discount = subtotal * .1
    print(f'Discount: {discount:.2f}')
    total = subtotal - discount

else:
    total = subtotal

tax = total * 0.06
total_with_tax = total + (tax)

print(f'Sales tax: {tax:.2f}')
print(f'Total: {total_with_tax:.2f}')