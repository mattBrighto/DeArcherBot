import discord, time, datetime
import random
from discord import components
from discord.member import Member
from discord.user import User
from discord import Option
from discord.ui import Button
from discord.ui import View

#useful variables
commandsNum = 12
meMention = '<@650343691998855188>'
runStarted = time.perf_counter()
bot = discord.Bot(description=f'Awesome Bot made by {meMention}', debug_guilds=[919436076081381386])

#getting token
file = open('Z:/token.txt', "r")
token = file.read()
file.close()

#when the bot comes alive
@bot.event
async def on_ready():
    game = discord.Game("/help | pomoc | @DeArcher")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    global meUser
    meUser = await bot.fetch_user(650343691998855188)
    print("The prefix is /")
    print(f'{bot.user.name} is currently: {bot.status}')


#USER COMMANDS HERE
#
#
#



#help command... tho needs upgrade

@bot.command(name='help', description='Komenda pomocy')
async def help(ctx, category: Option(str, 'Kategoria pomocy - różne komendy posortowane', required=False)):
    msg = discord.Embed(color=0x1ABC9C, )
    msg.remove_author
    global commandsNum
    msg.add_field(name="Inofrmacje",  value=f'Hej {ctx.author.mention}, jestem tu żeby ci pomóc. Posiadam ``{str(commandsNum)}`` komend i ciągle jestem rozwijany', inline=False)
    msg.add_field(name="Lista komend", value=f'``/help user``\n``/help profil``\n``/help eko``\n``/help muzyka``\n``/help admin``\n``/help owner``\n\n **Lub skorzystaj z przycisków poniżej**', inline=True)
    msg.add_field(name='FAQ', value='1. Nie szukam collaba\n2. Bota można zakupić lub otrzymać bezpłatnie ode mnie\n3. Nie pisać na /kontakt jeżeli sprawa nie jest ważna', inline=True)
    msg.add_field(name='Linki', value='``🖥 vps`` https://mc.polishwrona.pl\n``📜 blog`` https://polishwrona.pl\n``🐈 git`` https://github.com/mattBrighto', inline=True)
    userton = Button(label='User', style=discord.ButtonStyle.grey, emoji='👤')
    profilton = Button(label='Profil', style=discord.ButtonStyle.grey, emoji='🤳')
    ekoton = Button(label='Ekonomia', style=discord.ButtonStyle.grey, emoji='💵')
    musicton = Button(label='Muzyka', style=discord.ButtonStyle.grey, emoji='🎤')
    adminton = Button(label='Admin', style=discord.ButtonStyle.grey, emoji='🚫')
    ownerton = Button(label='Owner', style=discord.ButtonStyle.grey, emoji='👑')
    
    async def userback(interaction):
        msg = discord.Embed(color=0x1ABC9C)
        msg.add_field(name='Komendy użytkownika', value=' \n\n``/help <kategoria>`` - Pomoc\n\n``/ping`` - Sprawdza ping i połączenie bota\n``/info`` - Pokazuje informacje dotyczące bota\n\n``/kontakt <wiadomość>`` - Komenda do kontaktowania się z twórcą bota\n\n``/clock`` - Pokazuje aktualny czas w Polsce')
        await interaction.response.send_message(embed=msg)
    
    async def adminback(interaction):
        msg = discord.Embed(color=0x1ABC9C)
        msg.add_field(name='Komendy admina', value=' \n\n``/ban <użytkownik> <powód>`` - Banuje użytkownika\n``/idban <id> <powód>`` - Banuje użytkownika po jego ID\n``/unban <użytkownik> <powód>`` - Unbanuje użytkownika\n``/idunban <id> <powód>`` - Unbanuje użytkownika po jego ID\n\n``/clear <ilość_wiadomości>`` - Usuwa wiadomości z kanału')
        await interaction.response.send_message(embed=msg)

    async def ownerback(interaction):
        msg = discord.Embed(color=0x1ABC9C)
        msg.add_field(name='Komendy ownera', value=' \n\n``/logout`` - Wyłącza bota\n\n``/say <wiadomość>`` - Bot wysyła podaną wiadomość (Wysyłamy wiadomość jako bot)')
        await interaction.response.send_message(embed=msg)

    userton.callback = userback
    adminton.callback = adminback
    ownerton.callback = ownerback
    view = View()
    view.add_item(userton)
    view.add_item(profilton)
    view.add_item(ekoton)
    view.add_item(musicton)
    view.add_item(adminton)
    view.add_item(ownerton)
    await ctx.respond(embed=msg, view=view)

#ping embeded command
@bot.command(name='ping', description='Komenda do sprawdzenia połączenia bota')
async def ping(ctx):
    msg = discord.Embed(color=0xE06666)
    msg.remove_author()
    secs = abs(runStarted - time.perf_counter())
    runtiming = time.strftime("%H godzin %M minut %S sekund", time.gmtime(secs))
    msg.add_field(name='PING Request', value=f'Jestem online, a mój ping wynosi ``{round(bot.latency * 1000)} ms 💨``\n Jestem włączony od : ``{runtiming} ⏰``', inline=False)
    await ctx.respond(embed=msg)

#info embeded command
@bot.command(name='info', description='Komenda informacji o bocie i jego twórcy')  
async def info(ctx):
    msg = discord.Embed(color=0x9C1ABC)
    msg.remove_author()
    msg.add_field(name='Podstawowe informacje', value=f'Hej jestem {meMention}. Zrobiłem tego bota For Fun, ale jeśli chciałbyś, abym wykonał jakiś projekt informatyczny/programistyczny skorzystaj z komendy /kontakt żeby się ze mną skontaktować', inline=True)
    secs = abs(runStarted - time.perf_counter())
    runtiming = time.strftime("%H:%M:%S", time.gmtime(secs))
    msg.add_field(name='Info Bota', value=f'runtime:   ``{runtiming} ⏰ ``\nping :	``{round(bot.latency * 1000)}  ms 💨 ``', inline=True)
    msg.add_field(name='Linki', value='``🔗 PERSONAL SITE``   https://mc.polishwrona.pl/', inline=False)
    await ctx.respond(embed=msg)

#contact limited command
@bot.command(name='kontakt', description='Komenda służąca do kontaktu z twórcą bota')
async def contact(ctx, msg: Option(str, "Twoja wiadomość", Required=False, default=True)):
    if type(msg) == bool:
        msg = discord.Embed(color=0xFFFFFF)
        msg.remove_author()
        msg.add_field(name=f'📖 **Komenda** : ``{ctx.command.name}``', value='Komenda do kontaktu z twórcą bota. (bez spamu)', inline=False)
        msg.add_field(name='🤚 **Wymagane uprawnienia** : ', value='~ Brak')
        msg.add_field(name='👉 **Przykładowe użycie** : ', value='``/kontakt Problem z botem``\n``/kontakt Hej``')
        await ctx.respond(embed=msg)
        return
    list = []
    if ctx.author.id in list:
        await ctx.respond("⌛ Musisz zaczekać zanim wyślesz kolejną wiadomość", delete_after = 1)
    else:
        global meUser
        dm = await meUser.create_dm()
        await dm.send(f'New message from {ctx.author.mention}: '+msg)
        list.append(ctx.author.id)
        await ctx.respond(f"||{ctx.author.mention}|| Twoja wiadomość została wysłana ✅")

#clock command.... needs upgrade, (thumbnail is correct)
@bot.command(name='zegar', description='Wyświetla aktualną godzinę w Polsce')
async def clock(ctx):
    msg = discord.Embed(title="Zegar", color=0xFFFFFF)
    msg.remove_author
    msg.set_thumbnail(url="https://mc.polishwrona.pl/clock.png")
    msg.add_field(name=time.strftime("%H:%M"), value="-------", inline=False)
    await ctx.respond(embed=msg)



#MOD COMMANDS HERE
#
#
#

#clear messages command
@bot.command(name='clear', description='Komenda służąca do czyszczenia chatu (Domyślnie 1000)')
async def clear(ctx, number: Option(int, required=False, default='-1112022')):
    if type(number) == str:
        msg = discord.Embed(color=0xFFFFFF)
        msg.remove_author()
        msg.add_field(name=f'📖 **Komenda** : ``{ctx.command.name}``', value='Czyści podaną ilość wiadomości z danego kanału. Nie działa na DM z botem.', inline=False)
        msg.add_field(name='🤚 **Wymagane uprawnienia** : ', value='~ Zarządzanie wiadomościami')
        msg.add_field(name='👉 **Przykładowe użycie** : ', value='``/clear 1000``\n``/clear 2341``')
        await ctx.respond(embed=msg)
        return
    x = len(await ctx.channel.purge(limit=number))
    await ctx.respond(f'❌ Pomyślnie usunięto {x} wiadomości!', delete_after = .5)

#ban command
@bot.command(name='ban', description='Banuje podanego użytkownika')
async def ban(ctx, user: Option(Member, 'Użytkownik do zbanowania',  required=False, default='-1112022'), rsn: Option(str, 'Powód bana', required=False, default='Nie określono')):
    if type(user) == str:
        msg = discord.Embed(color=0xFFFFFF)
        msg.remove_author()
        msg.add_field(name=f'📖 **Komenda** : ``{ctx.command.name}``', value='Banuje użytkowników. Można podać powód bana.', inline=False)
        msg.add_field(name='🤚 **Wymagane uprawnienia** : ', value='~ Banowanie członków')
        msg.add_field(name='👉 **Przykładowe użycie** : ', value='``/ban <@650343691998855188>``\n``/ban @user rsn``')
        await ctx.respond(embed=msg)
        return
    who = await bot.fetch_user(user.id)
    try:
        await who.send(f'||{who.mention}||')
    except:
        await ctx.author.send('Nie mogę napisać do użytkownika... Możliwe ,że nie ma go na serwerze lub nie dzielimy żadnych serwerów, ale i tak go zbanuję')
    else:
        dmMsg = discord.Embed(title='BAN', color=0x990000)
        dmMsg.set_author(name=ctx.author.name, icon_url=str(ctx.author.display_avatar))
        dmMsg.add_field(name=f'🔨 {who.display_name} zostałxś zbanowany 🔨', value=f'Zbanowany przez : {ctx.author.mention}\nZbanowany użytkownik : {who.mention}\nPowód bana : ``{rsn}``\nData : ``{datetime.datetime.now()}``', inline=True)
        await who.send(embed=dmMsg)
    await ctx.guild.ban(user=who, delete_message_days=0, reason=rsn)
    msg = discord.Embed(title='BAN', color=0x990000)
    msg.set_author(name=ctx.author.name, icon_url=str(ctx.author.display_avatar))
    msg.add_field(name=f'🔨 Użytkownik {who.display_name} został zbanowany 🔨', value=f'Zbanowany przez : {ctx.author.mention}\nZbanowany użytkownik : {who.mention}\nPowód bana : ``{rsn}``\nData : ``{datetime.datetime.now()}``', inline=True)
    await ctx.respond(embed=msg)

#idban command
@bot.command(name='idban', description='Banuje podanego użytkownika po id')
async def idban(ctx, id: Option(int, 'ID użytkownika do zbanowania', required=False, default='-1112022'), rsn: Option(str, 'Powód bana', required=False, default='Nie określono')):
    if type(id) == str:
        msg = discord.Embed(color=0xFFFFFF)
        msg.remove_author()
        msg.add_field(name=f'📖 **Komenda** : ``{ctx.command.name}``', value='Banuje użytkowników po ich id. Można podać powód bana.', inline=False)
        msg.add_field(name='🤚 **Wymagane uprawnienia** : ', value='~ Banowanie członków')
        msg.add_field(name='👉 **Przykładowe użycie** : ', value='``/idban 650343691998855188``\n``/idban 650343691998855188 rsn``')
        await ctx.respond(embed=msg)
        return
    who = await bot.fetch_user(id)
    try:
        await who.send(f'||{who.mention}||')
    except:
        await ctx.author.send('Nie mogę napisać do użytkownika... Możliwe ,że nie ma go na serwerze lub nie dzielimy żadnych serwerów, ale i tak go zbanuję')
    else:
        dmMsg = discord.Embed(title='BAN', color=0x990000)
        dmMsg.set_author(name=ctx.author.name, icon_url=str(ctx.author.display_avatar))
        dmMsg.add_field(name=f'🔨 {who.display_name} zostałxś zbanowany 🔨', value=f'Zbanowany przez : {ctx.author.mention}\nZbanowany użytkownik : {who.mention}\nPowód bana : ``{rsn}``\nData : ``{datetime.datetime.now()}``', inline=True)
        await who.send(embed=dmMsg)
    await ctx.guild.ban(user=who, delete_message_days=0, reason=rsn)
    msg = discord.Embed(title='BAN', color=0x990000)
    msg.set_author(name=ctx.author.name, icon_url=str(ctx.author.display_avatar))
    msg.add_field(name=f'🔨 Użytkownik {who.display_name} został zbanowany 🔨', value=f'Zbanowany przez : {ctx.author.mention}\nZbanowany użytkownik : {who.mention}\nPowód bana : ``{rsn}``\nData : ``{datetime.datetime.now()}``', inline=True)
    await ctx.respond(embed=msg)


#unban command
@bot.command(name='unban',desctiption='Unbanuje użytkownika')
async def unban(ctx, user: Option(Member, 'Użytkownik do zbanowania', required=False, default='-1112022'), rsn: Option(str, 'Powód unbana', required=False, default='Nie określono')):
    if type(user) == str:
        msg = discord.Embed(color=0xFFFFFF)
        msg.remove_author()
        msg.add_field(name=f'📖 **Komenda** : ``{ctx.command.name}``', value='Unbanuje użytkowników. Można podać powód bana.', inline=False)
        msg.add_field(name='🤚 **Wymagane uprawnienia** : ', value='~ Banowanie członków')
        msg.add_field(name='👉 **Przykładowe użycie** : ', value='``/unban <@650343691998855188>``\n``/ban @user rsn``')
        await ctx.respond(embed=msg)
        return
    who = await bot.fetch_user(user)
    await ctx.guild.unban(user=who,reason=rsn)
    msg = discord.Embed(title='UNBAN', color=0xCFF1EA)
    msg.set_author(name=ctx.author.name, icon_url=str(ctx.author.display_avatar))
    msg.add_field(name=f'🔨 Użytkownik {who.display_name} został obanowany 🔨', value=f'Odbanowany przez : {ctx.author.mention}\nZbanowany użytkownik : {who.mention}\nPowód unbana : ``{rsn}``\nData : ``{datetime.datetime.now()}``', inline=True)
    await ctx.respond(f'||{who.mention}||',embed=msg)

@bot.command(name='idunban',desctiption='Unbanuje użytkownika')
async def idunban(ctx, user: Option(int, 'Użytkownik do zbanowania',required=False, default='-1112022'), rsn: Option(str, 'Powód unbana', required=False, default='Nie określono')):
    if type(id) == str:
        msg = discord.Embed(color=0xFFFFFF)
        msg.remove_author()
        msg.add_field(name=f'📖 **Komenda** : ``{ctx.command.name}``', value='Unbanuje użytkowników po  id. Można podać powód bana.', inline=False)
        msg.add_field(name='🤚 **Wymagane uprawnienia** : ', value='~ Banowanie członków')
        msg.add_field(name='👉 **Przykładowe użycie** : ', value='``/idunban 650343691998855188``\n``/idunban 650343691998855188 rsn``')
        await ctx.respond(embed=msg)
        return
    who = await bot.fetch_user(user)
    await ctx.guild.unban(user=who,reason=rsn)
    msg = discord.Embed(title='UNBAN', color=0xCFF1EA)
    msg.set_author(name=ctx.author.name, icon_url=str(ctx.author.display_avatar))
    msg.add_field(name=f'🔨 Użytkownik {who.display_name} został obanowany 🔨', value=f'Odbanowany przez : {ctx.author.mention}\nZbanowany użytkownik : {who.mention}\nPowód unbana : ``{rsn}``\nData : ``{datetime.datetime.now()}``', inline=True)
    await ctx.respond(f'||{who.mention}||',embed=msg)
    



#OWNER COMMANDS HERE
#
#
#

#logout owner command
@bot.command(name='logout', desciption='Komenda służąca do wyłączenia bota')
async def logout(ctx):
    if ctx.author.id != 650343691998855188:
        await ctx.respond("⛔ Nie masz wystarczających uprawnień :<", delete_after=.5)
    if ctx.author.id == 650343691998855188:
        msg = discord.Embed(title='Disconnecting.....', color=0x723535)
        msg.remove_author()
        secs = abs(runStarted - time.perf_counter())
        runtiming = time.strftime("%H godzin %M minut %S sekund", time.gmtime(secs))
        msg.add_field(name='------------------', value=f'{ctx.author.mention}, wylogowałeś mnie :< \nByłem włączony przez : ``{runtiming} ⏰ ``\nMój ping wynosi : ``{round(bot.latency * 1000)}  💨`` \n D1sScoo0nneCt1ing....', inline=True)
        await ctx.respond(embed=msg)
        print("\n\n\n\nDISCONNECTING\n\n\n\n")
        await discord.Client.close(bot)

#say owner command
@bot.command(name='say', description='Komenda służąca do kontrolowania wiadomości bota')
async def say(ctx, msg: Option(str, 'Wiadomość, którą bot ma wysłać', required=False, default=True)):
    if type(msg) == bool:
        msg = discord.Embed(color=0xFFFFFF)
        msg.remove_author()
        msg.add_field(name=f'📖 **Komenda** : ``{ctx.command.name}``', value='Mówisz jako bot.', inline=False)
        msg.add_field(name='🤚 **Wymagane uprawnienia** : ', value='~ Owner bota')
        msg.add_field(name='👉 **Przykładowe użycie** : ', value='``/say Strzeż się``\n``/say Jestem botem``')
        await ctx.respond(embed=msg)
        return
    if ctx.author.id != 650343691998855188:
        await ctx.respond("⛔ Nie masz wystarczających uprawnień :<", delete_after = .5)
    if ctx.author.id == 650343691998855188:
        botsay = ""
        list = ['0', 'o']
        for l in msg:
            botsay = botsay +  random.choice(list)
        await ctx.respond(botsay, delete_after = .0001)
        await ctx.send(msg)

bot.run(token)
