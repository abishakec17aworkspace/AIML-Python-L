import csv

data =[
    "mouriyaa","26","78","Chennai"
]

with open("student.csv","a",newline="") as file:
    writter = csv.writer(file)  
    writter.writerow(data)

with open("student.csv","r") as file2:
    reader = csv.reader(file2)  
    for text in reader:
        print(text)


# import csv

# data = [["Abishake", "21", "77", "Salem"],
#         ["mouri", "22", "76", "Chennai"]]

# with open("test_student.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerow(["Name", "Age", "Marks", "City"])
#     writer.writerows(data)


# with open("test_student.csv", "r", newline="") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)