import random

QUESTIONS = [
    {
        "question": "What does CPU stand for?",
        "choices": ["A. Central Processing Unit", "B. Computer Personal User", "C. Central Program Utility", "D. Control Processing User"],
        "answer": "A",
    },
    {
        "question": "Which language is this project written in?",
        "choices": ["A. Java", "B. Python", "C. HTML", "D. C++"],
        "answer": "B",
    },
    {
        "question": "What does RAM help a computer do?",
        "choices": ["A. Store temporary data for programs", "B. Print documents", "C. Connect to Wi-Fi only", "D. Turn electricity into sound"],
        "answer": "A",
    },
    {
        "question": "Which one is a web browser?",
        "choices": ["A. Windows", "B. Python", "C. Google Chrome", "D. Microsoft Word"],
        "answer": "C",
    },
    {
        "question": "What symbol starts a comment in Python?",
        "choices": ["A. //", "B. #", "C. <!--", "D. **"],
        "answer": "B",
    },
    {
        "question": "What is used to store multiple values in a Python list?",
        "choices": ["A. Square brackets []", "B. Curly brackets {}", "C. Parentheses ()", "D. Angle brackets <>"],
        "answer": "A",
    },
    {
        "question": "What does AI stand for?",
        "choices": ["A. Automatic Internet", "B. Artificial Intelligence", "C. Advanced Input", "D. Applied Information"],
        "answer": "B",
    },
    {
        "question": "Which device is mainly used to move the pointer on a computer screen?",
        "choices": ["A. Keyboard", "B. Monitor", "C. Mouse", "D. Printer"],
        "answer": "C",
    },
]

def ask_question(number, question_data):
    print(f"\nQuestion {number}: {question_data['question']}")
    for choice in question_data["choices"]:
        print(choice)

    while True:
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        if answer in {"A", "B", "C", "D"}:
            return answer
        print("Please enter A, B, C, or D.")

def play_game():
    questions = QUESTIONS.copy()
    random.shuffle(questions)
    score = 0

    print("\n" + "=" * 45)
    print("        TECHNOLOGY QUIZ GAME")
    print("=" * 45)
    print("Answer the questions and see your score!")

    for number, question in enumerate(questions, start=1):
        answer = ask_question(number, question)
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Not quite. The correct answer was {question['answer']}.")

    percentage = score / len(questions) * 100

    print("\n" + "=" * 45)
    print("              RESULTS")
    print("=" * 45)
    print(f"You scored {score}/{len(questions)} ({percentage:.0f}%).")

    if percentage == 100:
        print("Excellent! You got every question right!")
    elif percentage >= 80:
        print("Great job!")
    elif percentage >= 60:
        print("Good effort! Keep practicing.")
    else:
        print("Keep practicing and try again!")

def main():
    while True:
        print("\n1. Start Quiz")
        print("2. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Thanks for playing!")
            break
        else:
            print("Please choose 1 or 2.")

if __name__ == "__main__":
    main()
