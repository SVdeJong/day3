# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()

first_digit = 0
second_digit = 0

first_test = ["t", "r", "u", "e"]
second_test = ["l", "o", "v", "e"]

for i in lower_name1:
  if str(i) in first_test:
    first_digit += 1
  if str(i) in second_test:
    second_digit += 1

for i in lower_name2:
  if str(i) in first_test:
    first_digit += 1
  if str(i) in second_test:
    second_digit += 1

love_score = str(first_digit) + str(second_digit)
love_score_int = int(love_score)

if love_score_int < 10 or love_score_int > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score_int > 40 and love_score_int < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")

#print(love_score)
# my answer is different from the answer given in the course, since I already have some knowledge of for-loops. 
# one flaw in the code is if the first and/or second digit get a score of 10. Real world suggest this should be a 0 to 100 score, but this will then be exceeded. But the setup of the excercise is such that 1010 would be a valid score. Since it's outside the scope of the excercise, I'll leave it like this for now. 
