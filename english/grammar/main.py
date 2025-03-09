import random
from questions import quiz_questions

def run_quiz():
    score = 0
    selected_questions = random.sample(quiz_questions, 20)
    random.shuffle(selected_questions)

    print("\n🎓 Welcome to the English Grammar Quiz! 🎓")
    input("Select the correct answer (A, B, or C).\n")

    for i, (question, options, correct_answer) in enumerate(selected_questions, 1):
        print(f"{i}. {question}")
        print(f"A) {options[0]}")
        print(f"B) {options[1]}")
        print(f"C) {options[2]}")

        user_answer = input("Your answer (A, B, or C): ").strip().upper()

        if user_answer == 'q' :
            return

        if user_answer == correct_answer:
            print("✅ Correct!\n")
            score += 1
        else:
            input(f"❌ Incorrect. The correct answer is {correct_answer}) {options[ord(correct_answer) - 65]}.\n")

    print(f"🎯 Final Score: {score}/20")
    if score > 17:
        print("🎉 Amazing! You have excellent grammar skills!")
    elif score > 13:
        print("👍 Well done! Keep practicing.")
    elif score > 9:
        print("📚 Not bad, but you can improve!")
    else:
        print("📖 Keep studying! Practice makes perfect.")

if __name__ == "__main__":
    run_quiz()

