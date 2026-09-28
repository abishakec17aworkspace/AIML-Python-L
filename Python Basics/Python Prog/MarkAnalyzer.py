print("--- Student mark analyzer ---")
Marks= []
for i in range(5):
    marks = int(input(" Enter MArks.."))
    Marks.append(marks)

print(" Marks :", Marks)

Total = sum(Marks)  
average = Total/len(Marks)
Highest = max(Marks)
Lowest = min(Marks)

Pass_count = 0
Fail_count = 0

for i in Marks:
    if i >= 40:
        Pass_count += 1
    else:
        Fail_count += 1

print("--- Analyzed value ---")

print("marks :", Marks)
print("Total :",Total)
print("Avg :",average)
print("Highest :", Highest)
print("Lowest :", Lowest)
print("Pass_count :", Pass_count)
print("Fail_count :", Fail_count)
