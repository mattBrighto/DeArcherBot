import discord, time
from discord.ext import commands
runStarted = time.perf_counter()
bot = discord.Bot()
meMention = '<@650343691998855188>'
file = open('Z:/token.txt', "r")
token = file.read()
file.close()

@bot.event
async def on_ready():
    print("The prefix is /")
    print('Bot is currently: Online')

@bot.command()
async def ping(ctx):
    await ctx.send(ctx.author.mention + ', Jestem online! PONG 🏓')

@bot.command()  
async def info(ctx):
    msg = discord.Embed(color=0x9C1ABC)
    msg.remove_author()
    msg.add_field(name='Basic Info', value=f'Hej jestem {meMention}. Zrobiłem tego bota For Fun, ale jeśli chciałbyś, abym wykonał jakiś projekt informatyczny/programistyczny skorzystaj z komendy /contact (oczywiście z odpowiednim prefixem) żeby się ze mną skontaktować')
    secs = abs(runStarted - time.perf_counter())
    runtiming = time.strftime("%H:%M:%S", time.gmtime(secs))
    msg.add_field(name='Info Bota', value=f'``runtime:``   {runtiming}')
    msg.add_field(name='Linki', value='``PERSONAL SITE``   https://mc.polishwrona.pl/', inline=False)
    await ctx.send(embed=msg)

@bot.command()
async def contact(ctx, msg):
    list = []
    if ctx.message.author.id in list:
        await ctx.send("Musisz zaczekać zanim wyślesz kolejną wiadomość", delete_after = 2)
    else:
        global bot
        meUser = bot.fetch_user(65034369199885518)
        meDM = meUser.create_dm()
        await meDM.send(f'New message from {ctx.author.mention}: '+msg)


@bot.command()
async def say(ctx, msg):
    if ctx.author.id == 650343691998855188:
        await ctx.send(msg)
    else:
        await ctx.send("Nie masz wystarczających uprawnień :<", delete_after = 2)

@bot.command()
async def clear(ctx, x):
    await ctx.channel.purge(limit=int(x))
    await ctx.send(f'Pomyślnie usunięto {x} wiadomości!', delete_after = 2)

@bot.command()
async def clock(ctx):
    msg = discord.Embed(title="Zegar", color=0xFFFFFF)
    msg.set_author(name= ctx.author.name, icon_url= str(ctx.author.display_avatar))
    msg.set_thumbnail(url="https://mc.polishwrona.pl/clock.png")
    msg.add_field(name=time.strftime("%H:%M"), value="-------", inline=False)
    await ctx.respond(embed=msg)

@bot.command()
async def logout(ctx):
    if ctx.author.id == 650343691998855188:
        await ctx.send(f"bye... {ctx.author.mention}, you ended me :<")
        await ctx.respond(f"Status : disconnecting")
        await ctx.send(f"Bot ping : {round(bot.latency  * 1000)} ms")
        print("\n\n\n\nDISCONNECTING\n\n\n\n")
        await discord.Client.close(bot)
    else:
        ctx.respond("You don't have the permission to do that", delet_after=1)

bot.run(token)