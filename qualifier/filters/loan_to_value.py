"""Loan to Value Filter: filters the bank list by the applicant's maximum home loan to home value ratio."""


def filter_loan_to_value(loan_to_value_ratio, bank_list): # def function to filter loan to value passing loan to value ratio and bank list as arguments

    loan_to_value_approval_list = [] #create empty list to append approved loans to 

    for bank in bank_list: #for loop to iterate through bank list
        if loan_to_value_ratio <= float(bank[2]): #conditional - if loan to value ratio is less than or equal to the max ratio approved by bank
            loan_to_value_approval_list.append(bank) #if above is true, append the approved loans to the empty list above
    return loan_to_value_approval_list #return list of qualifying bank loans
