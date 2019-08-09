# --- Define your functions below! ---

# The chatbot introduces itself and gives the user instructions.
def intro():
        print("hi,my name is Chatbox1000.")
        # while true:
        #     answer=input()
# Choose a response based on the user's input.
def process_input(answer):
    if answer in listhello:
        greeting()
    else:
        default()
  # Define a list of possible ways the user might say hello.
listhello = ["hi", "hello", "hii", "hola", "sup","wassup","what's up","greetings","hey there"]
#listhello=""
  # Define a list of possible ways the user might say bye.
listbye = ["bye", "goodbye", "adios","peace","lates","byee"]
# listbye=""
    # The chatbot will continue asking for user input.
#define a list of possible way the user might say yes.
listyes=["sure", "yes", "go","si"]

# Display a greeting message to the user.
def greeting():
    print("hey there!")
while True:
    askjoke()
# Display a farewell message to the user.
def farewell():
    print("see ya later alligator :P")

# Tell the user an interactive knock-knock joke.
def askjoke():
    print("do you want to hear a knock knock joke?")
#if user wants to hear knock joke
 valid_responses = ["little old lady who", "little old lady who?"]
  done = False
  while not done:
    answer = input("Little old lady. ")
    if not is_valid_input(answer.lower(), valid_responses):
      print("No, you're supposed to say, 'Little old lady who?'")
    else:
      done = True




  # "Knock knock!" "Who's there"?
def joke():

  # "Little old lady." "Little old lady who?"


  # Say the punchline!

# Display a default message to the user.
def default():
    print("that's cool")
# Check if user_input matches one of the elements in valid_responses.
#
      # If you find a matching response, the input is valid for this kind of response.

  # If you didn't find a matching response, after going through the entire list, the input isn't valid for this kind of response.

# --- Put your main program below! ---
def main():
  intro()
  while True:
    answer = input("(What will you say?) ")
    process_input(answer)



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
