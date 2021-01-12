#Pseudo Code

# Get inputs from user for hours worked and their pay rate
# Calculate total pay rate by multiplying hours worked and pay rate
# Calculate social security taxes as a percentage of total pay
# Subtract social security taxes from total pay to get net pay
# Display results in an easy to read output


# Code

# Initialize Variables

ss_tax_rate = 0.062 # SS Tax rate: 6.2%

# Get input from user

hours = int(input('Enter your hours worked: '))
pay_rate = int(input('Enter the pay rate in dollars per hour: '))

# Calculate results

total_pay = hours * pay_rate
ss_tax = ss_tax_rate * total_pay 
net_pay = total_pay - ss_tax

# Print out results with informative labels 
# Using %.2f truncates values to 2 decimal places without changing value
print('Total pay: $%.2f' % total_pay)
print('Social Security Tax: $%.2f' % ss_tax)
print('Net pay: $%.2f' % net_pay)

