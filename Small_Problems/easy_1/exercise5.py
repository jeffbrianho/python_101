# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate.
# The program must compute the tip, then print both the tip and the total amount of the bill. 
# You can ignore input validation and assume that the user will enter valid numbers.

def tip_percent(cost, tip):
    return cost * tip

def bill_cost():
    print("Welcome to the bill calculator!")
    bill = float(input("Enter in the cost of the bill"))
    tip_rate = float(input("Enter in your tip amount"))

# def display():
#     print(f'The cost of the tip is{tip_percent(bill, tip_rate)}')
#     print(f'The total cost is ')

bill_cost()
print(tip_percent(bill, tip_rate))
