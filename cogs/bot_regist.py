import discord
from discord.ext import commands


class botRegist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['add', 'regist'])
    async def registBot(self, ctx, *, bot_name=None):
        """ボットのデータを登録する"""
        # ボット名チェック
        if not await self._check_bot_name(bot_name, ctx.message.channel):
            return

        # 登録
        self._save_bot_data(ctx.message.id, bot_name)
        result = f'『{bot_name}』を登録しました'
        await ctx.send(result)

    async def _check_bot_name(self, bot_name, ch):
        """入力名チェック（とりあえず長さのみ）"""
        max_length = self.bot.regist_rules['bot_name_max_length']
        min_length = self.bot.regist_rules['bot_name_min_length']

        error_msg = ''
        if not bot_name:
            error_msg = '登録するボットの名前が入力されていません'
        elif len(bot_name) > max_length:
            error_msg = f'{max_length + 1}文字以上の名前は登録できません'
        elif len(bot_name) <= min_length:
            error_msg = f'{min_length}文字以下の名前は登録できません'

        if error_msg:
            await self._put_error_msg(error_msg, ch)
            return False
        else:
            return True

    def _save_bot_data(self, message_id: int, bot_name):
        """登録実行"""
        self.bot.bots_data[message_id] = bot_name
        return

    async def _put_error_msg(self, result, ch):
        embed = discord.Embed(
            title='エラーが発生しました',
            description=result,
            color=0xff0000
        )
        await ch.send(embed=embed)


def setup(bot):
    bot.add_cog(botRegist(bot))
