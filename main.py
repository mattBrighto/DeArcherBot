from typing_extensions import runtime
import discord, time, logging
from discord.ext import commands

#logging
logging.basicConfig(level=logging.INFO)

#useful variables
runStarted = time.perf_counter()
bot = discord.Bot()
UserMatt = bot.get_or_fetch_user(650343691998855188)
meMention = '<@650343691998855188>'

#getting token
file = open('Z:/token.txt', "r")
token = file.read()
file.close()

#when the bot comes alive
@bot.event
async def on_ready():
    global meUser
    meUser = await bot.get_or_fetch_user(650343691998855188)
    print("The prefix is /")
    print('Bot is currently: Online')

#ping embeded command
@bot.command()
async def ping(ctx):
    msg = discord.Embed(title="PING Request", color=0xE06666)
    msg.remove_author()
    secs = abs(runStarted - time.perf_counter())
    runtiming = time.strftime("%H godzin %M minut %S sekund", time.gmtime(secs))
    msg.add_field(name='------------', value=f'Jestem online, a mój ping wynosi ``{round(bot.latency * 1000)} ms``\nJestem włączony od : ``{runtiming}``', inline=False)
    await ctx.respond(embed=msg)

#info embeded command
@bot.command()  
async def info(ctx):
    msg = discord.Embed(color=0x9C1ABC)
    msg.remove_author()
    msg.add_field(name='Basic Info', value=f'Hej jestem {meMention}. Zrobiłem tego bota For Fun, ale jeśli chciałbyś, abym wykonał jakiś projekt informatyczny/programistyczny skorzystaj z komendy /contact (oczywiście z odpowiednim prefixem) żeby się ze mną skontaktować')
    secs = abs(runStarted - time.perf_counter())
    runtiming = time.strftime("%H godzin %M minut %S sekund", time.gmtime(secs))
    msg.add_field(name='Info Bota', value=f'``runtime:``   {runtiming}\n ``ping`` :	{round(bot.latency * 1000)}  ms')
    msg.add_field(name='Linki', value='``PERSONAL SITE``   https://mc.polishwrona.pl/', inline=False)
    await ctx.respond(embed=msg)

#contact limited command
@bot.command()
async def contact(ctx, msg):
    list = []
    if ctx.author.id in list:
        await ctx.respond("Musisz zaczekać zanim wyślesz kolejną wiadomość", delete_after = 1)
    else:
        global meUser
        dm = await meUser.create_dm()
        await dm.send(f'New message from {ctx.author.mention}: '+msg)
        list.append(int(ctx.author.id))
        await ctx.respond(f"||{ctx.author.mention}|| Twoja wiadomość została wysłana")

#say owner command
@bot.command()
async def say(ctx, msg):
    if ctx.author.id != 650343691998855188:
        await ctx.respond("Nie masz wystarczających uprawnień :<", delete_after = .5)
    if ctx.author.id == 650343691998855188:
        await ctx.send(msg)
        
#clear messages command.... but still want to display deleted messages not how many were supposed to be
@bot.command()
async def clear(ctx, x):
    await ctx.channel.purge(limit=int(x))
    await ctx.respond(f'Pomyślnie usunięto {x} wiadomości!', delete_after = 1)

#clock command.... needs upgrade, (thumbnail is correct)
@bot.command()
async def clock(ctx):
    msg = discord.Embed(title="Zegar", color=0xFFFFFF)
    msg.set_author(name= ctx.author.name, icon_url= str(ctx.author.display_avatar))
    msg.set_thumbnail(url="https://mc.polishwrona.pl/clock.png")
    msg.add_field(name=time.strftime("%H:%M"), value="-------", inline=False)
    await ctx.respond(embed=msg)

#logout owner command
@bot.command()
async def logout(ctx):
    if ctx.author.id != 650343691998855188:
        ctx.respond("Nie masz wystarczających uprawnień :<", delet_after=1)
    if ctx.author.id == 650343691998855188:
        msg = discord.Embed(title='Disconnecting.....', color=0x723535)
        msg.remove_author
        secs = abs(runStarted - time.perf_counter())
        runtiming = time.strftime("%H godzin %M minut %S sekund", time.gmtime(secs))
        msg.add_field(name='------------------', value=f'{ctx.author.mention}, wylogowałeś mnie :< \n Byłem włączony przez : ``{runtiming}``\nMój ping wynosi : ``{round(bot.latency * 1000)}`` \n D1sScoo0nneCt1ing....', inline=True)
        await ctx.respond(embed=msg)
        print("\n\n\n\nDISCONNECTING\n\n\n\n")
        await discord.Client.close(bot)

bot.run(token)
