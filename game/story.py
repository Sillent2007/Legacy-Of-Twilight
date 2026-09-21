from pathlib import Path
from time import sleep

from core import utils
from core.music import EFFECT, MUSIC, audio
from dialogues import dialogue
from entities import monsters
from ui.screens import combat, history


def prologue():
    history.set_entitie(dialogue.prologue)
    utils.clear()
    audio.stop_music()
    sleep(2)
    audio.play_music(Path(MUSIC["prologue"]).as_posix())
    history.render_screen(3, "Continuar", img_path="images\\prologue\\zerkan_map.png")
    history.render_screen(3, "Continuar", img_path="images\\prologue\\dead_crops.png")
    history.render_screen(2, "Continuar", img_path="images\\prologue\\dead_cattle.png")
    history.render_screen(3, "Continuar", img_path="images\\prologue\\dead_man.png")
    history.dialogue_update(quant_lines=1)
    history.options_update("Continuar")
    history.render_screen(3, "Continuar", img_path="images\\prologue\\meteor1.png")
    history.scene_update("images\\prologue\\meteor2.png")
    sleep(2)
    history.scene_update("images\\prologue\\meteor3.png")
    sleep(2)
    history.scene_update("images\\black_screen.png")
    sleep(1)
    audio.play_sfx(EFFECT["explosion"])
    sleep(3)
    history.render_screen(1, "Continuar", img_path="images\\black_screen.png")
    history.render_screen(2, "Continuar", img_path="images\\prologue\\chicken.png")
    audio.stop_music()
    audio.play_sfx(EFFECT["chicken"])
    sleep(2)
    # ------- INICIO DO JOGO -------


def chapter_1():
    history.set_entitie(dialogue.player)  # ------ PLAYER HOME ------
    audio.play_music(MUSIC["village"])
    choice = history.render_screen(
        3,
        "Trocar de roupa",
        "Ir tomar café",
        "Voltar a dormir",
        img_path="images\\backgrounds\\bedroom_player.png",
    )
    while True:  # ------ WAKING UP ------
        match choice:
            case "trocar de roupa":
                history.scene_update("images\\backgrounds\\closet.png")
                audio.play_sfx(EFFECT["changing_clothes"])
                sleep(3.5)
                history.render_screen(1, "Ir tomar café", dialogue=["Agora sim!"])
                break

            case "ir tomar café":
                choice = history.render_screen(
                    1,
                    "Trocar de roupa",
                    "Voltar a dormir",
                    dialogue=["Eu deveria tirar esse pijama primeiro"],
                )

            case "voltar a dormir":
                choice = history.render_screen(
                    1,
                    "Trocar de roupa",
                    "Ir tomar café",
                    dialogue=["Acho que já dormi demais"],
                )
    history.render_screen(  # ------ KITCHEN ------
        3, "Continuar", img_path="images\\backgrounds\\home_kitchen.png"
    )
    history.set_entitie(dialogue.mother)
    history.render_screen(3, "Continuar")
    choice = history.render_screen(2, "Sentar e comer", "Rejeitar")
    while True:
        match choice:
            case "sentar e comer":
                break
            case "rejeitar":
                choice = history.render_screen(
                    1, "Sentar e comer", dialogue=["Fiz o bolo que você adora!"]
                )

    history.render_screen(
        1, "Comer bolo", img_path="images\\backgrounds\\home_kitchen2.png"
    )
    # AUDIO
    history.options_update("Tomar suco")
    # AUDIO
    history.render_screen(3, "Ir para o porão")

    history.set_entitie(dialogue.player)  # ---- HOME BASEMENT ----
    history.render_screen(
        3, "Continuar", img_path="images\\backgrounds\\home_basement.png"
    )
    audio.play_sfx(EFFECT["rat_squeaking"])
    history.render_screen(
        2, "Iniciar Batalha", img_path="images\\backgrounds\\home_basement2.png"
    )

    combat.set_biome("duskwood_village")
    combat.set_enemy(monsters.rat)
    combat.start()

    audio.play_music(audio.play_music(MUSIC["village"]))
    history.render_screen(
        2, "Sair de casa", img_path="images\\backgrounds\\home_basement.png"
    )
    history.render_screen(
        2, "Continuar", img_path="images\\backgrounds\\duskwood_village.png"
    )
    history.set_entitie(dialogue.dilan)
    history.render_screen(
        2, "Continuar", img_path="images\\backgrounds\\duskwood_village2.png"
    )
    history.render_screen(
        2, "Continuar", img_path="images\\backgrounds\\duskwood_village3.png"
    )
    choice = history.render_screen(
        2,
        "Contar sobre os sonhos",
        "Não estou afim de falar",
        img_path="images\\backgrounds\\duskwood_village5.png",
    )

    match choice:
        case "contar sobre os sonhos":
            history.render_screen(
                3,
                "Ir para a Taverna",
                dialogue=[
                    "Isso explica sua cara de zumbi",
                    "vem, vamos a um lugar mais tranquilo para conversarmos",
                ],
            )

        case "não estou afim de falar":
            history.render_screen(
                2,
                "Ir para a Taverna",
                dialogue=[
                    "Alguém aqui está de mau humor",
                    "vem, vamos a um lugar mais tranquilo para conversarmos",
                ],
            )

    history.render_screen(3, "Falar", img_path="images\\backgrounds\\duskwood_tavern.png")

    history.set_entitie(dialogue.player)
    for _ in range(2):
        history.dialogue_update(3, "Continuar")