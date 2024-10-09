def prompt(message):
    print(f'===> {message}')

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number < 0:
            raise ValueError(f'number must be > 0: {number_str}')
    except ValueError:
        return True
    return False

prompt("Welcome to the Mortgage Calculator!")

while True:
    prompt('Enter the loan amount in dollars ')

    loan_amount = (input())
    while invalid_number(loan_amount):
        prompt("Hmm... that doesn't look like a valid number.")
        loan_amount = input()

    prompt('Enter the annual percentage rate as a percentage'
            '(ex. 2.0 not 0.02)')
    apr = (input())
    while invalid_number(apr):
        prompt("Hmm... that doesn't look like a valid number.")
        apr = input()

    apr_percent = float(apr) / 100
    monthly_interest = apr_percent / 12

    prompt('Enter the loan duration in years ')

    duration =  input()
    while invalid_number(duration):
        prompt("Hmm... that doesn't look like a valid number.")
        duration = input()

    monthly_duration = float(duration) * 12

    if int(apr):
        calculated_interest = (monthly_interest /(1 - (1 + monthly_interest)
                            ** (-monthly_duration)))
    else:
        calculated_interest = 1 / 12

    monthly_payment = float(loan_amount) * calculated_interest

    prompt(f' Your payment will be ${round(monthly_payment,2)} '
           'dollars a month!')

    prompt('Would you like to perform another mortgage calculation?(y, n) ')
    response = input()
    if response and response[0].lower() != 'y':
        break