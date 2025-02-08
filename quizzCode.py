import random


def fisher_yates_shuffle(array):
    """Shuffle 'array' in place using the Fisher-Yates algorithm."""
    for i in range(len(array) - 1, 0, -1):
        j = random.randint(0, i)
        array[i], array[j] = array[j], array[i]  # swap


def falseans_generator(correct_answer, potential_answers, num=3):
    """Generate 'num' incorrect answers excluding the correct answer."""
    filtered_options = [opt for opt in potential_answers if opt.lower() != correct_answer.lower()]
    return random.sample(filtered_options, num)


def create_mc_question(question_data, potential_answers):
    """Create multiple-choice quiz question with shuffled answers."""
    question_text = question_data["question"]
    correct_answer = question_data["correct_answer"]

    false_answers = falseans_generator(correct_answer, potential_answers, num=3)
    all_answers = [correct_answer] + false_answers
    fisher_yates_shuffle(all_answers)

    return {
        "question": question_text,
        "correct_answer": correct_answer,
        "options": all_answers,
    }


def save_chips(chips, filename="chips_data.txt"):
    """Save earned chips to a file for use in the roulette game."""
    with open(filename, "w") as file:
        file.write(str(chips))


def main():
    # Possible answers for distractors
    all_possible_answers = ["Berlin", "Madrid", "Tokyo", "London", "Sydney"]

    # Quiz questions
    questions_data = [
        {"question": "What is the capital of France?", "correct_answer": "Paris"},
        {"question": "Who developed the theory of relativity?", "correct_answer": "Albert Einstein"}
    ]

    mc_quiz = [create_mc_question(q_data, all_possible_answers) for q_data in questions_data]

    user_answers = []
    correct_count = 0
    wrong_count = 0
    total_chips = 0  # Starts with 0 chips

    for i, q in enumerate(mc_quiz, start=1):
        print(f"{i}. {q['question']}")
        for idx, option in enumerate(q['options'], start=1):
            print(f"   {idx}. {option}")

        user_choice = input("Enter your choice: ")
        while not user_choice.isdigit() or not (1 <= int(user_choice) <= len(q['options'])):
            user_choice = input(f"Invalid input. Please enter a number between 1 and {len(q['options'])}: ")
        user_choice = int(user_choice)

        chosen_answer = q['options'][user_choice - 1]
        user_answers.append(chosen_answer)

        if chosen_answer.lower() == q["correct_answer"].lower():
            correct_count += 1
            total_chips += 5  # Earns £5 chips per correct answer
            print(f"✅ Correct! You now have £{total_chips} in chips.\n")
        else:
            wrong_count += 1
            print(f"❌ Wrong! The correct answer was: {q['correct_answer']}\n")

    print("📊 Quiz Complete!")
    print(f"You got {correct_count} correct and {wrong_count} wrong.")
    print(f"💰 You earned £{total_chips} in chips.")

    # Save the earned chips for the roulette game
    save_chips(total_chips)

    # Ask if the user wants to play the roulette game
    print("\nWould you like to play the roulette game to win study break time?")
    print("Run `roulette_game.py` to use your chips!")


if __name__ == "__main__":
    main()
