import json

def load_questions(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def run_quiz(questions):
    score = 0
    for i, question in enumerate(questions):
        print(f"Q{i + 1}. {question['question']}")
        for idx, option in enumerate(question['options']):
            print(f"{idx}. {option}")

        try:
            user_answer = int(input("Your answer (number): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue  
        if user_answer == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer: {question['answer']}\n")

    print(f" Your final score: {score}/{len(questions)}")

if __name__ == "__main__":
    questions = load_questions('questions.json')
    run_quiz(questions)
