
# Taking Input Marks From The User

max_per_sub=int(input("Enter the maximum marks possible in each subject : "))
cs=int(input("Enter your marks in Computer Science : "))
math=int(input("Enter your marks in Mathematics : "))
phy=int(input("Enter your marks in Physics : "))
chem=int(input("Enter your marks in Chemistry : "))
eng=int(input("Enter your marks in English : "))
ped=int(input("Enter your marks in Physical Education : ")) 

# Calculating Maximum Marks, Total Marks, Average Marks, Percentage 
max_marks=max_per_sub*6
total_marks=cs+math+phy+chem+eng+ped
average_marks=total_marks/6
percentage=total_marks/max_marks*100

# Setting up conditions 
if 100>=percentage>90:
    grade="A1"
    remark="Outstanding! Keep up the good work."
elif 91>=percentage>80:
    grade="A2"
    remark="Very Good! You can do even better!"
elif 81>=percentage>70:
    grade="B1"
    remark="Good! But there's room for improvement."
elif 71>=percentage>60:
    grade="B2"
    remark="Ok result, but you can do better."
elif 61>=percentage>50:
    grade="C1"
    remark="Not Good. You have to work even harder."
elif 51>=percentage>40:
    grade="C2"
    remark="Poor Result. A ton of improvement required."
else:
    grade="Below C"
    remark="Maybe you will fail in the finals :/"

# Displaying Result

print("              Your Result\n")
print("Total Marks Scored : ",total_marks,"out of",max_marks)
print("     Average Marks : ",average_marks)
print("        Percentage : ",percentage,"%")
print("             Grade : ",grade,"\n")
print("           Remarks : " + remark,"\n\n")