print("----------------Student Marks Manager----------------")

    
# Asking user to enter student's name:
# Asking user to enter 3 subjects marks that is obtained for the student:

name = input("Enter Student's name: ")
sub1 = int(input("Enter the marks obtained in Physics: "))
sub2 = int(input("Enter the marks obtained in Chemistry: "))
sub3 = int(input("Enter the marks obtained in Mathematics: "))

# Adding all the 3 subject marks to get the total:
def total():
    Total = sub1 + sub2 + sub3
    return Total

# Taking average of the total marks of 3 subjects:
def average():
    total_marks = total()
    Average = total_marks/3
    Average = float('{:.2f}'.format(Average))
    return Average

# Checking if student has passed or fail:
def result():
    average_marks = average()
    if (average_marks >= 40):
        print(name,  "Your score is", average_marks, "PASS")
        return "PASS"
    else:
        print(name,  "Your score is", average_marks, "FAIL")
        return "FAIL"

result()

with open("Python_Small_Projects/Project_1_Student_Marks/student_details.txt", "a") as f:
    f.write( "Student Name : " + name + " | "),
    f.write( "Physics : " + str(sub1) + " | "),
    f.write( "Chemistry : " + str(sub2) + " | "),
    f.write( "Mathematics : " + str(sub3) + " | "),
    f.write( "Total Marks : " + str(total()) + " | "),
    f.write( "Average : " + str(average()) + " | "),
    f.write( "Result : " + str(result()) + "\n")