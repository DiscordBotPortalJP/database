import os
import discord
from discord.ext import commands
from datetime import datetime, timedelta
import platform


bot = commands.Bot(
    command_prefix='d:'
)

# 登録ボットデータ key=追加された時のmessage.id value=ボット名
bot.bots_data = {}

# 登録時の制限データ
regist_rules = {}
regist_rules['bot_name_max_length'] = 50
regist_rules['bot_name_min_length'] = 3
bot.regist_rules = regist_rules

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

    bot.load_extension('cogs.bot_regist')
    bot.load_extension('cogs.bot_show')

bot.run(os.environ['DISCORD_BOT_DB_TOKEN'])
