'''
Sales Report
This will be a program that prints the given information in the way explained in the book.
Programmer: Bertram, Calob
Course:CSC119
'''
#This is not complete because I could not figure it out, I emailed you asking you to talk after class, thank you.
def readFile():
    file=open("brewsters.txt","r")
    empDetails=[]
    #for line in infile.readlines():
#This is the function that will display the chart to the user.      
def chart():
    #The next 4 lines are copied from the book, I did not know how many equal signs went across on the book, but 40 looked close.
    print("Brewster's Used Cars, Inc.")
    print("Sales Report")
    print("Salesperson ID",(' '*3),"Sale Amount")
    print('='*40)
    #Set totalSales as 0 because we want to start fresh to add the salesmen too.
    totalSales=0
    #A for loop for the imported infile.
    for emp, sales in empDetails():
        #Prints the sales from each saleperson ID
        for sale in sales:
            print(emp,(' '*7),"($,.2f)",sales)
        #Prints the total per salesperson.        
        print("Total sales for this salesperson: $",(",.2f"),sum(amounts))
        print()
        #totalSales that gathers all of the combined and puts them together.
        totalSales+=sum(sales)
    #Prints the total sales.
    print("Total of all sales: $",(",.2f"),totalAmount)
#Main function 
def main():
    #Calls the two functions to execute the code.
    readFile()
    chart()
#Calls main()
main()
