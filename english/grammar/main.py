import random

# Liste des 50 questions sous forme (question, options, bonne réponse)
quiz_questions = [
    ("If I _______ you, I wouldn’t take that risk.", ["was", "were", "am"], "B"),
    ("I regret _______ him that secret.", ["tell", "to tell", "telling"], "C"),
    ("She had her house _______ last year.", ["painted", "painting", "to paint"], "A"),
    ("By the time we arrived, the show _______.", ["had already started", "has already started", "already started"], "A"),
    ("I wish I _______ more time to travel.", ["had", "have", "will have"], "A"),
    ("If only he _______ harder, he would have passed.", ["studies", "had studied", "would study"], "B"),
    ("She suggested _______ to the new restaurant downtown.", ["to go", "going", "go"], "B"),
    ("Not only _______ the book, but he also made a documentary.", ["he wrote", "did he write", "wrote he"], "B"),
    ("He denied _______ the money.", ["to steal", "stealing", "steal"], "B"),
    ("They were used to _______ in cold weather.", ["live", "living", "to live"], "B"),
    ("We would rather you _______ later.", ["come", "came", "will come"], "B"),
    ("If she _______ earlier, she wouldn’t have missed the train.", ["left", "had left", "leaves"], "B"),
    ("No sooner _______ the meeting started than he walked out.", ["had", "did", "has"], "A"),
    ("I can't stand _______ in traffic.", ["to wait", "waiting", "wait"], "B"),
    ("He insisted on _______ the bill.", ["pay", "paying", "to pay"], "B"),
    ("He is said _______ a fortune in real estate.", ["to make", "to have made", "making"], "B"),
    ("If I hadn’t been so tired, I _______ the party.", ["would have enjoyed", "enjoyed", "would enjoy"], "A"),
    ("She didn’t let me _______ my opinion.", ["express", "expressing", "to express"], "A"),
    ("It’s high time we _______ a decision.", ["make", "made", "have made"], "B"),
    ("Hardly _______ home when it started to rain.", ["had I arrived", "I had arrived", "have I arrived"], "A"),
    ("He has difficulty _______ in large groups.", ["speaking", "speak", "to speak"], "A"),
    ("He objected to _______ treated unfairly.", ["be", "being", "to be"], "B"),
    ("I needn’t _______ so much food.", ["to buy", "have bought", "buying"], "B"),
    ("I’d rather you _______ about this.", ["not talk", "don’t talk", "not talked"], "C"),
    ("The film was so boring that I _______ asleep.", ["fell", "have fallen", "was falling"], "A"),
    ("You must be tired after _______ all day.", ["work", "working", "to work"], "B"),
    ("I can’t help _______ when I watch that movie.", ["cry", "crying", "to cry"], "B"),
    ("She was accused of _______ confidential information.", ["leaking", "leak", "to leak"], "A"),
    ("You should have _______ me earlier.", ["call", "called", "calling"], "B"),
    ("The book is worth _______.", ["to read", "reading", "read"], "B"),
    ("I'd rather you _______ home now.", ["went", "go", "will go"], "A"),
    ("He was too tired _______ any further.", ["to walk", "walk", "walking"], "A"),
    ("He seems _______ a good time at the party.", ["having", "have had", "to have had"], "C"),
    ("She is believed _______ the crime.", ["to commit", "to have committed", "committing"], "B"),
    ("The manager demanded that he _______ on time.", ["be", "is", "was"], "A"),
    ("We are looking forward to _______ you.", ["seeing", "see", "to see"], "A"),
    ("If I had known, I _______ earlier.", ["will come", "would come", "would have come"], "C"),
    ("You had better _______ now.", ["leaving", "leave", "to leave"], "B"),
    ("The teacher made us _______ the test again.", ["do", "to do", "doing"], "A"),
    ("He had difficulty _______ the heavy box.", ["to carry", "carrying", "carry"], "B"),
    ("She denied _______ anything wrong.", ["to do", "doing", "do"], "B"),
    ("I can’t afford _______ a new car.", ["buying", "to buy", "buy"], "B"),
    ("It's no use _______ to him.", ["talking", "talk", "to talk"], "A"),
    ("You should avoid _______ too much sugar.", ["eat", "eating", "to eat"], "B"),
    ("He is used to _______ early.", ["waking up", "wake up", "wakes up"], "A"),
    ("They had difficulty _______ the car.", ["repairing", "to repair", "repair"], "A"),
    ("He went on _______ about his problems.", ["talking", "talk", "to talk"], "A"),
    ("She is busy _______ emails.", ["writing", "write", "to write"], "A"),
    ("I prefer _______ tea to coffee.", ["drink", "drinking", "to drink"], "B"),
    ("She kept _______ during the lecture.", ["yawning", "yawn", "to yawn"], "A"),
]

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

