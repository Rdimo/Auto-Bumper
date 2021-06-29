import asyncio, discord, random, time, json
from discord.ext import commands

bot = commands.Bot(command_prefix="*", self_bot=True) # Change prefix here

@bot.command(pass_context=True)
async def bump(ctx):
    await ctx.message.delete()
    while True:
        await ctx.send('!d bump')
        time.sleep(random.randint(7263, 7500))

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f":ping_pong: pong! {round(bot.latency * 1000)}ms")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name=f"🎉", url="https://rdimo.github.io/CheatAway/")) 
    print(f"Logged in as {bot.user} | {bot.user.id}")

bot.run('your_discord_token_here', bot=False) # Change your_discord_token_here to your actual token here