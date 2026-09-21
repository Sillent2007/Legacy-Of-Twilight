from readchar import key, readkey

from core import utils


def select_option_interface(
    title,
    *args,
    opc_color="yellow",
    title_color="reset",
    title_symbol=" ",
    position="left",
):
    indice = 0
    while True:
        utils.clear()
        utils.title(title, color=title_color, symbol=title_symbol)

        for i, opc in enumerate(args):
            if i == indice:
                opc = f">  {opc}"
            else:
                opc = f"   {opc}"

            opc = utils.colour[opc_color] + opc + utils.colour["reset"]
            if position == "left":
                print(utils.center(opc))
                print("")
            elif position == "center":
                print(utils.center(opc))
        utils.line("=", "purple")

        tecla = readkey()

        if tecla == key.UP:
            indice -= 1

        elif tecla == key.DOWN:
            indice += 1

        elif tecla == key.ENTER:
            return args[indice].strip().lower()

        indice %= len(args)


def message(msg, color="reset"):
    msg = utils.colour[color] + f"-------- {msg} --------" + utils.colour["reset"]
    print(utils.center(msg))


if __name__ == "__main__":
    message("Você ganhou 5 xp", color="green")
