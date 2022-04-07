"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
import sys #import sys to provide various functions and variables
import fire #imports the fire library to turn components into CLIs
import questionary #imports the questionary library to build user promts in the CLI
from pathlib import Path #from the pathlib library, imports Path to organize directories

from qualifier.utils.fileio import load_csv,save_csv #imports the function named load_csv from the fileio file in the qualifier.utils

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
) #imports two functions (calc monthly debt ratio & calc loan to value ratio) which are stored in the calculators file in qualifier.utils

from qualifier.filters.max_loan_size import filter_max_loan_size #imports the filter max loan size function stored in the file under qualifier.filters
from qualifier.filters.credit_score import filter_credit_score #imports the filter credit score function stored in the file under qualifier.filters
from qualifier.filters.debt_to_income import filter_debt_to_income #imports the filter debt to income function stored in the file under qualifier.filters
from qualifier.filters.loan_to_value import filter_loan_to_value #imports the filter loan to value function stored in the file under qualifier.filters

#header = []

def load_bank_data(): #defining function load_bank_data as first query
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask() #Prompt in CLI will ask the user to enter a file path
    csvpath = Path(csvpath)
    if not csvpath.exists(): #If that file path does not exist...
        sys.exit(f"Oops! Can't find this path: {csvpath}") #The system will exit by displaying an error "Oops! Cant find this path: with the path entered"

    return load_csv(csvpath) #We will want to return this function calling the csvpath to use in the future.


def get_applicant_info(): #defining function get_applicant_info as 2nd query if the user inputted an existing csv path
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask() #Promt in the CLI will ask the user to input their credit score
    debt = questionary.text("What's your current amount of monthly debt?").ask() #Promt in the CLI will ask the user to input their monthly debt
    income = questionary.text("What's your total monthly income?").ask() #Promt in the CLI will ask the user to input their monthly income
    loan_amount = questionary.text("What's your desired loan amount?").ask() #Promt in the CLI will ask the user to input their desired loan amt
    home_value = questionary.text("What's your home value?").ask() #Promt in the CLI will ask the user to input their home value

    credit_score = int(credit_score) #dependent on what the user enters, this will convert the input into an integer
    debt = float(debt) #dependent on what the user enters, this will convert the input into a number with a decimal
    income = float(income) #dependent on what the user enters, this will convert the input into a number with a decimal
    loan_amount = float(loan_amount) #dependent on what the user enters, this will convert the input into a number with a decimal
    home_value = float(home_value) #dependent on what the user enters, this will convert the input into a a number with a decimal

    return credit_score, debt, income, loan_amount, home_value #Return the values inputted to use for the rest of the application


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value): #defining a function to find the qualifying loans as next query, based on what the user has inputted above
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income) # Calculate the monthly debt ratio by calling the existing function and assign to variable monthly_debt_ratio
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}") #Print the result of above with an f string description and rounding to 2 decimal places

    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value) # Calculate loan to value ratio by calling the existing function and assign to variable loan_to_value_ratio
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.") #Print the result of above with an f string description and rounding to 2 decimal places

    bank_data_filtered = filter_max_loan_size(loan, bank_data) #Run qualification filter from existing function for max loan size
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered) #Run qualification filter from existing function for credit score
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered) #Run qualification filter from existing function for debt to income
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered) #Run qualification filter from existing function for loan to value

    print(f"Found {len(bank_data_filtered)} qualifying loans") #After running all filters with given parameters, use the len function to count how many qualifying loans were found, and print.
    
    return bank_data_filtered #return the list of qualifying loans to be referenced later


#Write here, if no qualifying loans exists, sys.exit

def save_qualifying_loans(qualifying_loans): #define function save qualifying loans, passing the list of qualifying loans
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    if not qualifying_loans:
        sys.exit("Unfortunately you have not qualified for a loan. Thank you for using our service and having an nice day.")
    save_file = questionary.confirm("Would you like to save your qualifying loans?").ask()
    
    if save_file:
        csvpath = questionary.text("Enter a file path to save your results(.csv):").ask()
        csvpath = Path(csvpath)
        save_csv(csvpath,qualifying_loans)
        
            
    #insert 

def run(): #defining main function for running the script above 
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)
