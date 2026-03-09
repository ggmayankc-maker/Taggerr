import asyncio
from pyrogram import Client, filters

API_ID = 32507403
API_HASH = "a5d57029811e4ac4bda7293265ae5954"
BOT_TOKEN = "8618488026:AAEsGg_8FnrRoSqsoCr4RhL_2YfT5L3GMlg"

app = Client("taggerbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

tagging = False

@app.on_message(filters.command("tagall") & filters.group)
async def tag_all(client, message):
    global tagging
    admins = [admin.user.id async for admin in client.get_chat_members(message.chat.id, filter="administrators")]

    if message.from_user.id not in admins:
        await message.reply("❌ Only admins can use this command")
        return

    tagging = True
    await message.reply("✅ Starting TagAll...")

    async for member in client.get_chat_members(message.chat.id):
        if not tagging:
            break

        if member.user.is_bot:
            continue

        try:
            await message.reply(f"[{member.user.first_name}](tg://user?id={member.user.id})")
            await asyncio.sleep(1)
        except:
            pass


@app.on_message(filters.command("stop") & filters.group)
async def stop_tag(client, message):
    global tagging
    tagging = False
    await message.reply("🛑 Tagging stopped")


app.run()

