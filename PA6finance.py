# Programmers: Alyssa and Chiara
# Course: CS201.02, Dr. Olsen
# Date: Dec 7, 2016
# Programming Assignment: 6
# Problem Statement: The purpose of this program is to analyze data about campaign finances. The Program can answer the following questions:
#    1:	How did the amount of donations change over time?
#    2:	Which committee received the most money?
#    3:	How many people donated from a particular employer?
#    4:	How much do retired people donate and the percentage of them who donate to each committee?
# Data In: choice of question, again(if user wants to pick another option), inputfile for data, employer user wants inquire information about
# Data Out: the amount of money donated to a committee and the name of the committee( to an output file), and
#    graph(money_per_day.png)-graphs how the amount of donations changed over time
# Ofter files needed: campaignfinance.csv, campaignfinance-short.csv,testfile.txt
# Credits: none

import os, sys, pylab, string


# Lead Programmer: Chiara
# Purpose: error checks input file to see if file exists
# Parameters: none
# Return: valid input file
def valid_file():
    filename = input("Please enter an input file :").strip()
    while not os.path.exists(filename):
        print("Invalid file name.")
        filename = input("Please enter an input file: ").strip()

    return filename


# Lead Programmer: CO-Programed
# Purpose: read data from the input file to a list
# Parameters: inputfile
# Return:list of data in file
def read_file_to_list(inputfile):
    try:
        datalist = []
        file = open(inputfile, "r")  # opens input file in read mode
        for each_line in file:
            line = each_line.replace("\n", "")  # gets rid of any unnecessary new lines in the file
            newline = ""
            quote_count = 0
            # replaces necessary commas with "|" so that list can be split into values needed to solve problems
            for letter in line:
                if letter == "," and quote_count % 2 == 0:  # if the letter is a comma and  quotes count is even
                    add = "|"
                elif letter != "\"":  # if the letter is not a quote
                    add = letter
                else:  # if the letter is a quote add one to count and add nothing
                    quote_count += 1
                    add = ""
                newline += add
            if letter == line[-1]:
                quote_count += 1
            line_list  = newline.split("|")
            datalist.append(line_list)
        file.close()
    except FileNotFoundError:
        print("Error. The file you inputted is no longer found. Sorry.")
        sys.exit(1)
    return datalist


# Lead Programmer: Alyssa
# Purpose: Gives the user a menu of options
# Parameters: None
# Return choice
def menu():
    print("*"*100)
    print("Please choose a question:")
    print("1:\tHow did the amount of donations change over time? \n2:\tWhich committee received the most money?\n3:\tHow many people donated from a particular employer?\n4:\tHow much do retired people donate and the percentage of them who donate to each committee?")
    choice = input("Your choice: ").strip()
    # outputs an error if user enters an invalid choice and asks user to pick again
    while choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print("Input Error: Please enter 1,2,3 or 4")
        choice = input("Your choice: ").strip()
    return int(choice)


# Lead Programmer: Chiara
# dictionary_choice1
# Purpose: analyzes the list of lists to count the donations per day then stores day as key and count as value
# Parameters:list of list , choice from menu
# Return: dictionary with keys of dates and values of amount donated on that day
def dictionary_choice1(list):
    # creates empty dictionary
    money_per_day = {}
    for line in list:
        # error checks to make sure that years written as 16 are rewritten to be 2016 in dates
        if line[9][6:] == "16 0:00":
            line[9] = line[9][0:5] + "/2016 0:00"
        # checks if the date at the value in the list is in the dictionary money_per_day
        if line[9] in money_per_day:
            # if date is in money_per_day adds amount donated to the value associated with the date in the dictionary money_per_day
            money_per_day[line[9]] += float(line[-1].strip())
        else:
            # otherwise creates a key in money_per_day with the date and the value of the amount donated
            money_per_day[line[9]] = float(line[-1].strip())
    return money_per_day


# Lead Programmer: Alyssa
# Dictionary_choice2
# Create dictionary function choice 2 = amount of donations per committee,
# Purpose: analyzes data and adds amount of donation to each commitee. Creates a dictionary where commmitee is the value and amount of total donations is the key
# Parameters: list of list,
# Return: dictionary of committees as keys and the amount donated to the committees as values
def dictionary_choice2(list_list, outfilename):
    dict = {}
    numkey_dict = {}
    for donation in list_list:
        # checks if committee is a key in dictionary dict
        if donation[0] in dict:
            # if committee is already a key in the dictionary dict-adds donation to the value associated with the key
            dict[donation[0]] += float(donation[-1].strip())
        else:
            # otherwise creates a new key-value pair in the dictionary dict where the committee is the key and the value is their donation
            dict[donation[0]] = float(donation[-1].strip())
    # opens output file in write mode
    outfile = open(outfilename, "w")
    # prints to outputfile every value (rounded to the second decimal place) and its corresponding key in the dictionary dict
    for key in dict:
        print(round(dict[key], 2), key, sep="\t\t", file=outfile)
    outfile.close()
    # Creates dictionary numkey_dict so that the keys in numkey_dict are the values in dict and the values in numkey_dict are the keys in dict
    for key in dict:
        numkey_dict[dict[key]] = key
    return numkey_dict


# Lead Programmer: CO-programmed
# Purpose: Deletes punctuation in string
# Parameters: string of choice
# Return: string without punctuation
def punctuation(str):
    for letter in string.punctuation:
        str= str.replace(letter, "") # replaces all punctuation in str with ""
    return str


# Lead Programmer: Chiara
# dictionary_choice3
# Purpose: analyzes the list of lists to count the number of donations from each employer, creates a dictionary that has employer as key and count as value,
# and determines how many people donated from a particular employer
# Parameters:list of list
# Return: the value at employer_donations[employer] - the amount of people who donated from the particular employer the user chose
def dictionary_choice3(list):
    employer_donations = {}
    # for every line in list checks if employer is a key in the dictionary employer_donations
    for line in list:
        temp = punctuation(line[6].upper())
        if temp in employer_donations:
            # if employer is a key in employer_donations adds one to the value at that key
            employer_donations[temp] += 1
        else:
            # if employer is not yet a key in employer_donations creates a key-value pair in employer_donations where the employer is the key and 1 is its value
            employer_donations[temp] = 1

    return employer_donations


# Lead Programmer: CO-Programmed
# Purpose: checks if employer is in dictionary and asks user to input a different employer if it isn't in the dictionary
# Parameters: dictionary of employers, employer to look for
# return: employer that is in dictionary
def employer_check(employer_donations, employer):
    # while employer is not in dictionary asks user to enter another employer
    while not (employer.upper().strip() in employer_donations):
        print("That employer is not in our list.")
        employer = input("Please enter the name of another employer: ").upper().strip()
    return employer


# Lead Programmer: Alyssa
# dictionary_choice4
# Purpose: Analyses data in a list of lists and creates a dictionary with a key of committee  and a value of the amount of retired of people who donated to the committee
# Parameters: list of list, choice
# Return: dictionary (key of committee  and a value of the amount of retired of people who donated to the committee)
def dictionary_choice4(list_list):
        dict = {}
        sum = 0 # will contain sum of total donations made my retired people
        for donation in list_list:
            # if the occupation is retired
            if donation[7].lower() == "retired":
                sum += float(donation[-1]) # adds donated amount to sum
                if donation[0] in dict: # if the committee the retired person donates to is a key in dict
                    dict[donation[0]] += 1 # add one to the value at the key of the committee
                else:
                    dict[donation[0]] = 1 # otherwise creates a key value pair of committee as key and 1 as value
        print("The total amount that retired people have donated is $", round(sum, 2))
        return dict


# Lead Programmer: CHiara
# Purpose: Creates a list of lists for dates and values and orders list by date
# The function will convert each entry in dictionary to a list and append list to a larger list, then sort this larger list by date
# Parameters: dictionary( keys as dates and values as donations)
# Return: a list sorted by date
def sort_dates(money_per_day):
    date_list = []
    for key in money_per_day:
        # creates a temporary list holding the key in money_per_day and its value
        temp = [key, money_per_day[key]]
        # adds the list temp to the larger list date_list
        date_list.append(temp)
    # sorts date_list so that the dates are in order
    date_list.sort()
    return date_list


# Lead Programmer: Alyssa
# Purpose: Creates a graph that shows how the amount of donations change over time by creating two lists x and y for graph, x values are at index[0] and y values at index[1] then uses lists to create graph
# Parameters: list of list with x and y values (sorted list from "list of list for dates and values and order by date")
# Return: n/a
def graph(sorted_dates):
    x = []
    y = []
    for i in range(len(sorted_dates)):
        y.append(sorted_dates[i][1])  # appends the value of the donation at sublist i to list y
        x.append(i)
    pylab.plot(x, y)  # plots x and y coordinates on a line graph
    pylab.ylabel("Amount of money")
    x_axis_label = "Dates from "+ sorted_dates[0][0]+" to "+ sorted_dates[-1][0]
    pylab.xlabel(x_axis_label)
    pylab.title("Amount of Money Donated Per Day")
    pylab.savefig("money_per_day.png")


# Lead Programmer: Chiara
# find greatest value and key from amount of donations dictionary
# Purpose: search through keys to find the max and its value(committee)
# Parameters: dictionary with keys as amount donated to a committee and the value as the name of the corresponding committee ,
# Return:max(committee with most donations)
def find_max(dictionary):
    max = 0
    # checks if each key is greater than the max
    for key in dictionary:
        if key > max:
            max = key # sets max to key if key is greater than max
    return max


# Lead Programmer: Alyssa
# Purpose: calculates percent for each committee and output to user
# calculates the percent by dividing the amount to committee to the total amount of retired people
# Parameters: retired dictionary
# Return: percent per committee dictionary
def percent_retired(retired_dict):
    dict_of_percent ={}
    sum = 0 # will hold the amount of retired people  that donated
    # adds the amount of retired people who donated
    for key in retired_dict:
        sum += retired_dict[key]
    # creates a percent of people who donated to each committee
    for key in retired_dict:
        percent = retired_dict[key]/sum
        dict_of_percent[key] = str(round(percent*100,3))+"%" # rounds percent
    return dict_of_percent


# Lead Programmer: CO-Programmed
# Purpose: main program
# Parameters: none
# Return:none
def main():
    print("The purpose of this program is to analyze data about campaign finances.")
    in_file= valid_file() # checks if file is valid
    finance_list=read_file_to_list(in_file) # reads file to list
    again = "yes"
    while again == "yes":
        choice = menu() # runs menu
        if choice == 1:
            money_per_day_dict = dictionary_choice1(finance_list)
            sorted_dates = sort_dates(money_per_day_dict) # sorts dates
            graph(sorted_dates) # makes graph
            print("Your graph of how the donations have change over time has been created.")
        elif choice == 2:
            outfilename = input("Please enter an outfile name: ").strip()
            committee_dict = dictionary_choice2(finance_list, outfilename)
            max = find_max(committee_dict) # finds committee
            print("The committee with the most money is ", committee_dict[max]," with $", round(max,2))
        elif choice == 3:
            employer_name = punctuation(input("Please enter the employer that you like to look up: ").upper().strip()) # replaces punctuation in inputed string employer_name
            employer_donations = dictionary_choice3(finance_list)
            employer_checked = employer_check(employer_donations, employer_name) # checks if employer is in the data
            print("The number of people who donated from ",employer_checked," is : ",employer_donations[employer_checked])
        else:  # choice == 4
            dict_retired = dictionary_choice4(finance_list)
            dict = percent_retired(dict_retired) # finds percents of retired people who donated to each committee
            print("% of Retired    Committee")
            print("~"*100) # creates border
            # prints the percent of retired people who donated to each committee
            for key in dict:
                print(dict[key], key,  sep="\t\t\t")
        print("*"*100) # creates border
        # asks user if they want to pick an option again
        again = input("Do you want to pick again?").strip().lower()
        while not(again == "yes" or again == "no"):
            again = input("Do you want to pick again? (please enter yes or no)").strip().lower()
main() # runs program

