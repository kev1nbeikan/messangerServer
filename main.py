import asyncio

import config
from pyrogram import Client
from pyrogram import filters
from pyrogram import types

app = Client("account", config.api_id, config.api_hash)
is_turn = True


def check_below_16_from_davinci_msg(text: str):
    return text is not None and text.split(', ')[1] <= "16"


@app.on_message(filters=filters.chat(config.da_vinci_id))
async def handle_davinci_msg(client: Client, message: types.Message):
    global is_turn
    if is_turn and message.from_user.is_bot:
        if check_below_16_from_davinci_msg(message.caption):
            await asyncio.sleep(0.5)
            await client.send_message(message.chat.id, '👎')
    else:
        if message.text == "стоп":
            is_turn = False
            await message.reply('clientBot: остановился')
        if message.text == "дальше":
            is_turn = True
            await message.reply('clientBot: продолжаю')


app.run()
