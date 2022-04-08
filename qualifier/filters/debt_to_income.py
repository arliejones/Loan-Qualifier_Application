"""Debt to Income Filter: filters the bank list by the applicant's maximum debt-to-income ratio."""


def filter_debt_to_income(monthly_debt_ratio, bank_list): #def function filter debt to income passing monthly debt ratio and bank list as arguments

    debit_to_income_approval_list = [] #create empty list to append approved loans to later on
    for bank in bank_list: #for loop to iterate through bank list
        if monthly_debt_ratio <= float(bank[3]): #conditional - if the monthly debt ratio is less than or greater to the max ratio allowed by the bank
            debit_to_income_approval_list.append(bank) #if above is true, append the approved loans to the empty list debut to income approval list
    return debit_to_income_approval_list #return list of qualifying bank loans
