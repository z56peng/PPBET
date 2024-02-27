import discord
from discord.ext import commands
import db
import os

token=os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    db.initialize_db()  # 初始化数据库

@bot.command()
async def sync(ctx):
    await bot.tree.sync()
    await ctx.send('CMD updated.')

@bot.hybrid_command()
async def balance(ctx):
    user_id = ctx.author.id
    user_balance = db.get_balance(user_id)
    await ctx.send(f'Your balance is {user_balance} PP coins.')

@bot.hybrid_command()
async def add(ctx, fund: int):
    user_id = ctx.author.id
    user_balance = db.get_balance(user_id)
    db.update_balance(ctx.author.id, user_balance + fund)
    await ctx.send(f'Balance added.')

@bot.hybrid_command()
async def bet(ctx, amount: int):
    # 这里需要添加赌注逻辑
    pass

# 运行机器人

bot.run(token)
