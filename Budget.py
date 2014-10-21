#Jcgaither

import time

AdminId = 'Admin1'
AdminPass = '000'

def currentBudget():
    with open ("Currentbudget.txt", "r") as budgetfile:
        currentbalance = int(budgetfile.readline())
        print "Current Balance: %s " % currentbalance
        proceed = raw_input("Finished transaction?(Yes,No)")
        if proceed == 'Yes' or proceed == 'yes':
            budgetfile.close
        elif proceed == 'No' or proceed == 'no':
            print "Closing session......"
            budgetfile.close
            time.sleep(3)
            print "Session closed"
            exit()
        else:
            print "Enter Yes or No"

def addExpense():
    with open("Currentbudget.txt", "r") as budgetfile:
        currentbalance = int(budgetfile.readline())
        expenseamnt = int(raw_input("Input expense amount: "))
        expensefrequency = int(raw_input("Input expense frequency:(per month)"))
        expensetotal = expenseamnt * expensefrequency
        endbalance = (currentbalance - expensetotal)
        if endbalance <= 0:
            print "Negative balance, insufficient funds to cover expenses"
            Continue
        elif endbalance <= 100:
            print "Low balance notice: Current balance: %s" % endbalance
            time.sleep(3)
            print "Process successful..."
            budgetfile.close
        else:
            time.sleep(3)
            print "Process successful..."
            print "Current balance: %s" % endbalance
            budgetfile.close
            

def addRevenue():
    with open("Currentbudget.txt", "r") as budgetfile:
        currentbalance = int(budgetfile.readline())
        revenueamnt = float(raw_input("Input revenue amount: "))
        revenuefrequency = float(raw_input("Input revenue frequency: (per month)"))
        revenuetotal = (revenueamnt * revenuefrequency)
        endbalance = int(currentbalance) + revenuetotal
        time.sleep(3)
        print "Current balance: %s" % endbalance
        print "Process successful..." 
    
print "Budget initializing..."
for i in range (0,5):
    if i == 4:
        print "Invalid Id or password..."
        break
    else: 
        i = i+1
        
        
        idinput = raw_input("Enter ID: ")
        if idinput != AdminId:
            print "Validating..."
            time.sleep(2)
        
    
        passinput = raw_input("Enter password: ")
        if passinput == AdminPass:
            print "Validating..."
            time.sleep(2)
        
        if idinput == AdminId and passinput == AdminPass:
            print "Credentials accepted"
            time.sleep(3)
            print ("""Select a transaction.
                 1. See current balance
                 2. Add expense
                 3. Add revenue
                 4. Exit """)
        
            transaction = int(input("Enter a transaction number: "))

            if transaction == 1:
                currentBudget()
            elif transaction == 2:
                addExpense()
            elif transaction == 3:
                addRevenue()
            elif transaction == 4:
                "Exiting budget application..."
                exit() 
            else:
                exit()
        else:
            "Invalid Id or password..."
    
    
    