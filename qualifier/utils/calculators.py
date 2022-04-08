"""Financial calculator functions needed to determine loan qualifications."""


def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income): #function calculate monthly debt ratio passing monthly debt payment and monthly income
    
    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income) #calculates monthly debt ratio - also converting inputs to integers - and assigns to variable
    return monthly_debt_ratio #returns monthly debt ratio to be used further in app.py


def calculate_loan_to_value_ratio(loan_amount, home_value): #function calculate loan to value ratio passing loan amount and home value parameters
    
    loan_to_value_ratio = int(loan_amount) / int(home_value) #calculates loan to value ratio - also converting inputs to integers - and assigns to variable
    return loan_to_value_ratio #returns loan_to_value_ratio to be used further in app.py
