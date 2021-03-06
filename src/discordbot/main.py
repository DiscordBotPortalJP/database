import os
import discord
from discord.ext import commands
from datetime import datetime, timedelta
import platform

allowed_mentions = discord.AllowedMentions(
    everyone=False,
    users=False,
    roles=False
)

bot = commands.Bot(
    command_prefix='d:',
    allowed_mentions=allowed_mentions
)

# 登録ボットデータ key=追加された時のmessage.id value=ボット名
bot.bots_data = {}

# 登録時の制限データ
rules = {}
rules['bot_name_max_length'] = 50
rules['bot_name_min_length'] = 3
bot.rules = rules

bot.border_color = 0x7289DA


@bot.event
async def on_ready():
    jst = datetime.utcnow() + timedelta(hours=9)
    dpy_ver = discord.__version__
    python_var = platform.python_version()
    print('--------------------------------')
    print(jst.strftime('%Y/%m/%d %H:%M:%S'))
    print(f'{bot.user.name} ({bot.user.id})')
    print(f'discord.py {dpy_ver} python {python_var}')
    print('--------------------------------')

bot.load_extension('cogs.bot_register')
bot.load_extension('cogs.bot_show')

bot.run(os.environ['DISCORD_BOT_DB_TOKEN'])
