from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Group", url="https://t.me/yt_vidio_download_sl")],
        [InlineKeyboardButton(
            "දෝෂ වාර්තා කරන්න 🤗", url="https://t.me/youtube_video_downloader_sl_sup")]
    ])
    welcomed = f"හලෝ <b>{message.from_user.first_name}</b>\n/වැඩිදුර තොරතුරු සඳහා උදව්"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
