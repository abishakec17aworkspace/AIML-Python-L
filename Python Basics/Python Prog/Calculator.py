
while True:
   Num1 = float(input(" Enter the Number : "))
#  Process = input(" Enter the Process (+,-,*,/) :")
   Operator = input(" ADD , SUB , DIV , MUL :")
   Num2 = float(input(" Enter the Number 2:"))


   def  add(a,b):
       return a + b
   
   def sub(a,b):
       return a - b
   
   def mul(a,b):
       return a * b
   
   def div(a,b):
       return a / b
   
   if Operator.lower() == "add":
       print(" Result = ", add(Num1,Num2))
   
   elif Operator.lower() == "sub":
       print(" Result = ", sub(Num1,Num2))
   
   elif Operator.lower() == "mul":
       print(" Result = ", mul(Num1,Num2))
   
   elif Operator.lower() == "div":
   
       if Num2 == 0:
           print(" cannot divisble by Zero..")
       else:    
           print(" Result = ", div(Num1,Num2))        
   
   else:
        Value = " enter the Valid Process"
      
   
   choice = input("If you want to  conntinue ( Yes / No):")
   
   if choice.lower() == "no":
       print(" Calculator is Closed")
       break