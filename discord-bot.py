import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000 
    await ctx.send(f'Pong! Latency is {latency:.2f}ms')


@bot.command()
async def members(ctx):
    total_members = ctx.guild.member_count
    await ctx.send(f'Total members in the server: {total_members}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, How Can I Help You?")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
        
    if f'<@!{bot.user.id}>' in message.content or f'<@{bot.user.id}>' in message.content:
        await message.channel.send("Hello")

    await bot.process_commands(message)

bot.run('YOUR_BOT_TOKEN_HERE')
