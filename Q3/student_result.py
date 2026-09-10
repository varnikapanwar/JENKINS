import sys

marks1 = float(sys.argv[1])
marks2 = float(sys.argv[2])
marks3 = float(sys.argv[3])

total = marks1 + marks2 + marks3
average = total / 3

print("Subject 1 Marks:", marks1)
print("Subject 2 Marks:", marks2)
print("Subject 3 Marks:", marks3)

print("Total Marks:", total)
print("Average Marks:", average)

if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")