import disnake
from disnake.ext import commands


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name = "помощь", description="информация о боте Library")
    async def __help(self, inter):
        embed = disnake.Embed(title="**Что это такое?**", description="""_Данный бот представляет собой хранилище данных с различной полезной информацией на конкретном сервере. Бот написан на python с использованием библиотеки disnake.
    Library предоставит вам возможность легко и удобно хранить важный контент сервера! Одной простой командой или несколькими кликами вы сможете открывать списки ролей, правила, информацию о сервере, описания событий, правила Roleplay и абсолютно любые тексты, которые вы сохраните в боте.
    Что не менее важно, так это то, что благодаря функционалу бота, любой участник сервера сможет с комфортом просмотреть всю нужную ему информацию, тем самым улучшая опыт работы с Discord!
    Чтобы выбрать интересующий вас контент пропишите команду - ```/категории```._""", colour = disnake.Color.random()) # url="https://avito.ru"
        embed.set_thumbnail(file=disnake.File("library.png"))
        embed.set_footer(text=f"✏ {inter.author.name}")
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(help(bot))