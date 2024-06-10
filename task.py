quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Southern Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "What is the powerhouse of the cell?",
        "options": ["A. Nucleus", "B. Ribosome", "C. Mitochondria", "D. Golgi apparatus"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'To be, or not to be'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
        "answer": "B"
    }
]

def ask_question(question):
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)
    user_answer = input("Please enter the letter of your answer: ").upper()
    return user_answer

def check_answer(question, user_answer):
    return user_answer == question["answer"]

def display_score(score, total_questions):
    print(f"\nYour final score is: {score}/{total_questions}")

def run_quiz():
    score = 0
    total_questions = len(quiz_questions)
    print(f"\nStarting the quiz... Total questions: {total_questions}\n")
    
    for question in quiz_questions:
        user_answer = ask_question(question)
        if check_answer(question, user_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {question['answer']}.\n")
    
    display_score(score, total_questions)

if __name__ == "_main_":
    run_quiz()