import os
from banco_dados import BancoDeDados
from interface_main import InterfaceTerminal


def main():
    interface = InterfaceTerminal()
    interface.exibir_menu()


if __name__ == "__main__":
    main()