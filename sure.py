
# Creates the dictionary to store responses.
answers = {}
print("New Entry! Please Answer the questions below")
'''
Below, write code that will pose the survey questions from the student prompt
to a user. Your program should save user input as a dictionary.
'''
survey = [
    "What is your name?",
    "How old are you?",
    "What is your hometown?",
    "What is your date of birth? (MM/DD/YYYY)"]

keys = ["name", "age", "hometown", "DOB"]

list_of_answers = []
 done = "NO"
 while done =="NO":
# store answers for dictionary


for x in range(len(survey)):
    response = input(survey[x] + "your answer: ")
    answers[keys[x]] = response

# Print the context of the dictionary.
print(answers)
