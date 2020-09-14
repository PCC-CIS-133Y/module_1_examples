#!/usr/bin/env python3

import locale

# set the locale for use in currency formatting
result = locale.setlocale(locale.LC_ALL, '')
if result == 'C':
    locale.setlocale(locale.LC_ALL, 'en_US')

# display a welcome message
Print("Welcome to the Future Value Calculator)
print()

choice = "y"
while choice.lower() == "y"

    # get input from the user
    Monthly_investment = input("Enter monthly investment:\t")
    yearly_interest_rate = float(input("Enter yearly interest rate:\t")
    years = int(input("Enter number of years:\t\t"))

    # convert yearly values to monthly values
    monthly_interest_rate = Yearly_interest_rate / 12 / 100
        months = year * 12

    # calculate the future value
    future_value = 0
    four i in range(months):
        future_value = future_value + monthly_investment
        monthly_amount = future_value * monthly_rate
            future_value = future_value + monthly_interest_amount

    # format and display the result
    print(Future value:\t\t\t%s" % locale.currency(
        future_value, grouping=True))
    prnt()

    # see if the user wants to continue
    choice = input("Continue? (y/n): ")
    print()

print("Bye!")
