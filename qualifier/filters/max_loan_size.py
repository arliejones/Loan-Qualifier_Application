"""Max Loan Size Filter: filters the bank list by comparing the user's loan value against the bank's maximum loan size."""


def filter_max_loan_size(loan_amount, bank_list): #def function filter max loan size passing loan amount and bank list as arguments

    loan_size_approval_list = [] #create empty list of loan size approvals to append to

    for bank in bank_list: #for loop to iterate through bank list
        if loan_amount <= int(bank[1]): #conditional - if the loan amount inputted is less than or equal to the max allowed by the bank
            loan_size_approval_list.append(bank) #if above is true, append the approved loan to empty list
    return loan_size_approval_list #return list of qualifying bank loans
