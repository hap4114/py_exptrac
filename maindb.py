#Creating a expense tracker application using datbase but no GUI 

#importing SQlite 
import sqlite3

# Connect to SQLite database 
conn = sqlite3.connect("expenses.db")

#establishing cursor connection for controling structure and traversal of database
cur = conn.cursor()

# Create expenses table if it does not exist
cur.execute("""CREATE TABLE IF NOT EXISTS expenses 
               (id INTEGER PRIMARY KEY,
                category TEXT,
                amount REAL)""")

#commit for creating the database
conn.commit()

#Print Elements 
def pri_men():
    print("Please choose from one of the following  :")
    print("1 : Add new Expense")
    print("2 : Remove an Expense")
    print("3 : List all Expense")

#Function for Adding the expenses 
def add_exp():

    #Taking input from the user
    cat = input("Enter The Category : ")

    # Convert input to float
    amt = float(input("Enter the Amount spend : "))  
    
    # Insert expense into SQLite database and commiting it
    cur.execute("INSERT INTO expenses (category, amount) VALUES (?, ?)", (cat, amt))
    conn.commit()


#Displaying the expenses 
def list_exp():
    #
    cur.execute("SELECT * FROM expenses")
    print("Here is list of Expense You Have")
    print("------------------------------------------------")
    print("Sr.no  Category  Amount")

    #counter for increment 
    count = 1

    #for fetching the data
    for row in cur.fetchall():
        print(count, "    ", row[1], "    ", row[2])
        count += 1

#Remove the expense
def rem_exp():
    list_exp()
    print("What Expense would you like to remove ?")
    try:
        exp_to_rem = int(input("> "))
        
        # Fetch expense id for deletion
        cur.execute("SELECT id FROM expenses")
        expense_ids = [row[0] for row in cur.fetchall()]
        
        # Check if selected expense number is valid
        if 1 <= exp_to_rem <= len(expense_ids):

            # Delete expense from SQLite database and commit the change 
            cur.execute("DELETE FROM expenses WHERE id = ?", (expense_ids[exp_to_rem - 1],))
            conn.commit()

        #For invalid entry 
        else:
            print("Invalid Input !!!! Please Try Again")

    #for invalid entry
    except:
        print("Invalid Input !!!! Please Try Again")

#The main function
def main():

    #Declaration for the loop 
    a = 1

    #loop for continious entry
    while a == 1:

        #print menu and select option
        pri_men()
        opt_sel = int(input("Enter your option : "))

        #for adding 
        if opt_sel == 1:
            add_exp()

        #for removing 
        elif opt_sel == 2:
            rem_exp()

        #for displaying 
        elif opt_sel == 3:
            list_exp()

        #for continouing or not
        a = int(input("Do you wish to continue?? \n1 : Yes \n0 : No \n> "))

# To run the Main function
if __name__ == "__main__":
    main()

# Close SQLite connection when done
conn.close()
