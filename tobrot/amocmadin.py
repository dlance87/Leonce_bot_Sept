

from tobrot.get_cfg import get_config


class Loilacaztion:
    PROCESSING = get_config(
        "STRINGS_PROCESSING",
        "processing ..."
    )

    CLEARED_THUMBNAIL = get_config(
        "STRINGS_CLEARED_THUMBNAIL",
        "✅ Custom thumbnail cleared succesfully."
    )
    HELP_SAVE_THUMBNAIL = get_config(
        "STRINGS_HELP_SAVE_THUMBNAIL",
        "Reply to a photo to save custom thumbnail"
    )
    SAVED_THUMBNAIL = get_config(
        "STRINGS_SAVED_THUMBNAIL",
        (
            "Custom video / file thumbnail saved. "
            "This image will be used in the upload, till /clearthumbnail."
        )
    )

    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "There is no help here"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    NO_TOR_STATUS = get_config(
        "STRINGS_NO_TOR_STATUS",
        "🤷‍♂️ No Active, Queued or Paused TORRENTs"
    )
    TOR_CANCELLED = get_config(
        "STRINGS_TOR_CANCELLED",
        "Torrent 🧲 Cancelled"
    )
    TOR_CANCEL_FAILED = get_config(
        "STRINGS_TOR_CANCEL_FAILED",
        "<i>FAILED</i>\n\n#error"
    )
