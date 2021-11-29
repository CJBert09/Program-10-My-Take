'''
Largest Number
Assuming a file name, find the largest number stored in the data.
Programmer: Bertram, Calob
Course:CSC119
'''
#Sets a global size variable to use to step through the array.
SIZE=10
#The findHigh function that will step throughout the array.
def findHigh():
    #This allows the numbers to go inside of the empty list.
    numbers=[]
    #Try-statement that will set the variable file to open and read a given document, in this case the book asks us to user numbers.dat, and the r is for reading.
    try:
        file = open("numbers.dat", "r")
    #Except statement that used a built in python function that will tell the user if there is a problem finding the file, I was not sure of this but in class we used this and this is what I found to work the best.
    except FileNotFoundError:
        print("We can't find a find/open a file with the name numbers.dat")
        #exits the error.
        exit(1)
    #A for loop that counts the numbers and appends them in a lists.
    for line in file:
        #Sets number as a variable and separtes the numbers in the given file.
        number=int(line.rstrip('\n'))
        #Appends the number varible into the numbers[] list.
        numbers.append(number)
    #I set a index or i to zero in order to start at the first element.
    i=0
    #I set the highest varible to hold the beggining number as the highest in order to step through and locate the highest.
    highest=numbers[i]
    #For loop that goes through each of the variables in the array and does what is asked.
    for i in range(SIZE):
        #if statment saying that is this index is greater than the current highest, change that to the highest.
        if numbers[i] > highest:
            highest = numbers[i]
        #Else change the index to go to the next number.
        else:
            i=i+1
    #Return the highest number to the main()
    return highest
    #Close the file.
    file.close()
#Main function that prints all the needed data.
def main():
    #Calls the highest variable back.
    highest = findHigh()
    #Prints the results
    print("The highest number in your list is", highest)
#Calls main()
main()
