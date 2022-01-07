import discord, logging, time
from discord.ext import commands

#setting up logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


#starting counting runtime
runStarted = time.perf_counter()
#declaring bot
bot = commands.Bot(command_prefix='/')
client = discord.Client()
#additional and useful variables
userMattBrigt = '<@650343691998855188>'
#reading token
txt = open('token.txt', "r")
token = txt.read()
txt.close()

@bot.slash_command(guild_ids=[919436076081381386])
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(token)