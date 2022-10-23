from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("DEVS", url="https://t.me/iromch")],
        [InlineKeyboardButton(
            "SUPPORT", url="https://t.me/qododev")]
    ])
    welcomed = f"Привет <b>{message.from_user.first_name}</b> Отправь боту ссылку на Youtube видео и мы пришлем тебе аудио или видео для скачивания"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
