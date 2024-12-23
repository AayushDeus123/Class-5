#Calculating Profit and Loss
cost = int(input('Enter your buying price : '))
sell = int(input('Enter your selling price : '))
if cost>sell:
    print('You have made a Loss of Rs' ,cost-sell)
elif sell>cost:
    print('You have made a Profit of Rs' ,sell-cost)
else:
    print('You have made no Profit or Loss')    