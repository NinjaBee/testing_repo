number_grade = int(input("What was the grade?\n:"))

plus_minus = number_grade % 10 

if plus_minus <= 3:
    plus_minus = "-"

elif 3 < plus_minus < 7:
    plus_minus = ""

else:
    plus_minus = "+"


if number_grade > 90 :
    grade = "Congrats! You got an A" + plus_minus + "!"
    
elif number_grade > 80:
    grade = "Wow! You got a B" + plus_minus + "! Good job."
    
elif number_grade > 70:
    grade = "Slow and steady gets the job done. Good job on that C" + plus_minus + "!"
    
elif number_grade > 60:
    grade = "Uh oh! Looks like you might want to find a tutor. You got a D" + plus_minus + "."
    
elif  number_grade <= 59:
    grade = " Daaang... maybe we should find a study group. That was an F" + plus_minus + "."
    
else:
     grade = "Say wha~~t??"

print(grade)