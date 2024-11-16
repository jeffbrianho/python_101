# Write a program that asks the user to enter an integer greater than 0, 
# then asks whether the user wants to determine the sum or the product of 
# all numbers between 1 and the entered integer, inclusive.

# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.



def compute_sum(num):
    print(sum(range(0, num + 1)))


def compute_product(num):
    prod = 1
    for nums in range(1, num + 1):
        prod *= nums
    print(prod)

def get_input():
    num = int(input('Please enter an integer greater than 0: '))
    return num

def calculate():
    cal = input('Enter "s" to compute the sum, or "p" to compute the product: ')
    if cal == 's':
        compute_sum(integer)
    elif cal == "p":
        compute_product(integer)
    else:
        print('please enter an appropriate letter')   

integer = get_input()
calculate()

        


        
    
  
