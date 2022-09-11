from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"දැනට සහාය දක්වන්නේ Youtube Single එකකට පමණි (ධාවන ලැයිස්තුවක් නොමැත) Youtube Url යවන්න"
    await message.reply_text(helptxt)
