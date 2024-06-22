from webserver import keep_alive
import disnake
import os
from disnake.ext import commands


bot = commands.Bot(command_prefix="/", intents=disnake.Intents.all(), sync_commands_debug=True)
bot.load_extensions("cogs")
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f"{bot.user} is connected!") 
    await bot.change_presence(status=disnake.Status.idle, activity=disnake.Game("/помощь"))

keep_alive()
bot.run(os.getenv("TOKEN"))