#Expense Tracker without GUI and DataBase

#Expense for list
Expenses = []

#Print Elements 
def pri_men():
    print("Please choose from one of the following  :")
    print("1 : Add new Expense")
    print("2 : Remove an Expense")
    print("3 : List all Expense")

#Adding a new expense
def add_exp():
    #Taking the input of category and amount of expense
    cat = input("Enter The Category : ")
    amt = input("Enter the Amount spend : ")

    #Adding them in list in form of dictonary
    expense = { "category" : cat , "amount" : amt}

    #adding the dictonary in the list using append function
    Expenses.append(expense)

#Remove an Expense 
def rem_exp():
        #Printing the list of expense 
        list_exp()
        print("What Expense would you like to remove ?")

        #For chosing which expense user wants to remove
        try:
            exp_to_rem = int(input("> "))
            del Expenses[exp_to_rem - 1]

        #If tried an invalid option 
        except:
            print("Invalid Input !!!! Please Try Again")

#List The Expense 
def list_exp():

    #For printing purpose 
    print("Here is list of Expense You Have")
    print("------------------------------------------------")
    print("Sr.no  Category  Amount")

    #Counter variable 
    count = 1

    #Printing the list of elements 
    for expense in Expenses :
        print(count , "    " ,expense['category'] ,"    ",expense['amount'])
        count +=1

#main function
def main():

    #making the variable True 
    a = 1

    #loop for continous running the main fuction 
    while a == 1 :

        #printing the menu 
        pri_men()

        #Taking the option the user wants to do 
        opt_sel = int(input("Enter the your option : "))
        
        #if the user wants to add the expense
        if opt_sel == 1 :
            add_exp()

        #If the user wants to remove the expense
        elif opt_sel == 2 :
            rem_exp()

        #If the user wants to list the expense 
        elif opt_sel == 3 :
            list_exp()

        #to continue the operation 
        a = int (input("Do you wish to continue?? \n1 : Yes \n0 : N0 \n> "))

#Run the main Function
if __name__ == "__main__":
    main()
        