def kbc_game():
    question = "Which team is the world T20 champions of 2024?"
    
    options = {
        "A": "India",
        "B": "South Africa",
        "C": "Australia",
        "D": "England"
    }

    correct_answer = "A"

    print(question)

    for option, answer in options.items():
        print(f"{option}. {answer}")
    user_choice = input("Enter your choice (A/B/C/D): ").upper()

    if user_choice==correct_answer:
        print("Congratulation!! You won")
    else:
       print("oops!! you lost correct ans is A")

kbc_game()

print("Thank you")







# Sample questions and options
questions = [
    "What is the capital of France?",
    "Which planet is closest to the Sun?",
    "Who wrote 'Romeo and Juliet'?",
    #Add more questions here...
]

options = [
    ["Paris", "London", "Berlin", "Madrid"],
    ["Mercury", "Venus", "Earth", "Mars"],
    ["Shakespeare", "Dickens", "Hemingway", "Twain"],
    #Add more options here...
]

#Prize money
prize = 1000

for i, question in enumerate(questions):
    print(f"\nQ{i + 1}: {question}")
    for j, option in enumerate(options[i]):
        print(f"{j + 1}. {option}")

    user_choice = input("Your answer (1-4): ")
    correct_answer = 1  # Assume the first option is correct

    if user_choice == str(correct_answer):
        print(f"Correct! You won ₹{prize}")
        prize *= 2  # Double the prize for the next question
    else:
        print(f"Wrong! Game over. You won ₹{prize}")
        break

print("\nThanks for playing KBC!")



