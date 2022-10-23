from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
   
    welcomed = f"Привет <b>{message.from_user.first_name}</b> Отправь боту ссылку на Youtube видео и мы пришлем тебе аудио или видео для скачивания"
    await message.reply_text(welcomed)
    raise StopPropagation
