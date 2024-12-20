import google.generativeai as genai
import discord
from dotenv import load_dotenv
from os import getenv


async def chat_genai(msg):
    gemini_pro = genai.GenerativeModel()
    response = gemini_pro.generate_content(msg)
    return response.text


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix := "$AI"):
        msg = message.content.removeprefix(prefix)
        try:
            print(msg)
            response = await chat_genai(msg)
            await message.channel.send(response)
        except Exception as e:
            print(e)
            await message.channel.send("エラーが発生しました。")


if __name__ == "__main__":
    load_dotenv()
    genai.configure(api_key=getenv("GOOGLE_API_KEY"))
    client.run(getenv("DISCORD_TOKEN"))
