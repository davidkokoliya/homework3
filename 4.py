def my_func(x, y):
    return 1 / x ** abs(y)
print(f'Result - {my_func(int(input("Enter positive numeral ")), int(input("Enter Negative Numeral ")))}')