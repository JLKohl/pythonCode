import math
print()
items = int(input('How many items are there? '))
amount = int(input('How many items per box? '))

boxes = math.ceil(items/amount)

print()
print(f' For {items} items, packing {amount} items in each box, you will need {boxes} boxes.')
print()