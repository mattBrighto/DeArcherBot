import discord
from discord.ext import commands

bot = discord.Bot()

txt = open('Z:/token.txt', "r")
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

@bot.command()
async def logout(ctx):
    if ctx.author.is_owner():
        await ctx.send(f"bye... {ctx.author}, you ended me :<")
        await ctx.send(f"Status : {discord.Client.status}")
        await ctx.send(f"Bot ping : {bot.latency}")
        print("\n\n\n\nDISCONNECTING\n\n\n\n")
        await discord.Client.close(bot)
    else:
        ctx.send("You don't have the permission to do that", delet_after=1)

bot.run(token)