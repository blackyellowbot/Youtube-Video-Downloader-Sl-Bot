from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"В настоящее время поддерживает только Youtube Single (без плейлиста) Отправить URL-адрес Youtube"
    await message.reply_text(helptxt)
