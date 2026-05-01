import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} olarak giriş yaptı!')

@bot.command()
@commands.has_permissions(administrator=True) # Sadece yöneticiler kullanabilir
async def silkanal(ctx):
    await ctx.send("Bütün kanallar siliniyor...")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"Kanal silinemedi: {e}")

token = os.getenv('TOKEN')
bot.run(token)
