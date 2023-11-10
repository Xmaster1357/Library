import disnake
from disnake.ext import commands


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name = "помощь", description="информация о боте Library")
    async def __help(self, inter):
        embed = disnake.Embed(title="**Что это такое?**", description="""_Данный бот представляет собой библиотеку с различными книгами/статьями. Бот полностью на русском языке, написан на python (disnake).
    Library предоставит вам возможность не только читать интереснейшие статьи или книги, но и писать их! Написанные вами произведения смогут прочитать такие же пользователи discord как и вы.
    Что не менее важно, так это то, что вы можете сделать свои книги/статьи платными и получать с них доход! Цену устанавливаете вы сами, небольшой процент от ваших доходов будет идти на развитие проекта Library, остальное всё ваше!
    Чтобы начать читать книги/статьи вы должны прописать команду - ```/категории``` и выбрать нужную вам категорию, затем нажать на интересующий вас контент._""", colour = disnake.Color.random()) # url="https://avito.ru"
        embed.set_thumbnail(file=disnake.File("library.png"))
        embed.set_footer(text=f"✏ {inter.author.name}")
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(help(bot))