import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['question'])
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        user_answer = input("Your answer (enter the option number): ")
        return int(user_answer)

    def run_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            user_answer = self.display_question(question)
            if user_answer == question['correct_answer']:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question['correct_answer']}: {question['options'][question['correct_answer'] - 1]}\n")

        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    # Sample questions
    questions = [
        {
            'question': 'What is the capital of France?',
            'options': ['Berlin', 'Paris', 'Madrid', 'Rome'],
            'correct_answer': 2
        },
        {
            'question': 'Which programming language is this quiz written in?',
            'options': ['Java', 'Python', 'C++', 'JavaScript'],
            'correct_answer': 2
        },
        {
            'question': 'What is the largest mammal?',
            'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
            'correct_answer': 2
        }
        # Add more questions as needed
    ]

    quiz = Quiz(questions)
    quiz.run_quiz()
