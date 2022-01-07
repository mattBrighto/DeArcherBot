import discord, time, datetime
from discord.ext import commands
runStarted = time.perf_counter()
bot = commands.Bot(command_prefix='/')
client = discord.Client()
meMention = '<@650343691998855188>'
file = open('token.txt', "r")
token = file.read()
file.close()

@client.event
async def on_ready():
    print("The prefix is /")
    print('Bot is currently: Online')

@bot.slash_command()
async def ping(ctx):
    await ctx.send(ctx.author.mention + ', Jestem online! PONG 🏓')

@bot.slash_command()  
async def info(ctx):
    msg = discord.Embed(color=0x9C1ABC)
    msg.remove_author()
    msg.add_field(name='Basic Info', value=f'Hej jestem {meMention}. Zrobiłem tego bota For Fun, ale jeśli chciałbyś, abym wykonał jakiś projekt informatyczny/programistyczny skorzystaj z komendy /contact (oczywiście z odpowiednim prefixem) żeby się ze mną skontaktować')
    secs = abs(runStarted - time.perf_counter())
    runtiming = time.strftime("%H:%M:%S", time.gmtime(secs))
    msg.add_field(name='Info Bota', value=f'``runtime:``   {runtiming}')
    msg.add_field(name='Linki', value='``PERSONAL SITE``   https://mc.polishwrona.pl/', inline=False)
    await ctx.send(embed=msg)

@bot.slash_command()
async def contact(ctx, msg):
    list = []
    if ctx.message.author.id in list:
        await ctx.respond("Musisz zaczekać zanim wyślesz kolejną wiadomość", delete_after = 2)
    else:
        global bot
        meUser = bot.fetch_user(65034369199885518)
        meDM = meUser.create_dm()
        await meDM.respond(f'New message from {ctx.author.mention}: '+msg)


@bot.slash_command()
async def say(ctx, msg):
    if ctx.author.id == 650343691998855188:
        await ctx.respond(msg)
    else:
        await ctx.respond("Nie masz wystarczających uprawnień :<", delete_after = 2)

@bot.slash_command()
async def clear(ctx, x):
    await ctx.channel.purge(limit=int(x))
    await ctx.respond(f'Pomyślnie usunięto {x} wiadomości!', delete_after = 2)

@bot.slash_command(name="Zegar",  description="Pokazuje godzinę")
async def clock(ctx):
    msg = discord.Embed(title="Zegar", color=0xFFFFFF)
    msg.set_author(name  = ctx.author.display_name, icon_url=ctx.author.avatar_url)
    msg.set_thumbnail(url="https://mc.polishwrona.pl/clock.png")
    msg.add_field(name=time.strftime("%H:%M"), value="-------", inline=False)
    await ctx.respond(embed=msg)

bot.run(token)