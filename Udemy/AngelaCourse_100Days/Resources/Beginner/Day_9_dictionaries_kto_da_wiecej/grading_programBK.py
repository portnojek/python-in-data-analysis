student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
    
    if (student_scores[key]) < 70:
        student_scores[key] = "Fail"
    elif 71 <= (student_scores[key]) <= 80:
        student_scores[key] = "Acceptable"
    elif 81 <= (student_scores[key]) <= 90:
        student_scores[key] = "Exceeds Expectations"
    else:
        student_scores[key] = "Outstanding"
        
    student_grades[key] = student_scores[key]

# 🚨 Don't change the code below 👇
print(student_grades)

