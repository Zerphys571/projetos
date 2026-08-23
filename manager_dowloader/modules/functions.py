from modules.config import LIST_DIR, CONFIGS_EXT
from modules.logger import log_pastas
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from time import sleep
from winotify import Notification, audio


def verificar_pastas():
    list_error = []
    for i in LIST_DIR:
        try:
            i.mkdir(parents=True, exist_ok=True)
        except PermissionError as e:
            print("Ocorreu um erro de permissão nas pastas!\n")
            list_error.append(i)
        except OSError as e:
            print("Ocorreu um erro no sistema operacional!\n")
            list_error.append(i)
    (
        log_pastas("Ocorreu erro ao criar as pastas", list_error)
        if len(list_error) > 0
        else print("Nenhum problema encontrado")
    )


class Organizador(FileSystemEventHandler):
    def on_created(self, event):
        super().on_created(event)

        if not event.is_directory:
            file = Path(event.src_path)
            self.extension(file)

    def on_moved(self, event):
        super().on_moved(event)

        if not event.is_directory:
            file = Path(event.src_path)
            self.extension(file)

    def on_modified(self, event):
        super().on_modified(event)

        if not event.is_directory:
            file = Path(event.src_path)
            self.extension(file)

    def extension(self, file: Path) -> None:
        if not file.exists():
            return

        file_ext = file.suffix.lower()
        i = 0
        while i <= 5:
            try:

                if file_ext in CONFIGS_EXT["ext_doc"]:
                    file_path = self.path_file(file, LIST_DIR[4])
                    file.rename(file_path)
                elif file_ext in CONFIGS_EXT["ext_image"]:
                    file_path = self.path_file(file, LIST_DIR[2])
                    file.rename(file_path)
                elif file_ext in CONFIGS_EXT["ext_video"]:
                    file_path = self.path_file(file, LIST_DIR[3])
                    file.rename(file_path)
                elif file_ext in CONFIGS_EXT["ext_instal"]:
                    file_path = self.path_file(file, LIST_DIR[5])
                    file.rename(file_path)
                elif file_ext in CONFIGS_EXT["ext_tmp"]:
                    return
                else:
                    file_path = self.path_file(file, LIST_DIR[6])
                    file.rename(file_path)
            except PermissionError as e:
                sleep(1)
                i += 1
            else:
                break

    def path_file(self, file: Path, directory: Path) -> Path:
        i = 1
        final_file = directory / file.name

        while final_file.exists():
            new_name = f"{file.stem} ({i}){file.suffix}"
            final_file = directory / new_name
            i += 1

        return final_file

def notification() -> None:
    toast = Notification(
        app_id="📁 organizer",
        title ="Organizador de Downloads 📁",
        msg   ="O monitoramento está ativo!",
    )
    toast.set_audio(audio.Mail, loop=False)
    toast.show()

def exit_notification() ->None:
    toast = Notification(
        app_id="📁 organizer",
        title ="Encerrando organizador!",
        msg   ="O monitoramento está desativado!",
    )
    toast.set_audio(audio.Mail, loop=False)
    toast.show()