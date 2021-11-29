'''
Golf Scores(Part One)
This is the first part of the program, that will create a program called golf.dat, and give it the data needed.
Programmer: Bertram, Calob
Course:CSC119
'''
#readFile that finds the file and prints it.
def readFile():
    #Trying to open the golf.txt that was made from the previous program.
    try:
        file=open("golf.txt")
    #If there is a error, the program will tell you.
    except:
        print("Cannot open the file.")
        exit(1)
    #Reads line by line in the file.
    for line in file:
        print(line, end='')
    #Close the file.
    file.close()
#This the main function, which creates the file.
def main():
    #Tries to open a file name golf.dat
    try:
        file=open("golf.txt", "w")
    #If there is a error it will let the user know.
    except:
        print("There was a error when writing this file.")
        exit(1)
    #Getting info to put in the file.
    getInfo(file)
    print("The scores you have entered have been displayed as following.")
    readFile()
#getInfo function that gets the users scores and names.
def getInfo(file):
    #Sets a varible that will be more names if the user wants too.
    moreNames='y'
    #While loop that is more names is yes then it will allow the user to enter more scores.
    while moreNames=='y':
        #Gets the name of the user.
        name=input("Please enter the players name: ")
        #Gets the score of the previous name
        score=int(input("Please enter that players score: "))
        #Writes the name first followed by spaces to give it room to the right.
        file.write(name+"   ")
        #Writes the score as a string, and then goes to the next line.
        file.write(str(score)+"\n")
        #For the while loop, if wanted the user can enter more names.
        moreNames=input("Would you like to enter more entries?[y/n]: ")
    #If more names is not a yes, then it will close the file.
    file.close()
    #This is telling the user that the file has been entered into the system.
    print("Your file has been succesfully writen as golf.txt")
#calls the main()
main()
