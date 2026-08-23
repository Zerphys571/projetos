from modules.config import LIST_DIR
from modules.functions import verificar_pastas, Organizador, notification, exit_notification
from watchdog.observers import Observer
import time

def app() -> None:
    notification()
    verificar_pastas()
    my_organizer = Organizador()
    observer = Observer()

    observer.schedule(my_organizer, LIST_DIR[0], recursive=False)

    observer.start()

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print("Encerrando aplicação...")
    finally:
        exit_notification()
        observer.stop()
        observer.join()

if __name__ == "__main__":
  app()