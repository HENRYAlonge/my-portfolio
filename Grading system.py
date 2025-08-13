#Grading system
grades = ("A","B","C","D","F")
score= float(input("Input student score:"))
if 0 <= score <= 59:
    print(f"you have an {grades[4]} Grade")
elif 60 <= score <= 69:
    print(f"you have an {grades[3]} Grade")
elif 70 <= score <= 79:
    print(f"you have an {grades[2]} Grade")
elif 80 <= score <= 89:
    print(f"you have an {grades[1]} Grade")
elif 90 <= score <= 109:
    print(f"you have an {grades[0]} Grade")
else:
    print("Invalid score")