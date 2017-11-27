#Campaign Finance PA6

##Problem
Campaign finance is in the news every election. Who is funding campaigns? How much money are they giving?
In this PA you will develop a program to answer these types of questions, and test it on a file with 3 weeks of data.

##Details
You must create a program that can read in all data from the file, store it in a list, and then answer questions about that data.

###File Info
The file has the following values comma-delimited:
0* Committee name (where money was donated to)
1* Entity making the donation (individual, organization, etc)
2* Contributor's first name
3* Contributor's last name
4* Contributor's city
5* Contributor's state
6* Contributor's employer
7* Contributor's occupation
8* Amount of money they've donated so far this year ("year to date")
9* Date of their donation
10* Amount of money donated on this date

The user chooses the name of the file to input. You are provided with a large file that has lots of data.
Your data is from the 3 weeks leading up to election day (10/18/16 - 11/08/16).
Your data is from the Federal Election Commission.

###Program Abilities
Your program must answer the following questions:
* How did the amount of donations change over time? Create a graph that displays the total number of donations made each day leading up to the election, ordered by day.
* Which committees received the most money? Output to a file the list of each committee and the total money they received.
* How many people donated from a particular employer? (user provides the name of the employer)
* A question of your choosing!

The user is provided with a menu to choose among the options, and they may continue choosing until they choose to quit.

If you have a group of 3, you will also need to answer the following questions:
* A question of your choosing!
* A question of your choosing!

###Error Checking
You do not need to error check the employer input by the user.
However, you do have missing data in your file. The only missing data is in strings, which will appear as "" (empty string or whitespace) in your data.
There is no missing data in fields that are numerical.
