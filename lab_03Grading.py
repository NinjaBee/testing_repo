number_grade = int(input("What was the grade?\n:"))

if number_grade > 90 :
    grade = "Congrats! You got an A!"
    
elif number_grade > 80:
    grade = "Wow! You got a B! Good job."
    
elif number_grade > 70:
    grade = "Slow and steady gets the job done. Good job on that C!"
    
elif number_grade > 60:
    grade = "Uh oh! Looks like you might want to find a tutor. You got a D."
    
elif  number_grade <= 59:
    grade = " Daaang... maybe we should find a study group. That was an F."
    
else:
     grade = "Say wha~~t??"

print(grade)