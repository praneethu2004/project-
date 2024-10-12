class Quiz:
    def __init__(self):
        self.questions = []  # List of questions
        self.options = []    # List of options for each question
        self.answers = []    # List of correct answers

    def add_question(self, question, options, answer):
        """
        Adds a question, its options, and the correct answer to the quiz.
        """
        self.questions.append(question)
        self.options.append(options)
        self.answers.append(answer)

    def conduct_quiz(self):
        """
        Conducts the quiz, asks questions, and calculates the score.
        """
        score = 0
        
        print("\nStarting the quiz! Select the correct option for the following questions:\n")
        
        for i, question in enumerate(self.questions):
            print(f"Q{i + 1}: {question}")
            for j, option in enumerate(self.options[i]):
                print(f"  {j + 1}. {option}")
            
            user_answer = input("Your answer (enter the option number): ")
            
            # Check if the input is a valid option
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(self.options[i]):
                selected_option = self.options[i][int(user_answer) - 1]
                if selected_option == self.answers[i]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect! The correct answer is: {self.answers[i]}")
            else:
                print("Invalid option selected.")
        
        print(f"\nYour total score is: {score}/{len(self.questions)}")

def main():
    quiz = Quiz()

    while True:
        print("\nQuiz Management")
        print("1. Add a question")
        print("2. Conduct the quiz")
        print("3. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            question = input("Enter the quiz question: ")
            options = []
            for i in range(4):  # Assuming 4 options per question
                option = input(f"Enter option {i + 1}: ")
                options.append(option)
            answer = input("Enter the correct answer: ")
            quiz.add_question(question, options, answer)
            print("Question added!")

        elif choice == "2":
            if not quiz.questions:
                print("No questions available. Please add questions first.")
            else:
                quiz.conduct_quiz()

        elif choice == "3":
            print("Exiting the quiz management system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
