
Rcome = {'Alice':90000,
        'vision':100000,
        'Guo-He':200000,
        'Starsak':98888,
        'Xinyuy':98881}

Highh = max(Rcome, key=Rcome.get)
print("The Richest man on earth who pay for lunch:", end=' ')
print(Highh + ' with $' + str(Rcome[Highh]))