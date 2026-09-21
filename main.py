from core import utils
from dialogues import dialogue
from entities.player import player
from game import story
from ui import menus, screens


def main():
    # ------ INTRODUCTION -------
    screens.size_terminal_calibration()
    # screens.intro()

    # ------ MAIN MENU -------
    utils.hide_cursor()
    choice = menus.main_menu()
    if choice == "nova jornada":
        name_player = menus.new_game_menu()
        player.get_info(
            nickname=name_player, health=10, damage=5, defense=2, xp=0, level=1
        )
        dialogue.player.set_name(name_player)

        # ------ PROLOGUE ------
        # story.prologue()

    # ------ START GAME ------
    story.chapter_1()


if __name__ == "__main__":
    main()
