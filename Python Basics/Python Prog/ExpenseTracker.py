expences = []
budget = float(input(" enter your budget : "))

while True:

  print("--- Expense Tracker ---")
  print(" 1.Add expense")
  print(" 2.View Expenditure")
  print(" 3.Total Calculations")
  print(" 5.Budget veerification")
  print(" 4.Exit")
  print("-----------------------")

  choice = int(input("Enter choise : "))

  if choice == 1:

       catagory = input("Catagory : ")
       price = float(input("Price : "))

       expence={
           "catagory":catagory,
           "price":price
       }

       expences.append(expence)

       print("expense Sucessfully added...")


  elif choice == 2:

        if len(expences) == 0:
            print(" no more expense recorded..")

        print("--- the Expenses are ---")

        for i in expences:
            print(i["catagory"],"$",i["price"])


  elif choice == 3:
      total = 0

      for i in expences:
          total += i["price"]

      print(" Total expense till now :",total)


  elif choice == 4:
      print(" App exited")
      break       

  elif choice == 5:

      total = 0
      for i in expences:
          total += i["price"]
    
      print(" Your budget : ", budget)
      print(" your expense : ", total)
      current_budget = budget - total 
      print(" curr_budget : ", current_budget)           

else:
    price("invalid choice")