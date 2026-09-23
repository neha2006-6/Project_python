import time

def run_quiz():
    # Store questions, options, and correct answers in a list of dictionaries
    quiz_data = [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A) func", "B) def", "C) define", "D) function"],
            "answer": "B"
        },
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A) .pyt", "B) .pt", "C) .py", "D) .python"],
            "answer": "C"
        },
        {
            "question": "Which data type is immutable (cannot be changed after creation)?",
            "options": ["A) List", "B) Dictionary", "C) Set", "D) Tuple"],
            "answer": "D"
        },
        {
            "question": "What does the len() function do?",
            "options": [
                "A) Returns the number of items in an object",
                "B) Measures execution time",
                "C) Converts text to lowercase",
                "D) Generates a random number"
            ],
            "answer": "A"
        }
    ]

    score = 0
    total_questions = len(quiz_data)

    print("==========================================")
    print("      WELCOME TO THE PYTHON QUIZ!        ")
    print("==========================================\n")

    for index, q in enumerate(quiz_data, 1):
        print(f"Question {index} of {total_questions}: {q['question']}")
        for option in q["options"]:
            print(f"  {option}")
        
        # Validate user input to ensure they enter A, B, C, or D
        while True:
            user_answer = input("\nYour answer (A, B, C, or D): ").strip().upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            print("Invalid input! Please choose A, B, C, or D.")

        # Check answer
        if user_answer == q["answer"]:
            print("Correct! 🎉\n")
            score += 1
        else:
            print(f"Wrong! ❌ The correct answer was {q['answer']}.\n")
        
        time.sleep(0.5)

    # Final score summary
    print("==========================================")
    percentage = (score / total_questions) * 100
    print(f"QUIZ FINISHED! Your Score: {score}/{total_questions} ({percentage:.0f}%)")
    
    if percentage == 100:
        print("Perfect score! Excellent work! 🏆")
    elif percentage >= 50:
        print("Good job! Keep practicing! 👍")
    else:
        print("Better luck next time! Keep learning! 📚")
    print("==========================================")

if __name__ == "__main__":
    run_quiz()
