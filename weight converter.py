
weight = int(input('Enter the weight: ' ))
unit = input('(l )bs or (k)g : ')

if unit.lower() == 'l':
    converted = weight * 0.45
    print(f'You are {converted} kilos')
else:
    converted =weight /0.45
    print(f"you are {converted} lbs")


