def to_roman( n ):
    numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    result = ""
    for value, symbol in numerals.items():
        while n >= value:
            result += symbol
            n -= value
    return result



def price_of_shipment( weight, priority=False ):
    price = 5 + weight * 2
    if priority:
        price * 1.5
    return price



def factorial( n ):
    if n == 0:
        return 1
    return n * factorial(n - 1)


