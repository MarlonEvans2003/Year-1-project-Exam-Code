import pandas as pd                 ### Import library for Pandas
import datetime                     
import matplotlib.pyplot as plt     ### Import library for graphs
import getpass                      ### This imports getpass function to hide password
import sys                          ### This imports sys functions to exit program

def startmenu():
    print("#########################################################")      ### welcome Menu
    print("#                                                       #")
    print("#                                                       #")
    print("#   Welcome to KRJ inventory checker!                   #")
    print("#                                                       #")
    print("#   To get started please login:                        #")
    print("#                                                       #")
    print("#                                                       #")
    print("#########################################################")


def login():                        ### This section reads the login values from a txt file
    username = input("Username: ")
    password = getpass.getpass("Password: ") ### getpass function hides user input for security
    f = open("logindetails.txt", "r")
    for line in f.readlines():
        us, pw = line.strip().split("|")
        if (username in us) and (password in pw): ### Username and password validation
            print ("Login successful!")
            return True
        else:
            print ("Wrong username/password")
            return False

def logingate():            ### Checks and validates that the credentials are correct
    count = 1               ### Counts the number of attempts
    validate = True
    while validate == True:
        log = login()
        if log == True:
            validate = False
            break
        if count == 3:   
            exit = input("Access denied due to excessive login attempts. Please press enter to exit: ") ### Locks user out after 3 attempts
            sys.exit() ### Exits the program
        else:
            print("Wrong credentials. Please try again:")
            count = count + 1

def profit_loss_menu():  ### Function for user input on what they want to do
    flag = True
    while flag:
        print("#########################################################")
        print("#  Welcome! Please choose an option from the list       #")
        print("#  1. Show profit/loss for specific products            #")
        print("#  2. Show profit/loss for all products                 #")
        print("#  3. Show profit/loss for certain supplier             #")
        print("#########################################################")

        profit_loss_choice = input("Please enter the number of your choice (1-3): ")

	      # This code tries to convert the input into an int
	      # if it fails, the except: path is executed, otherwise the else path
        try:  
            int(profit_loss_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(profit_loss_choice) < 1 or int(profit_loss_choice) > 3:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(profit_loss_choice) 


def get_supplier_choice():       ### Supplier choice Function
    validation = True
    while validation == True:
        print("#########################################################")
        print("# Please choose a supplier from this list:              #")
        print("# Please enter a number between ()                      #")
        print("# 1. Farm Direct                                        #")
        print("# 2. Natural Best                                       #")
        print("# 3. Nature Food                                        #")
        print("# 4. Grocers Int                                        #")
        print("# 5. Clean living                                       #")
        print("#########################################################")
        supplier_list = ["Farm Direct", "Natural Best", "Nature Food", "Grocers Int.", "Clean Living"]

        supplier_choice = input("Please enter the number of your choice (1-5): ")
        #### This checks the input is an integer
        try:
            int(supplier_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(supplier_choice) < 1 or int(supplier_choice) > 5:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                supplier_name = supplier_list[int(supplier_choice)-1]
                return supplier_name



def get_product_choice():          ### Lists produce the user can choose from
    flag = True
    while flag:
        print("#########################################################")
        print("#Please choose a product from the list:                 #")
        print("#Please enter the number of the product (1-16)          #")
        print("# 1.  Potatoes                                          #")
        print("# 2.  Carrots                                           #")
        print("# 3.  Peas                                              #")
        print("# 4.  Lettuce                                           #")
        print("# 5.  Onions                                            #")
        print("# 6.  Apples                                            #")
        print("# 7.  Oranges                                           #")
        print("# 8.  Pears                                             #")
        print("# 9.  Lemons                                            #")
        print("# 10. Limes                                             #")
        print("# 11. Melons                                            #")
        print("# 12. Cabbages                                          #")
        print("# 13. Asparagus                                         #")
        print("# 14. Broccoli                                          #")
        print("# 15. Cauliflower                                       #")
        print("# 16. Celery                                            #")
        print("#########################################################")

        product_list = ["Potatoes", "Carrots", "Peas", "Lettuce", "Onions", 
"Apples", "Oranges", "Pears", "Lemons", "Limes","Melons", "Cabbages", 
"Asparagus", "Broccoli", "Cauliflower", "Celery"]

        product_choice = input("Please enter the number of your choice (1-16): ")
	      # This checks the input is an integer
        try:
            int(product_choice)
        except:
            print("Sorry, you did not enter a valid choice")  ### Gives error message if they enter a value that is not between 1 and 16
            flag = True
        else:
            if int(product_choice) < 1 or int(product_choice) > 16:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                product_name = product_list[int(product_choice)-1]
                return product_name

def get_start_date():
    flag = True
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) ')
        # This checks the start date is a valid date
        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            start_date_return = pd.to_datetime(start_date, dayfirst=True)
            if (pd.isnull(start_date_return) == True):
                print("Sorry, you did not enter a valid date")
                flag = True
            else:
                return start_date_return

def get_end_date():
    flag = True
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) ')
        # This checks the end date is a valid date
        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            end_date_return = pd.to_datetime(end_date, dayfirst=True)
            if (pd.isnull(end_date_return) == True):
                print("Sorry, you did not enter a valid date")
                flag = True
            else:
                return end_date_return

def get_date_range_all():
    # df1 is a pandas data frame being created from a csv file
    df1 = pd.read_csv("Task4a_data.csv") 

    df1["Date"] = pd.to_datetime(df1["Date"], dayfirst=True) # convert Date column to be a datetime object

    # This selects all the rows between the dates and removes the Supplier column completely
    # results is another data frame
    results = df1.loc[(df1["Date"] >= start_date) & (df1["Date"] <= end_date), df1.columns != "Supplier"].copy()
    
    # Calculate some new columns from existing columns
    results["Cost Subtotal"] = results["KGs Purchased"] * results["Purchase Price"]
    results["Sales subtotal"] = results["KGs Sold"] * results["Selling Price"]
    results["Profit subtotal"] = results["Sales subtotal"] - results["Cost Subtotal"]
    
    total = round(results["Profit subtotal"].sum(),2)
    
    # The to_string function just makes the Pandas data frame look nice
    # without the index (index = False)
    results_print = results.to_string(index=False)
    print(results_print)

    # The format function is just a convenient way to make a string to print out
    # Anything between the {} is replaced with the value of the variables that are passed to the string
    print("The overall profit/loss for the selected time frame was £{}".format(total))

def get_date_range_product():            ### Function to see products
    product_name = get_product_choice()
    # df2 is a pandas data frame from the complete csv file
    df2 = pd.read_csv("Task4a_data.csv") 

    df2["Date"] = pd.to_datetime(df2["Date"], dayfirst=True) # convert Date column to be a datetime object

    # This selects all the rows in the data frame between the dates and for the chosen product 
    # and makes a new data frame called product_results
    product_results = df2.loc[(df2["Date"] >= start_date) & (df2["Date"] <= end_date) & (df2["Product"] == product_name)].copy()

    # Calculate some new columns from existing columns
    product_results["Cost Subtotal"] = product_results["KGs Purchased"] * product_results["Purchase Price"]
    product_results["Sales subtotal"] = product_results["KGs Sold"] * product_results["Selling Price"]
    product_results["Profit subtotal"] = product_results["Sales subtotal"] - product_results["Cost Subtotal"]
    
    total = round(product_results["Profit subtotal"].sum(),2)
    # The to_string function just makes the Pandas data frame look nice
    results_print = product_results.to_string(index=False)
    
    print(results_print)        
    product_results.sort_values(by="Date", inplace = True)
    plt.plot(product_results["Date"], product_results["Profit subtotal"]) ### Graph for the profit/loss on chosen products
    plt.xticks(rotation=90)
    plt.xlabel("Date")
    plt.ylabel("Profits")
    plt.title("Profit/Loss for chosen Product(s)")
    plt.show()
    #
    plt.plot(product_results["Date"], product_results["KGs Sold"]) ### Graph for the quantity on chosen products
    plt.xticks(rotation=90)
    plt.xlabel("Date")
    plt.ylabel("Quantity")
    plt.title("Quantity for chosen product(s)")
    plt.show()
    # The format function is just a convenient way to make a string to print out 
    # Anything between the {} is replaced with the value of the variables that are passed to the string
    print("The profit/loss for the {} for the selected time frame was £{}".format(product_name, total))

def get_date_range_supplier():                     ### Function to see only supplier's action
    supplier_name = get_supplier_choice()
    # df2 is a pandas data frame from the complete csv file
    df2 = pd.read_csv("Task4a_data.csv")


    df2["Date"] = pd.to_datetime(df2["Date"], dayfirst=True) # convert Date column to be a datetime object

    # This selects all the rows in the data frame between the dates and for the chosen product
    # and makes a new data frame called product_results
    supplier_results = df2.loc[(df2["Date"] >= start_date) & (df2["Date"] <= end_date) & (df2["Supplier"] == supplier_name)].copy()

    # Calculate some new columns from existing columns
    supplier_results["Cost Subtotal"] = supplier_results["KGs Purchased"] * supplier_results["Purchase Price"]
    supplier_results["Sales subtotal"] = supplier_results["KGs Sold"] * supplier_results["Selling Price"]
    supplier_results["Profit subtotal"] = supplier_results["Sales subtotal"] - supplier_results["Cost Subtotal"]
   
    total = round(supplier_results["Profit subtotal"].sum(),2)
    # The to_string function just makes the Pandas data frame look nice
    results_print = supplier_results.to_string(index=False)
   
    print(results_print)
    supplier_results.sort_values(by="Date", inplace = True)
    plt.plot(supplier_results["Date"], supplier_results["Profit subtotal"]) ### Graph for the profit/loss on chosen supplier
    plt.xticks(rotation=90)
    plt.xlabel("Date")
    plt.ylabel("Profits")
    plt.title("Profit/Loss for chosen supplier(s)")
    plt.show()
    #
    plt.plot(supplier_results["Date"], supplier_results["KGs Sold"]) ### Graph for the quantity on chosen supplier
    plt.xticks(rotation=90)
    plt.xlabel("Date")
    plt.ylabel("Quantity")
    plt.title("Quantity for chosen supplier(s)")
    plt.show()
    # The format function is just a convenient way to make a string to print out
    # Anything between the {} is replaced with the value of the variables that are passed to the string
    print("The profit/loss for the {} for the selected time frame was £{}".format(supplier_name, total))



def process_menu_choice():          ### depending on what user chooses, goes to the correct function.
    if profit_choice == 1:
        get_date_range_product()
    if profit_choice == 2:
        get_date_range_all()
    if profit_choice == 3:
        get_date_range_supplier()


##############################
#
#
#       MAIN MENU
#
#
##############################

### Functiongs getting called.. otherwise nothing shows up

Flag = True

while Flag:                                                                     ### While loop to allow the user to repeat and choose another option
    start = startmenu()
    logingatecall = logingate()

    profit_choice = profit_loss_menu()
    start_date = get_start_date()
    end_date = get_end_date()
    pres = process_menu_choice()
    again = input("Do you want to choose another option? Type yes or no: ")
    again = again.lower()                                                           ### .lower() changes the value to lowercase so that even capitalised version of no still works.
    if again == "no":
        print("Goodbye, have a nice day!")                                          ### Making Flag = False breaks the loop.
        Flag = False