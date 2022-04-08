"""Credit Score Filter: filters a bank list by the user's minimum credit score."""


def filter_credit_score(credit_score, bank_list): #def filter credit score function passing credit score and bank list parameters

    credit_score_approval_list = [] #create empty list to append approved loans to later
    for bank in bank_list: #for loop to iterate through bank list 
        if credit_score >= int(bank[4]): #conditional statement, if credit score is greater then or equal to the minimum allowed credit score referenced by index 4
            credit_score_approval_list.append(bank) #if above is true, append the credit score approval list with the available bank loans
    return credit_score_approval_list #return the list of qualifying bank loans
