import disnake
from disnake.ext import commands


class category(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    class Programming_Button(disnake.ui.View):
        def __init__(self):
            super().__init__()
            #self.add_item(disnake.ui.Button(label="1", style=disnake.ButtonStyle.blurple))
        @disnake.ui.button(label="1", style=disnake.ButtonStyle.blurple)
        async def button1(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            embed = disnake.Embed(title="Язык программирования python", description = "Test", colour = disnake.Color.random())
            embed.set_footer(text=f"✏ {inter.author.name}")
            await inter.send(embed=embed)
        @disnake.ui.button(label="2", style=disnake.ButtonStyle.blurple)
        async def button2(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            embed = disnake.Embed(title="PrTest2", description = "Test", colour = disnake.Color.random())
            embed.set_footer(text=f"✏ {inter.author.name}")
            await inter.send(embed=embed)
        @disnake.ui.button(label="3", style=disnake.ButtonStyle.blurple)
        async def button3(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            embed = disnake.Embed(title="PrTest3", description = "Test", colour = disnake.Color.random())
            embed.set_footer(text=f"✏ {inter.author.name}")
            await inter.send(embed=embed)


    class Iskustvo_Button(disnake.ui.View):
        def __init__(self):
            super().__init__()
        @disnake.ui.button(label="1", style=disnake.ButtonStyle.blurple)
        async def button1(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            embed = disnake.Embed(title="IskustvoTest1", description = "Test", colour = disnake.Color.random())
            embed.set_footer(text=f"✏ {inter.author.name}")
            await inter.send(embed=embed)
        @disnake.ui.button(label="2", style=disnake.ButtonStyle.blurple)
        async def button2(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            embed = disnake.Embed(title="IskustvoTest2", description = "Test", colour = disnake.Color.random())
            embed.set_footer(text=f"✏ {inter.author.name}")
            await inter.send(embed=embed)
        @disnake.ui.button(label="3", style=disnake.ButtonStyle.blurple)
        async def button3(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            embed = disnake.Embed(title="IskustvoTest3", description = "Test", colour = disnake.Color.random())
            embed.set_footer(text=f"✏ {inter.author.name}")
            await inter.send(embed=embed)


    class Bisnes_and_invest(disnake.ui.View):
        def __init__(self):
            super().__init__()
        @disnake.ui.button(label="1", style=disnake.ButtonStyle.blurple)
        async def button1(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            embed = disnake.Embed(title="BisnesTest1", description = "Test", colour = disnake.Color.random())
            embed.set_footer(text=f"✏ {inter.author.name}")
            await inter.send(embed=embed)
        @disnake.ui.button(label="2", style=disnake.ButtonStyle.blurple)
        async def button2(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            embed = disnake.Embed(title="BisnesTest2", description = "Test", colour = disnake.Color.random())
            embed.set_footer(text=f"✏ {inter.author.name}")
            await inter.send(embed=embed)
        @disnake.ui.button(label="3", style=disnake.ButtonStyle.blurple)
        async def button3(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            embed = disnake.Embed(title="BisnesTest3", description = "Test", colour = disnake.Color.random())
            embed.set_footer(text=f"✏ {inter.author.name}")
            await inter.send(embed=embed)


    class Dropdown(disnake.ui.StringSelect):
        def __init__(self):
            options = [
                disnake.SelectOption(label="Программирование", emoji="👨‍💻", value="1"), # description="test" 
                disnake.SelectOption(label="Искусство и дизайн", emoji="🎨", value="2"),
                disnake.SelectOption(label="Бизнес и инвестиции", emoji="💸", value="3"),
                disnake.SelectOption(label="Медицина", emoji="💉", value="4"),
                disnake.SelectOption(label="Здоровье и спорт", emoji="💪", value="5"),
                disnake.SelectOption(label="Психология", emoji="🎭", value="6"),
                disnake.SelectOption(label="Кулинария и домашнее хозяйство", emoji="🍽", value="7")
            ]
            super().__init__(placeholder="Выбрать:", min_values=1, max_values=1, options=options)# min_values=1 - минимальный выбор количества элементов | max_values=1 - максимальный выбор количества элементов
        async def callback(self, inter: disnake.MessageInteraction):
            if self.values[0] == "1":
                embed = disnake.Embed(title="_Список доступных книг/статей для чтения на тему ```Программирование:```_", colour = 0x006400)
                embed.add_field(name = "1. Python", value = "Описание книги")
                embed.add_field(name = "2. Test", value = "Описание книги")
                embed.add_field(name = "3. Test", value = "Описание книги")
                embed.set_footer(text=f"✏ {inter.author.name}")
                view = Programming_Button()
                await inter.send(embed=embed, view=view)
            if self.values[0] == "2":
                embed = disnake.Embed(title="_Список доступных книг/статей для чтения на тему ```Искусство и дизайн:```_", colour = disnake.Color.random())
                embed.add_field(name = "1. Test", value = "Описание книги")
                embed.add_field(name = "2. Test", value = "Описание книги")
                embed.add_field(name = "3. Test", value = "Описание книги")
                embed.set_footer(text=f"✏ {inter.author.name}")
                view = Iskustvo_Button()
                await inter.send(embed=embed, view=view)
            if self.values[0] == "3":
                embed = disnake.Embed(title="_Список доступных книг/статей для чтения на тему ```Бизнес и инвестиции:```_", colour = disnake.Color.random())
                embed.add_field(name = "1. Test", value = "Описание книги")
                embed.add_field(name = "2. Test", value = "Описание книги")
                embed.add_field(name = "3. Test", value = "Описание книги")
                embed.set_footer(text=f"✏ {inter.author.name}")
                view = Bisnes_and_invest()
                await inter.send(embed=embed, view=view) 
            if self.values[0] == "4":
                embed = disnake.Embed(title="_Список доступных книг/статей для чтения на тему ```Медицина:```_", colour = disnake.Color.random())
                embed.add_field(name = "1. Test", value = "Описание книги")
                embed.add_field(name = "2. Test", value = "Описание книги")
                embed.add_field(name = "3. Test", value = "Описание книги")
                embed.set_footer(text=f"✏ {inter.author.name}")
                await inter.send(embed=embed)
            if self.values[0] == "5":
                embed = disnake.Embed(title="_Список доступных книг/статей для чтения на тему ```Здоровье и спорт:```_", colour = disnake.Color.random())
                embed.add_field(name = "1. Test", value = "Описание книги")
                embed.add_field(name = "2. Test", value = "Описание книги")
                embed.add_field(name = "3. Test", value = "Описание книги")
                embed.set_footer(text=f"✏ {inter.author.name}")
                await inter.send(embed=embed)
            if self.values[0] == "6":
                embed = disnake.Embed(title="_Список доступных книг/статей для чтения на тему ```Психология:```_", colour = disnake.Color.random())
                embed.add_field(name = "1. Test", value = "Описание книги")
                embed.add_field(name = "2. Test", value = "Описание книги")
                embed.add_field(name = "3. Test", value = "Описание книги")
                embed.set_footer(text=f"✏ {inter.author.name}")
                await inter.send(embed=embed)
            if self.values[0] == "7":
                embed = disnake.Embed(title="_Список доступных книг/статей для чтения на тему ```Кулинария и домашнее хозяйство:```_", colour = disnake.Color.random())
                embed.add_field(name = "1. Test", value = "Описание книги")
                embed.add_field(name = "2. Test", value = "Описание книги")
                embed.add_field(name = "3. Test", value = "Описание книги")
                embed.set_footer(text=f"✏ {inter.author.name}")
                await inter.send(embed=embed)

    class DropdownView(disnake.ui.View):
        def __init__(self):
            super().__init__()
            self.add_item(Dropdown())

    @commands.slash_command(name = "категории", description="выбрать нужную категорию для чтения") 
    async def __category(self, inter):
        await inter.send("_Выберите категорию для чтения_", view = DropdownView())
.

def setup(bot):
    bot.add_cog(category(bot))