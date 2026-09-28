Marks = [30,40,50,60,70]

for mark in Marks:

    if mark>=60:
        print(mark,"Pass",end=" ")

    else:
        print(mark,end=" ")    


i=0
while i < len(Marks):
    if Marks[i] >= 60:
        print(Marks,"pass")