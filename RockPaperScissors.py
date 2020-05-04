
from random import randint


rock_default = "Rock"
paper_default = "Paper"
scissors_default = "Scissors"

RPS = {
    "rock": rock_default,
    "paper": paper_default,
    "scissors": scissors_default
}


# Set RPS names
def set_rps(r=rock_default, p=paper_default, s=scissors_default):
    RPS["rock"] = r
    RPS["paper"] = p
    RPS["scissors"] = s


# Getters - return lower-case versions of the choices for comparison

def rock():
    return RPS["rock"].lower()


def paper():
    return RPS["paper"].lower()


def scissors():
    return RPS["scissors"].lower()


def get_ai_choice():
    valinta = randint(1, 3)
    if valinta == 1:
        return RPS["rock"]
    elif valinta == 2:
        return RPS["paper"]
    else:
        return RPS["scissors"]


def main():

    # Commands
    select_play = "P"
    select_custom = "C"
    select_defaults = "R"
    quit_game = "Q"
    invalid_command = "Invalid command."

    # Main loop
    while True:

        print("\n*** Welcome to ", end="")
        print(RPS["rock"], RPS["paper"], RPS["scissors"] + "! ***\n", sep="-")

        user_input = input("""(P)lay
(C)ustom Game
(R)estore Defaults
(Q)uit program
: """).lower()

        # Quit
        if user_input == quit_game.lower():
            break

        # Play game
        elif user_input == select_play.lower():

            rounds = 0
            wins = 0
            losses = 0
            ties = 0

            win_msg = "You win!"
            lose_msg = "You lose!"
            tie_msg = "It's a tie!"

            print("*** Starting new game ***")

            # Game loop
            while True:

                print("\nRound", rounds + 1)
                # Prompt uses the case sensitive versions
                prompt = RPS["rock"] + ", " + RPS["paper"] + ", or " + RPS["scissors"] + "? (\"" + \
                    quit_game + "\" to quit game)\nYou: "

                # Get user and AI selection
                user_selection = input(prompt).lower()  # case shouldn't matter
                ai_selection = get_ai_choice()

                # Quit
                if user_selection == quit_game.lower():
                    break

                # Valid selection
                if user_selection == rock() or user_selection == paper() or user_selection == scissors():

                    print("AI:", ai_selection)
                    ai_selection = ai_selection.lower()     # case shouldn't matter

                    if user_selection == rock():
                        if user_selection == ai_selection:
                            print(tie_msg)
                            ties += 1
                        elif ai_selection == paper():
                            print(lose_msg)
                            losses += 1
                        elif ai_selection == scissors():
                            print(win_msg)
                            wins += 1
                    elif user_selection == paper():
                        if user_selection == ai_selection:
                            print(tie_msg)
                            ties += 1
                        elif ai_selection == scissors():
                            print(lose_msg)
                            losses += 1
                        elif ai_selection == rock():
                            print(win_msg)
                            wins += 1
                    elif user_selection == scissors():
                        if user_selection == ai_selection:
                            print(tie_msg)
                            ties += 1
                        elif ai_selection == paper():
                            print(win_msg)
                            wins += 1
                        elif ai_selection == rock():
                            print(lose_msg)
                            losses += 1
                    rounds += 1
                # Invalid selection
                else:
                    print(invalid_command)

            # Print final stats
            print("\n***STATS***")
            print("Rounds played:", rounds)
            if rounds != 0:
                print("Won:", wins, "(" + str(round(wins / rounds * 100, 2)) + "%)")
                print("Lost:", losses, "(" + str(round(losses / rounds * 100, 2)) + "%)")
                print("Tied:", ties, "(" + str(round(ties / rounds * 100, 2)) + "%)")
            input("\n[Press enter to continue]")

        # Custom game
        elif user_input == select_custom.lower():

            # Get new rock
            user_rock = input("New " + rock_default + ": ")

            # Get new paper
            user_paper = input("What beats " + user_rock + "? ")

            # Make sure rock and paper aren't the same
            while user_paper.lower() == user_rock.lower():
                print(user_paper, "cannot beat itself!")
                user_paper = input("What beats " + user_rock + "? ")

            # Get new scissors and make sure it's not the same as rock or paper
            user_scissors = input("What beats " + user_paper + " and loses to " + user_rock + "? ")
            while user_scissors.lower() in [user_rock.lower(), user_paper.lower()]:
                if user_scissors.lower() == user_rock.lower():
                    print(user_scissors, "cannot lose to itself!")
                else:
                    print(user_scissors, "cannot beat itself!")
                user_scissors = input("What beats " + user_paper + " and loses to " + user_rock + "? ")

            while True:
                # Are you sure?
                user_input = input("Set new mode as \"" + user_rock + ", " +
                                   user_paper + ", " + user_scissors + "\"? (Y/N): ").lower()

                # If yes, set new values
                if user_input == "y":
                    set_rps(user_rock, user_paper, user_scissors)
                    break
                elif user_input == "n":
                    break
                else:
                    print(invalid_command)

        # Restore defaults
        elif user_input == select_defaults.lower():

            if RPS["rock"] == rock_default and RPS["paper"] == paper_default and RPS["scissors"] == scissors_default:
                print("Already using defaults.")

            else:
                while True:
                    user_input = input("Really restore defaults? (Y/N): ").lower()
                    if user_input == "y":
                        set_rps()
                        break
                    elif user_input == "n":
                        break
                    else:
                        print(invalid_command)

        # Invalid command
        else:
            print(invalid_command)


if __name__ == '__main__':
    main()

