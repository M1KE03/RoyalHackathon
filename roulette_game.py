import random
import os

def load_chips(filename="chips_data.txt"):
    """Load chips from the quiz results file."""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return int(file.read().strip())
    return 0  # If file doesn't exist, assume 0 chips

def save_chips(chips, filename="chips_data.txt"):
    """Save updated chips after playing roulette."""
    with open(filename, "w") as file:
        file.write(str(chips))

def play_roulette(chips):
    """Roulette game where user can gamble chips to win study breaks."""
    print("\n🎰 Welcome to the Study Break Roulette! 🎰")
    print(f"You currently have £{chips} in chips.")

    while chips > 0:
        print("\nHow much would you like to bet?")
        bet = input(f"Enter a number (1 - {chips}, or 'q' to quit): ")

        if bet.lower() == 'q':
            break  # Exit the roulette game
        if not bet.isdigit() or not (1 <= int(bet) <= chips):
            print("❌ Invalid bet. Please enter a valid amount.")
            continue

        bet = int(bet)
        print("🔄 Spinning the roulette wheel...")
        spin_result = random.randint(0, 36)  # Simulate roulette numbers

        # Determine win/loss (basic rules)
        if spin_result % 2 == 0:  # Even numbers win
            chips += bet
            print(f"✅ You won! The wheel landed on {spin_result}. Your new balance is £{chips}.")
        else:  # Odd numbers lose
            chips -= bet
            print(f"❌ You lost! The wheel landed on {spin_result}. Your new balance is £{chips}.")

        if chips <= 0:
            print("💸 You're out of chips! Better luck next time.")
            break  # Exit when user runs out of chips

    print("\n🎉 Roulette session over. Saving your chip balance...")
    save_chips(chips)
    return chips  # Return updated chip count


def main():
    chips = load_chips()  # Load chips from quiz
    if chips == 0:
        print("🚫 You have no chips to play! Earn chips by completing the quiz.")
        return

    play_roulette(chips)

    print("\nRun `quiz_game.py` to earn more chips!")

if __name__ == "__main__":
    main()
