from telethon import TelegramClient, events

api_id = 23264159
api_hash = '0a16d597961547c158275f741842807d'
bot_token = '8385184232:AAHWyqJTv_A_f2kIIOXVSTKWC5TNwzQnhHw'
source_group_id = -1002773511066
target_channel_id = -1002860787429

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats=source_group_id))
async def handler(event):
    if event.media:
        await client.send_file(target_channel_id, event.media, caption=event.text)
    else:
        await client.send_message(target_channel_id, event.text)

print("Bot is running...")

client.run_until_disconnected()