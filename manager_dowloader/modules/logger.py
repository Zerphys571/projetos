from pathlib import Path
from datetime import datetime
from modules.config import DIR_LOGS


def log_pastas(mensagem: str, diretorio: list[Path] | str) -> None:
    date = datetime.now().strftime("%H:%M:%S")
    try:
        with open(DIR_LOGS / "manager.log", "a") as file:
            file.write(f"[{date}] {mensagem} - {diretorio}\n")
    except PermissionError as e:
        print(f"Erro de permissões ao abrir o arquivo em: {DIR_LOGS}/manager\n")
    except OSError as e:
        print(f"Erro no sistema ao abrir o arquivo em: {DIR_LOGS}/manager.log\n")


def log_file(mensagem: str, file: Path) -> None:
    date = datetime.now().strftime("%H:%M:%S")
    try:
        with open(DIR_LOGS / "manager.log", "a") as log_file:
            log_file.write(f"[{date}] {mensagem} - {file}\n")
    except PermissionError as e:
        print(f"Erro de permissões ao abrir o arquivo em: {DIR_LOGS}/manager.log\n")
    except OSError as e:
        print(f"Erro no sistema ao abrir o arquivo em: {DIR_LOGS}/manager.log\n")
