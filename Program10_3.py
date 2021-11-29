'''
Sum of Numbers
This program will take a assumed file name and take all of the numbers inside of it and then calculate the totals.
Programmer: Bertram, Calob
Course:CSC119
'''
#This is the main function.
def main():
    #This sets the sum off at zero in order to add all the numbers in given file.
    sum=0
    #This is the numbers empty list that allows the file to be put into a array/list
    numbers=[]
    #Try-statement that will set the variable file to open and read a given document, in this case the book asks us to user numbers.dat, and the r is for reading.
    try:
        file = open("numbers.txt", "r")
    #Except statement that used a built in python function that will tell the user if there is a problem finding the file, I was not sure of this but in class we used this and this is what I found to work the best.
    except FileNotFoundError:
        print("We can't find a find/open a file with the name numbers.txt")
        #exits the error.
        exit(1)
    #A for loop that counts the numbers and appends them in a lists.
    for line in file:
        #Sets number as a variable and separtes the numbers in the given file.
        number=int(line.rstrip('\n'))
        #Appends the number varible into the numbers[] list.
        numbers.append(number)
        #Calculates the sum of the number by setting it to zero(earlier) and then adding the numbers one by one.
        sum=sum+number
    #Closes the file.
    file.close()
    #This is the second function that allows us to tell the user the information the program has found.
    tellUser(numbers, sum)
#The tell user fucntion that has parameters of the main()
def tellUser(numbers, sum):
    #Prints the numbers
    print("Your numbers are:", numbers)
    #Tells the user the average of the numbers.
    print("The total of your numbers is:", sum)
#Calls main()
main()
