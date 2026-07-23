import discord
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    print("Content:", message.content)
    print("Embeds:", message.embeds)
    print("Attachments:", message.attachments)
    print("Snapshots:", getattr(message, "message_snapshots", None))
    print("Raw message:", message)

    # Only respond to DMs
    if isinstance(message.channel, discord.DMChannel):
        with open("knowledge_base.txt", "a", encoding="utf-8") as f:
            f.write(f"\n[{datetime.now()}]\n")
            f.write(f"{message.author}: {message.content}\n")
            f.write("-" * 50 + "\n")

        await message.channel.send("Saved! ✅")

client.run(TOKEN)
