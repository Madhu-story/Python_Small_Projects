print("----------------Student Marks Manager----------------")

# Asking user to enter student's name:
name = input("Enter Student's name: ")

# Asking user to enter 3 subjects marks that is obtained for the student:
sub1 = int(input("Enter the marks obtained in Physics: "))
sub2 = int(input("Enter the marks obtained in Chemistry: "))
sub3 = int(input("Enter the marks obtained in Mathematics: "))

# Adding all the 3 subject marks to get the total:
Total = sub1 + sub2 + sub3

# Taking average of the total marks of 3 subjects:
average = Total/3

# Checking if student has passed or fail:
if (average >= 40):
    print(name,  "Your score is", average)
    print('"PASS"')
else:
    print(name,  "Your score is", average)
    print('"FAIL"')