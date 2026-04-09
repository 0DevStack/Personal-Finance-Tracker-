#Expense Tracker Project

expenses=[] #list of  expenses in form of dictionary
print("Welcoe to Expense Tracker:Save Money For Future")

while True:
    print("====MENU====")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.Total Soending")
    print("3.Exit")

    choice=int(input("Enter your choice(1/2/3/4):"))
    if (choice==1):
        date=input("Date of Spending Money:")
        category=input("Spent Money on Which Category:")
        description=input("Enter Short Description:")
        amount=float(input("Enter Amount Spent:"))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expenses.append(expense)
        print("Expense Added Successfully")

#2. view all Expenses
    elif (choice==2):
        if (len(expenses)==0):
            print("No Expenses Found")
        else:
            print("====EXPENSES====")
            count=1
            for expense in expenses:
                print(f"Kharch Number {count} ->{expense['date']},{expense['category']},{expense['description']},{expense['amount']}")
                count+=1

#3. View Total Spending
    elif (choice==3):
        total=0
        for expense in expenses:
            total=total+expense["amount"]

        print("Total Expense=",total)

#4.EXIT
    elif(choice==4):
        print("Thank You")
        break
    else:
        print("Invalid Choice")



        




