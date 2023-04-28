# Getting the user income

income = float(input('Enter your income after taxes'))

# Using the 50/30/20 rule we have the following percentages

p_50 = (50/100) * income
p_30 = (30/100) * income
p_20 = (20/100) * income

print('==================== \n Your 50% 30% 20% \n====================')
print('Essentials: £{:,.2f}'.format(p_50))
print('Wants: £{:,.2f}'.format(p_30))
print('Savings: £{:,.2f}'.format(p_20))