import disnake
from disnake.ext import commands


bot = commands.Bot(command_prefix="/", intents=disnake.Intents.all(), sync_commands_debug=True)
bot.load_extensions("cogs")
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f"{bot.user} is connected!") 
    await bot.change_presence(status=disnake.Status.idle, activity=disnake.Game("/помощь"))


bot.run('MTA3MDc4NDQzOTk2MzEwNzM3OA.GkiSFf.UyhhKLzM_xzZCcWnumqwwc2P004KbcB01P-fMg')