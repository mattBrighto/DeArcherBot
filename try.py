import discord
from discord.ext import commands

bot = discord.Bot()

txt = open('token.txt', "r")
token = txt.read()
txt.close()

@bot.message_command()
async def Mention(ctx, message):
    await ctx.respond(message.author.mention)

@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")

@bot.user_command(name="Say Hello")
async def hi(ctx, user):
    await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")

bot.run(token)