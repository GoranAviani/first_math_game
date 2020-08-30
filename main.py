# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def display_intro():
    game_title = "First math game"
    print("*" * len(game_title))
    print(game_title)
    print("*" * len(game_title))

def display_menu():
    menu_list = ["Press N for [N]ew game", "Press X for E[x]it"]
    for menu_option in menu_list:
        print(menu_option)

def display_separator():
    print("*" * 30)

def get_user_input():
    user_input = input("What is your selection?: ")
    return user_input.lower()

def play_game():
    print("This is a game")

def main():
    display_intro()
    display_menu()
    user_input = get_user_input()
    if user_input == "n":
        display_separator()
        play_game()
    else:
        exit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
