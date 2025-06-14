"""
1) Start by displaying a welcome message and game instructions using a display_title() function.

2) Include a main() function that controls the game flow.

3) Ask the player to enter their name or a code name and validate the input using a regular expression; using the re module.

4) Present the user with choices using if/elif/else statements.

5) Use at least two additional functions, aside from main() and display_title(), to control sections of the story.

6) Store the player's decisions in a list.

7) Use a loop to allow the player to replay the game.

8) Include at least one while or for loop and one dictionary to map outcomes.

9) Save the player's game data (e.g., name, decisions, outcome) to a file in JSON format using the json module
"""

welcome_message = "Welcome to the Adventure Game!"

def display_title():
    print(welcome_message)

def main():
    display_title()
    

if __name__ == "__main__":
    main()