import sys
from pathlib import Path
from colorama import init, Fore, Style


init(autoreset=True)


def list_directory_structure(path: str | Path, indent: str = "") -> None:
   
    try:
        p = Path(path)

        if not p.exists():
            print(f"{Fore.RED}Помилка: Шлях '{path}' не існує.")
            return

        if not p.is_dir():
            print(f"{Fore.RED}Помилка: '{path}' не є директорією.")
            return

        if indent == "":
            print(f"{Fore.BLUE}{p.name}/")
            indent = "  "

        items = sorted(p.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))

        for item in items:
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/")
                
                list_directory_structure(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")

    except Exception as e:
        print(f"{Fore.RED}Сталася непередбачена помилка: {e}")


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Використання: python Task_03/task_03.py [шлях_до_директорії]")
    else:
        directory_path = sys.argv[1]
        list_directory_structure(directory_path)