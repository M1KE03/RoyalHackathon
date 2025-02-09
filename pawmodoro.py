import time
import sys  # Import sys to overwrite lines in the terminal


def user_input(answer):
    while True:
        try:
            duration = int(input(answer))  # Get user input as an integer
            if duration <= 0:
                print("Unless you can time travel, that's not a valid duration :D Try again please: ")
            else:
                return duration  # Return the valid duration to store in a variable
        except ValueError:
            print("Error! :( Please enter a number!")  # If input isn't a number


def pomodoroStudy(studyTime, breakTime, amount):
    """Runs the study session countdown, then starts break session."""
    for i in range(amount):
        print(f" Study session {i+1} of {amount} starting now!")
        seconds = studyTime * 60  # Convert minutes to seconds
        while seconds:
            mins, sec = divmod(seconds, 60)  # Convert total seconds into MM:SS format
            timer = f"{mins:02d}:{sec:02d}"
            sys.stdout.write("\r" + timer)  # Overwrite the line instead of printing new ones
            sys.stdout.flush()
            time.sleep(1)  # Pause for a second
            seconds -= 1

        print("\nStudy session over! Break time :D")  # Move to new line
        if i < amount - 1:  # Only take a break if it's not the last session
            pomodoroBreak(breakTime)
        else:
            print("All study sessions completed! Great job! :D")


def pomodoroBreak(breakTime) :
    """Runs the break countdown, then restarts the study session."""
    seconds = breakTime * 60
    while seconds:
        mins, sec = divmod(seconds, 60)
        timer = f"{mins:02d}:{sec:02d}"
        sys.stdout.write("\r" + timer)
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1

    print("Break time over! Back to study time :D")
    pomodoroStudy(study_duration, break_duration)  # Restart study session


if __name__ == '__main__':
    study_duration = user_input("Please enter how long you would like to study for in minutes: ")
    amount = int(input("How many study sessions would you like to complete? "))
    break_duration = user_input("Please enter how long you would like to take a break for in minutes: ")
    pomodoroStudy(study_duration, break_duration, amount)  # Start the cycle