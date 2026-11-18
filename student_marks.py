name = input("Enter student name: ")

m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))
m4 = int(input("Enter subject 4 marks: "))
m5 = int(input("Enter subject 5 marks: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
