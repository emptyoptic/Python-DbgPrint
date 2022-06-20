from turtle import back
from colorama import init, Fore, Back, Style
import os
from datetime import datetime

init(convert=True)

class debugging:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    class types:
        debug = "debug",
        error = "error",
        warning = "warning",
        note = "note"
def DbgPrint(type: debugging.types, msg: str) -> str:
    colored_debug = Fore.GREEN + msg + Fore.RESET + Back.RESET
    colored_error = Fore.RED + msg + Fore.RESET + Back.RESET
    colored_warning = Fore.YELLOW + msg + Fore.RESET + Back.RESET
    colored_note = Fore.BLUE + msg + Fore.RESET + Back.RESET

    match type:
        case debugging.types.debug:
            print(f"{Back.GREEN}{Fore.BLACK}[*] Debug message ({debugging.current_time}):{Back.RESET}\n{colored_debug}")
        case debugging.types.error:
            print(f"{Back.RED}{Fore.BLACK}[*] Error message ({debugging.current_time}):{Back.RESET}\n{colored_error}")
        case debugging.types.warning:
            print(f"{Back.YELLOW}{Fore.BLACK}[*] Warning message ({debugging.current_time}):{Back.RESET}\n{colored_warning}")
        case debugging.types.note:
            print(f"{Back.BLUE}{Fore.BLACK}[*] Note ({debugging.current_time}):{Back.RESET}\n{colored_note}")
        case _:
            print(f"{Fore.BLACK}{Back.RED}Wrong type. Types: debug, error, warning, note{Fore.RESET}{Back.RESET}")


def main():
    DbgPrint(debugging.types.debug, "Hello")
    DbgPrint(debugging.types.error, "Hello")
    DbgPrint(debugging.types.warning, "Hello")
    DbgPrint(debugging.types.note, "Hello")
    os.system("pause")

if __name__ == "__main__":
    main()