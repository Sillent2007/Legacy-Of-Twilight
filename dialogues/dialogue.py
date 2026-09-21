class Dialogue:
    def __init__(self, name=" ", dialogue=None, start=0):

        if dialogue is None:
            dialogue = []

        self.name = name
        self.last_dialog = []
        if dialogue is None:
            dialogue = []
        self.dialogue = dialogue
        self.start = start

    def set_name(self, name):
        self.name = name

    def reset_start(self):
        self.start = 0


main_menu_welcome = Dialogue(
    dialogue=["SEJA MUITO BEM VINDO AO MEU PRIMEIRO PROJETO", "APROVEITE!!!"]
)

new_game = Dialogue(dialogue=["NOME DO SEU HERÓI"])

prologue_dialogue = [
    "Zerkan... um local esquecido no mapa",  # Inicio do dialogo em tela
    "Onde por longos e longos milênios, era conhecida pela sua prosperidade",
    "Até... a GRANDE SECA",
    "Durante anos, o céu permaneceu em silêncio",  # Inicio do dialogo em tela
    "Onde nenhuma gota de chuva caiu sobre Zerkan",
    "Plantações que sustentavam seu povo... se foram",
    "E consequentemente, por conta da falta de suprimento",  # Inicio do dialogo em tela
    "Os grandes gados iam se extinguindo a cada dia",
    "Como se não bastasse a sede e fome",  # Inicio do dialogo em tela
    "Aqueles sem onde ficar não suportavam o calor escaldante",
    "Nos levando a um futuro que pensávamos ser impossível de evitar",
    "Ao menos.. era o que pensávamos",  # Inicio do dialogo em tela
    "Na noite em que toda esperança se esgotou",  # Inicio do dialogo em tela
    "aquilo em que alguns consideram um presente do divino",
    "chegou em nossa terra",
    "E lá de dentro",  # Inicio do dialogo em tela
    "Um Frango..",  # Inicio do dialogo em tela
    "Pera... um frango??",
]
prologue = Dialogue(name="Narrador", dialogue=prologue_dialogue)

player_dialogue = [  # ---- DUSKWOOD VILLAGE ----
    "De novo esse sonho estranho",  # -- line 0 --
    "parece que acordei mais cedo do que o normal",
    "melhor eu tirar o pijama e ir comer alguma coisa.",
    "Bom dia mamãe!",  # Inicio do dialogo em tela
    "deu para sentir o cheiro lá de cima",
    "o papai ja saiu?",
    "Esse lugar está precisando de uma limpeza",  # Inicio do dialogo em tela
    "não podemos culpar os ratos",
    "aonde será que eles foram?",
    "Aí está você!",  # Inicio do dialogo em tela
    "uns chutes deve dar conta do recado.",  # -- line 10 --
    "Acho que agora está tudo certo!",  # Inicio do dialogo em tela
    "vou sair para andar um pouco.",
    "Vila movimentada hoje",  # Inicio do dialogo em tela
    "bom saber que os negócios estão indo bem",
    "Tenho sonhado praticamente toda noite", # Inicio do dialogo em tela
    "algo relacionado a Grande Seca e algumas pedras...",
    "E por algum motivo uma galinha, mas não acho que seja relevante.",
    "Sei que não faz muito sentido", # Inicio do dialogo em tela
    "mas sempre acordo me sentindo estranho depois",
    "sensação de que algo vai acontecer" # -- line 20 --
]
player = Dialogue(name="JOGADOR", dialogue=player_dialogue)


mother_dialogue = [
    "Bom dia querido!",  # line 0
    "seu pai precisou sair para a patrulha mais cedo",
    "teve relatos de brigas na aldeia ao Leste.",
    "Tenho uma tarefa para você",  # Inicio do dialogo em tela
    "mas antes, sente-se e coma!",
    "Espero que goste querido!",  # Inicio do dialogo em tela
    "Agora que terminou",  # Inicio do dialogo em tela
    "acabei encontrando alguns ratos no porão mais cedo",
    "acha que consegue cuidar disso para sua mãe?",
]
mother = Dialogue(name="Mãe", dialogue=mother_dialogue)

dilan_dialogue = [
    "Ei!",  # Inicio do dialogo em tela
    "Não acredito no que estou vendo.",
    "Que milagre você saindo da sua casa",  # Inicio do dialogo em tela
    "sumiu por uns dias.",
    "Você não me parece muito animado",  # Inicio do dialogo em tela
    "aconteceu alguma coisa?",
    "Agora sim, bem melhor.",  # Inicio do dialogo em tela
    "Me conta mais sobre o que está acontecendo.",
]
dilan = Dialogue(name="Dilan", dialogue=dilan_dialogue)
