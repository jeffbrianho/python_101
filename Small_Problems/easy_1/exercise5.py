# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate.
# The program must compute the tip, then print both the tip and the total amount of the bill. 
# You can ignore input validation and assume that the user will enter valid numbers.

def bill_cost():
    print("Welcome to the bill calculator!")
    bill = float(input("Enter in the cost of the bill "))
    return bill

def tip_percent():
   tip = float(input('What is the tip percent? Enter in 0.2 for 20% '))
   return tip   
         
def display_total():
    print(f'The cost of the tip is {tip}')
    print(f'The total cost is {tip + bill}')

bill = bill_cost()
tip = (tip_percent() * bill)

display_total()

