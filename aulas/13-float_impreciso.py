import decimal

dec1 = decimal.Decimal('0.1')
dec2 = decimal.Decimal('0.3')
print(dec1 + dec2)

num1 = 0.141341341323341
num2 = 0.741341235135134343
num3 = num1 + num2
print(num3)
print(f'{num3:.2f}')
print(round(num3, 3))
