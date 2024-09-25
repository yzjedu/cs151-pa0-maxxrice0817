#Programer: Max Rice Problem: 
# Calculate grade needed on final weighted 20% to get 90% in whole course
Current_Grade = float(input("Current Grade: "))
#My sisters goal was to get a 90% on the grade
Desired_Grade = 90
#Test was weighted 20% so I made it 0.2 so it would work with the calculation
Final_Exam_Weight = 0.20


print("You will need at least a:",((Desired_Grade - ((1 - Final_Exam_Weight) * Current_Grade)) / Final_Exam_Weight))


