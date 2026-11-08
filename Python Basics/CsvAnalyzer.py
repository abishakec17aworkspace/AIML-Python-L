import csv

with open("student.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    total = 0
    count = 0
    nameList = []



    for text in reader:
        name = text[0]
        age = text[1]
        city = text[3]
        marks = int(text[2])
        total += 1

        print("name:",name)
        print("age:",age)
        if marks >=70:
          print("marks: ", marks)
          print("your pass...")
          count +=1
        else:
           print("mark: ",marks)
           print("your are fail...")
        print()

        if marks<=90 and city.lower()=="salem":
            nameList.append(text)
        # else:
        #     nameList.append(" no such student...")           
 
print("--- overall data ---")
print(" total pass count: ",count )
failCount = total-count
print(" total fail count: ", failCount)
print(" valid applicant: ", nameList)
print()

print("--- valid AApplicant\'s are ---")
for validApplicant in nameList:
   print("Name: ",validApplicant[0],"\n","Age:",validApplicant[1],"\n","Marks:",validApplicant[2],"\n","City:",validApplicant[3])


        
         