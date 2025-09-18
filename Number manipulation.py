bmi = 84 / 1.65 ** 2
print(bmi)
# To make the bmi a interger number, we need to force it with this type when printing
print(int(bmi))
# To make it more precise, we need to house de ROUND function
print(round(bmi))
# If we want a decimal number
print(round(bmi, 2))



# If we a have score, and then we need to accumulate the result, we can use ASSIGNMENT OPERATORS
score = 0

#A user scores a point
score += 1
print(score)


#So if we want to print scores with different data types we can use the "f-String"
score = 0
height = 1.8
is_winning = True
print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")
