from pathlib import Path

DIR_HOME = Path.home()
DIR_DOWNLOADS = DIR_HOME / "Downloads"
DIR_LOGS = DIR_HOME / "Documents" / "logs_manager"


DIR_IMAGENS = DIR_DOWNLOADS / "Imagens"
DIR_VIDEOS = DIR_DOWNLOADS / "Videos"
DIR_DOCUMENTOS = DIR_DOWNLOADS / "Documentos"
DIR_INSTALADORES = DIR_DOWNLOADS / "Instaladores"
DIR_OUTROS = DIR_DOWNLOADS / "Outros"

LIST_DIR = [
    DIR_DOWNLOADS,
    DIR_LOGS,
    DIR_IMAGENS,
    DIR_VIDEOS,
    DIR_DOCUMENTOS,
    DIR_INSTALADORES,
    DIR_OUTROS,
]

CONFIGS_EXT = {
    "ext_doc"    : (".pdf", ".docx", ".xlsx"),
    "ext_image"  : (".jpg", ".png", ".gif", ".jpeg", ".webp", ".raw", ".heic", ".heif", ".svg"),
    "ext_video"  : (".mp4", ".mkv", ".wmv", ".mov", ".avi", ".webm"),
    "ext_instal" : (".exe", ".msi"),
    "ext_tmp"    : (".tmp", ".crdownload")
}