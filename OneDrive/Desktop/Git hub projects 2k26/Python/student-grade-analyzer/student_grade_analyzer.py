# To input number of students 
n = int(input("Enter the number of students: "))

# List to store student details
s=[]

# Loop to take details for each student
for i in range(n):
    student_name = input("Enter the Student "+ str(i+1) + " name:")
    maths,python,oops=map(int,input("Enter the Marks of the subject Maths, Python , Oops:").split())
    total = maths + python + oops
    average = round(total/3,2)

    # Assign grade based on average and subject passing marks 
    if maths < 40 or python < 40 or oops < 40:
        grade = "F"
    elif average>=90:
        grade = "A"
    elif average >=80:
        grade = "B"
    elif average >=70:
        grade = "C"
    elif average >=60:
        grade = "D"
    else:
        grade = "F"   

    # Stores student details in the list    
    s.append([student_name,total,average,grade])

# Displays details in table format
print("--------------------------------------")
print("\t STUDENT DETAILS")
print("--------------------------------------") 
print("Name\tTotal\tAverage\tGrade")

# Print each student's details
for name,total,average,grade in s :
    print(name.upper(),"\t",total,"\t",average,"\t",grade)
    
