Num1 = float(input(" Enter the Number : "))
Process = input(" Enter the Process (+,-,*,/) :")
Num2 = float(input(" Enter the Number 2:"))

Operator = input(" ADD , SUB , DIV , MUL")

def  add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

if Operator == "add":
    print(" Result = ", add(Num1,Num2))



if Process == "+":
    Value = Num1 + Num2

elif Process == "-":
    Value = Num1 - Num2   

elif Process == "*":
    Value =  Num1 * Num2

elif Process == "/":
    Value = Num1 / Num2

else:
     Value = " enter the Valid Process"

print("Result = ", Value)      