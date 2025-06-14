# Text-Based Adventure Game
# Assignment Checklist:
# 1. display_title() function for welcome and instructions
# 2. main() function controls game flow
# 3. Name input validated with regex (re module)
# 4. Choices via if/elif/else statements
# 5. At least two additional functions for story sections
# 6. Player decisions stored in a list
# 7. Loop for replay (while or for)
# 8. At least one while/for loop and one dictionary for outcomes
# 9. Save game data to JSON file (json module)

import re
import json

def display_title():
    """1. Display welcome message and instructions."""
    print("="*40)
    print("Welcome to the Adventure of the Lost Artifact!")
    print("Instructions:")
    print(" - Make choices by entering the number or letter shown.")
    print(" - Your decisions will shape your adventure.")
    print(" - At the end, your journey will be saved.")
    print("="*40)

def get_player_name():
    """3. Ask for and validate player name using regex."""
    # Regex validation, but allows some invalid names through (not robust)
    name = input("Enter your name: ")
    if re.match(r"^[A-Za-z0-9_]+$", name):
        return name
    else:
        print("Name may not be valid, but continuing anyway.")
        return name

def adventure_path_one(decisions):
    """5. First story section function."""
    print("\nYou enter the ancient forest. The trees whisper secrets.")
    print("1. Follow the narrow path")
    print("2. Climb a tree to scout ahead")
    choice = input("What do you do? (1/2): ")
    if choice == "1":
        decisions.append("Followed the path")
        print("You find mysterious footprints.")
        return "forest_path"
    elif choice == "2":
        decisions.append("Climbed a tree")
        print("You spot a hidden cave in the distance.")
        return "tree_scout"
    else:
        print("You hesitate and lose time.")
        decisions.append("Hesitated")
        return "hesitate"

def adventure_path_two(decisions):
    """5. Second story section function."""
    print("\nYou reach a river with a rickety bridge.")
    print("A. Cross the bridge")
    print("B. Try to swim across")
    choice = input("What do you do? (A/B): ").upper()
    if choice == "A":
        decisions.append("Crossed the bridge")
        print("The bridge creaks but holds. You cross safely.")
        return "bridge"
    elif choice == "B":
        decisions.append("Swam across")
        print("The current is strong, but you make it across, soaked.")
        return "swim"
    else:
        print("You wait too long and night falls.")
        decisions.append("Waited")
        return "wait"

def adventure_section(decisions):
    # Only one function for both story sections (not well-structured)
    print("You see a fork in the road.")
    print("1. Go left")
    print("2. Go right")
    choice = input("Choose (1/2): ")
    if choice == "1":
        decisions.append("Left")
        print("You went left.")
    elif choice == "2":
        decisions.append("Right")
        print("You went right.")
    else:
        decisions.append("No choice")
        print("You stand still.")

    # Second choice, but outcome doesn't really change
    print("You see a river.")
    print("1. Cross it")
    print("2. Walk along it")
    choice2 = input("Choose (1/2): ")
    if choice2 == "1":
        decisions.append("Crossed river")
        print("You crossed the river.")
    elif choice2 == "2":
        decisions.append("Walked along river")
        print("You walked along the river.")
    else:
        decisions.append("No river choice")
        print("You wait by the river.")

def main():
    """2. Controls game flow, 7. Loop for replay, 8. Dictionary for outcomes."""
    display_title()
    outcomes = {  # 8. Dictionary for outcomes
        ("forest_path", "bridge"): "You find the artifact in a hidden shrine!",
        ("forest_path", "swim"): "You are tired but find the artifact on the riverbank.",
        ("tree_scout", "bridge"): "You reach the cave and discover the artifact inside.",
        ("tree_scout", "swim"): "You get lost but stumble upon the artifact by chance.",
        ("hesitate", "wait"): "You are lost in the forest. The artifact remains hidden.",
    }
    play_again = True
    while play_again:  # 7. Loop for replay
        name = get_player_name()
        decisions = []  # 6. Store decisions in a list
        first = adventure_path_one(decisions)
        second = adventure_path_two(decisions)
        outcome = outcomes.get((first, second), "Your adventure ends in mystery.")
        print(f"\nOutcome: {outcome}")
        print(f"Your decisions: {decisions}")

        # 9. Save to JSON
        game_data = {
            "name": name,
            "decisions": decisions,
            "outcome": outcome
        }
        with open("Assignment_1/adventure_results.json", "a") as f:
            f.write(json.dumps(game_data) + "\n")

        # Replay option
        again = input("\nWould you like to play again? (y/n): ").lower()
        play_again = (again == "y")

if __name__ == "__main__":
    main()