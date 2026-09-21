from pathlib import Path
from random import randint
from time import sleep

from readchar import key, readkey

import entities
import entities.monsters
import entities.player
from core import utils
from core.music import EFFECT, MUSIC, audio
from core.utils import WIDTH_TERMINAL, clear_lines, colour, line
from dialogues import dialogue
from dialogues.dialogue import Dialogue
from skills import skill


class HistoryScreen:
    def __init__(self):
        self.last_dialogue = []
        self.quant_lines = 1
        self.entitie = dialogue.player

    def set_entitie(self, entitie: Dialogue):
        self.entitie = entitie

    def scene_screen(self, img_path):
        line()
        utils.image_to_pixels(Path(img_path).as_posix())

    def scene_update(self, img_path, up_line=10):
        utils.cursor_down(999)
        utils.cursor_up(9 + up_line)
        utils.clear_lines(200)
        utils.clear_lines(200)
        self.scene_screen(Path(img_path).as_posix())
        utils.cursor_down(999)

    def dialogue_screen(
        self,
        quant_lines,
        dialogue=None,
        write_effect=True,
    ):
        if not dialogue:
            lines = self.entitie.dialogue[
                self.entitie.start : self.entitie.start + quant_lines
            ]
            self.entitie.start += quant_lines
        else:
            lines = dialogue
        lines_empty = 3 - quant_lines
        utils.line()
        if self.entitie.name != " ":
            utils.console.print(
                f"    {self.entitie.name}:", justify="center", style=colour["yellow"]
            )
        else:
            print(" ")
        for line in lines:  # noqa: F402
            if write_effect:
                utils.write(f"    {line}\n".rstrip().center(WIDTH_TERMINAL))
                sleep(0.5)
            else:
                utils.console.print(f"    {line}\n", justify="center")
        print("\n" * lines_empty)

    def dialogue_update(
        self,
        quant_lines,
        *options,
        dialogue=None,
        write_effect=True,
    ):

        utils.cursor_down(999)
        utils.clear_lines(8)
        self.dialogue_screen(
            quant_lines=quant_lines,
            dialogue=dialogue,
            write_effect=write_effect,
        )

        self.options_screen(*options)

    def options_screen(
        self,
        *options,
    ):
        index = 0

        line()

        if len(options) == 0:
            print(" ")
            line()
        else:
            while True:
                line_options = ""
                for i, option in enumerate(options):
                    if i == index:
                        line_options += f">  {option}                   "
                    else:
                        line_options += f"   {option}                   "

                utils.console.print(
                    line_options.rstrip(), justify="center", style=colour["yellow"]
                )
                line()
                k = readkey()
                if k == key.LEFT:
                    index -= 1
                elif k == key.RIGHT:
                    index += 1
                elif k == key.ENTER:
                    return options[index].lower()

                audio.play_sfx(EFFECT["navegation"])
                index %= len(options)

                utils.clear_lines(2)

    def options_update(self, *options, input_manual=False):

        utils.clear_lines(3)
        if input_manual:
            return utils.center_input()
        return self.options_screen(*options)

    def render_screen(
        self,
        quant_lines,
        *options,
        img_path=None,
        dialogue=None,
        write_effect=True,
        input_mode="immersive",
    ):
        if img_path:
            utils.clear()
            self.scene_screen(img_path)
        else:
            utils.clear_lines(8)
        self.dialogue_screen(
            quant_lines=quant_lines,
            dialogue=dialogue,
            write_effect=write_effect,
        )
        if input_mode == "manual":
            clear_lines(1)
            utils.console.print(
                "DIGITE ABAIXO", justify="center", style=colour["purple"]
            )
            print(" ")
            return utils.center_input()
        elif input_mode == "immersive":
            return self.options_screen(*options)


history = HistoryScreen()


class CombatScreen(HistoryScreen):
    def __init__(self) -> None:
        self.player_actual_health = entities.player.player.health

    def set_enemy(self, enemy: entities.monsters.Monster):
        self.enemy = enemy
        self.enemy_actual_health = enemy.health

    def set_biome(self, biome):
        self.biome = biome

    def action_screen(self, options=["Atacar", "Defender", "Itens", "Status"]):
        self.scene_screen(f"images\\combat\\{self.biome}\\{self.enemy.id}.png")
        line()
        names_space_empty = " " * (
            WIDTH_TERMINAL - len(self.enemy.name) - len(dialogue.player.name) - 100
        )
        player_health_info = (
            f"Vida: {self.player_actual_health} / {entities.player.player.health}"
        )
        enemy_health_info = f"Vida: {self.enemy_actual_health} / {self.enemy.health}"

        utils.console.print(
            f"      {dialogue.player.name}{names_space_empty}{self.enemy.name}",
            style=colour["yellow"],
            justify="center",
        )
        print(" ")
        utils.console.print(
            f"      {player_health_info}{' ' * (WIDTH_TERMINAL - len(player_health_info) - len(enemy_health_info) - 100)}{enemy_health_info}",
            justify="center",
        )
        print(" ")

        return self.options_screen(*options)

    def attack_screen(self):
        clear_lines(9)
        attacks_line = ""

        line()
        print(" ")
        utils.console.print("ATAQUES", style=colour["yellow"], justify="center")
        for attack in entities.player.player.attacks:
            attacks_line += f"{attack.name}: {entities.player.player.damage * attack.multiplier}        "
        utils.console.print(f"{attacks_line}".rstrip(), justify="center")
        utils.skip_line(2)
        line()
        print(" ")
        while True:
            utils.console.print(
                "DIGITE O ATAQUE", justify="center", style=colour["purple"]
            )
            print(" ")
            choice = utils.center_input().capitalize()
            if choice in attacks_line:
                for skl in skill.skills:
                    if choice == skl.name:
                        damage = (
                            entities.player.player.damage * skl.multiplier
                            - self.enemy.defense
                        )
                        if damage <= 0:
                            damage = 1
                        audio.play_sfx(skl.sound)
                self.enemy_actual_health -= damage

                clear_lines()
                utils.console.print(
                    f"---- {self.enemy.name} tomou {damage} de dano! ----",
                    justify="center",
                    style=colour["green"],
                )
                utils.cursor_up(20)
                self.scene_update("images\\combat\\duskwood_village\\rat_damage.png")
                sleep(2)
                break
            clear_lines(2)
            utils.console.print(
                "---- Você não possui esse ataque ----",
                style=colour["red"],
                justify="center",
            )
            sleep(1.2)
            clear_lines(2)

    def enemy_attack(self):
        indice = randint(0, len(self.enemy.attacks) - 1)
        attack = self.enemy.attacks[indice]
        damage = self.enemy.damage * attack.multiplier - entities.player.player.defense

        self.player_actual_health -= damage

        utils.clear()
        self.scene_screen(f"images\\combat\\{self.biome}\\{self.enemy.id}.png")
        line()
        print(" ")
        utils.console.print(
            f"{self.enemy.name} usou {attack.name}!",
            justify="center",
            style=colour["red"],
        )
        audio.play_sfx(attack.sound)
        print(" ")
        line()

        sleep(2)
        clear_lines(2)

        utils.console.print(
            f"{dialogue.player.name} tomou {damage} de dano!!",
            justify="center",
            style=colour["red"],
        )
        print(" ")
        line()
        sleep(2)

    def result_screen(self, result):
        utils.clear()
        if result == "win":
            self.scene_screen(
                f"images\\combat\\{self.biome}\\{self.enemy.id}_death.png"
            )
            line()
            print(" ")
            utils.console.print(
                f"JOGADOR {entities.player.player.nickname} VENCEU!!",
                justify="center",
                style=colour["green"],
            )
            print(" ")
            line()
            audio.pause_music()
            audio.play_sfx(EFFECT["combat_win"])
            sleep(4)

        elif result == "defeat":
            self.scene_screen(f"images\\combat\\{self.biome}\\{self.enemy.id}.png")
            line()
            print(" ")
            utils.console.print(
                f"JOGADOR {entities.player.player.nickname} MORREU!!",
                justify="center",
                style=colour["red"],
            )
            print(" ")
            line()
            audio.pause_music()
            audio.play_sfx(EFFECT["combat_defeat"])
            sleep(3)

    def start(self):
        utils.clear()
        audio.play_music(MUSIC["combat"])

        while True:
            choice = self.action_screen()

            match choice:
                case "atacar":
                    self.attack_screen()
                    if self.enemy_actual_health <= 0:
                        self.result_screen("win")
                        break
                case "defender":
                    pass

                case "status":
                    pass

                case "itens":
                    pass

            self.enemy_attack()
            if self.player_actual_health <= 0:
                self.result_screen("defeat")
                break


combat = CombatScreen()


def size_terminal_calibration():
    utils.hide_cursor()
    utils.clear()
    utils.line()
    utils.image_to_pixels("images\\logo_icon.png", WIDTH_TERMINAL, 90)
    utils.line()
    print(
        utils.center(
            "AJUSTE O TAMANHO DA TELA ATÉ QUE AS LINHAS ROXAS E A IMAGEM CALIBREM PERFEITAMENTE"
        )
    )
    print(utils.center("Pressione ENTER para prosseguir...", color="purple"))
    utils.line()
    input("")
    utils.clear()
    return ""


def intro():
    utils.hide_cursor()
    audio.play_music(MUSIC["intro"])
    utils.logo_fade("images\\intro\\mushroom_head_productions.png")
    sleep(0.5)
    print(" ")
    print(" ")
    utils.logo_fade("images\\intro\\logo.png")
    sleep(0.5)
