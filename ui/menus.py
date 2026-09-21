from dialogues import dialogue
from ui.screens import history


def main_menu():
    history.set_entitie(dialogue.main_menu_welcome)

    return history.render_screen(
        3,
        "Nova Jornada",
        "Continuar Jornada - Em desenvolvimento",
        "Opções - Em desenvolvimento",
        img_path="images\\menus\\main_menu.png",
        write_effect=False,
    )


def new_game_menu():
    history.set_entitie(dialogue.new_game)

    name_player = history.render_screen(
        1,
        img_path="images\\menus\\new_game_menu.png",
        write_effect=False,
        input_mode="manual",
    )
    return name_player


if __name__ == "__main__":
    pass
