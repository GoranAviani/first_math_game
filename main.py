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


def main():
    display_intro()
    display_menu()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
