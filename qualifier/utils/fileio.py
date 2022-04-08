"""Helper functions to load and save CSV data."""

import csv #import the csv function library


def load_csv(csvpath): #defining function load_csv 
    
    with open(csvpath, "r") as csvfile: #use with open function to open the csv file from the Path as a reader csvfile
        data = [] #create a new list for data to append data to later on
        csvreader = csv.reader(csvfile, delimiter=",") #names file inputted as the csvreader and opens by passing csvfile

        next(csvreader) # Skip the CSV Header

        for row in csvreader: #iterates through the rows od data in the csv file given
            data.append(row) #appends the empty list data with the new rows of data
    return data #Returns a list of lists that contain the rows of data from the csv file inputted


def save_csv(csvpath, qualifying_loans): #Defining function save_csv 

    with open(csvpath, "w") as csvfile: #use with open function to open the csv file from the path as a writer csvfile
        csvwriter = csv.writer(csvfile, delimiter=",") #names file inputted as the csvwriter and opens it by passing csvfile

        for loan in qualifying_loans: #iterates through the list of qualifying loans
            csvwriter.writerow(loan) #csv writer writes out the rows of data from the qualifying loans list

