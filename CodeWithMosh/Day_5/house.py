price = 1000000
buyer = input('Enter or good or bad credit: ')

if buyer == 'good':
    downpayment = (price*10)/100
    print(f"Down payment = {downpayment}")
else:
    downpayment = (price*20)/100
    print(f"Down payment = {downpayment}")    

 