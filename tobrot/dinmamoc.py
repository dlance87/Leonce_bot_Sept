

from tobrot.get_cfg import get_config


class Commandi:
    LEECH = get_config(
        "COMMANDI_LEECH",
        "leech"
    )
    PURGE = get_config(
        "COMMANDI_PURGE",
        "purge"
    )
    YTDL = get_config(
        "COMMANDI_YTDL",
        "ytdl"
    )
    STATUS = get_config(
        "COMMANDI_STATUS",
        "status"
    )
    CANCEL = get_config(
        "COMMANDI_CANCEL",
        "cancel"
    )
    EXEC = get_config(
        "COMMANDI_EXEC",
        "exec"
    )
    EVAL = get_config(
        "COMMANDI_EVAL",
        "eval"
    )
    RENAME = get_config(
        "COMMANDI_RENAME",
        "rename"
    )
    UPLOAD = get_config(
        "COMMANDI_UPLOAD",
        "upload"
    )
    HELP = get_config(
        "COMMANDI_HELP",
        "help"
    )
    SAVETHUMBNAIL = get_config(
        "COMMANDI_SAVETHUMBNAIL",
        "savethumbnail"
    )
    CLEARTHUMBNAIL = get_config(
        "COMMANDI_CLEARTHUMBNAIL",
        "clearthumbnail"
    )
    GET_RCLONE_CONF_URI = get_config(
        "COMMANDI_GET_RCLONE_CONF_URI",
        "getrcloneconfuri"
    )
    UPLOAD_LOG_FILE = get_config(
        "COMMANDI_UPLOAD_LOG_FILE",
        "log"
    )
