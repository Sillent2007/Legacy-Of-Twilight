from pathlib import Path

import pygame

pygame.mixer.init()


class AudioManager:
    def __init__(self):

        self.music_volume = 0.5
        self.sfx_volume = 1.0

    # ----------------------------
    # MÚSICA
    # ----------------------------

    def play_music(self, path, loop=True):

        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(self.music_volume)

        pygame.mixer.music.play(-1 if loop else 0)

    def stop_music(self):

        pygame.mixer.music.stop()

    def pause_music(self):

        pygame.mixer.music.pause()

    def resume_music(self):

        pygame.mixer.music.unpause()

    def fadeout(self, milliseconds=1000):

        pygame.mixer.music.fadeout(milliseconds)

    def set_music_volume(self, volume):

        self.music_volume = volume

        pygame.mixer.music.set_volume(volume)

    # ----------------------------
    # EFEITOS SONOROS
    # ----------------------------

    def play_sfx(self, path):

        sound = pygame.mixer.Sound(path)

        sound.set_volume(self.sfx_volume)

        sound.play()

    def set_sfx_volume(self, volume):

        self.sfx_volume = volume


MUSIC = {
    "intro": Path("assets\\music\\intro.mp3").as_posix(),
    "prologue": Path("assets\\music\\prologue.mp3").as_posix(),
    "village": Path("assets/music/village.mp3").as_posix(),
    "forest": Path("assets/music/forest.mp3").as_posix(),
    "combat": Path("assets/music/combat.mp3").as_posix(),
}

EFFECT = {
    "navegation": Path("assets\\sound_effect\\change_option.mp3").as_posix(),
    "dialogue": Path("assets\\sound_effect\\dialogues.mp3").as_posix(),
    "explosion": Path("assets\\sound_effect\\explosion.mp3").as_posix(),
    "chicken": Path("assets\\sound_effect\\chicken.mp3").as_posix(),
    "rat_squeaking": Path("assets\\sound_effect\\rat_squeaking.mp3").as_posix(),
    "chicken_screaming": Path("assets\\sound_effect\\chicken_screaming.mp3").as_posix(),
    "changing_clothes": Path("assets\\sound_effect\\changing_clothes.mp3").as_posix(),
    "stairs": Path("assets\\sound_effect\\walking_in_stairs.mp3").as_posix(),
    "kick": Path("assets\\sound_effect\\kick.mp3").as_posix(),
    "bite": Path("assets\\sound_effect\\bite.mp3").as_posix(),
    "combat_defeat": Path("assets\\sound_effect\\combat_defeat.mp3").as_posix(),
    "combat_win": Path("assets\\sound_effect\\combat_win.mp3").as_posix(),
}

audio = AudioManager()
audio.set_sfx_volume(0.5)
audio.set_music_volume(0.2)
