/***database README.txt***/

This is a simple python application that can search, add, or delete entries from a txt file

The db.txt file is formatted specifically to be able to search, like below:
  1 (nothing in this space)
  2 1st person's phone number
  3 1st person's name
  4 2nd person's phone number
  5 2nd person's name
  6...

The python file (named test.py) contains 3 functions: Search, Append and Delete
  Search takes input as name or phone number, and reads the document line by line until it finds a match, then prints out 2 lines with the name and phone number
    There is nothing in the search function as of now to handle multiple entires with the same data
  Append simply takes input, and adds it to the end of the document
  Delete uses the search function to find the values, then changes the values to "" and writes back to the file
