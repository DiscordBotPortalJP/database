import discord
from discord.ext import commands


class BotRegister(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['add', 'regist'])
    async def register_bot(self, ctx, *, bot_name=None):
        """ボットのデータを登録する"""
        # ボット名チェック
        if error_msg := self._validate_bot_name(bot_name):
            await self._put_error_msg(error_msg, ctx.channel)
            return

        # 登録
        self._save_bot_data(ctx.message.id, bot_name)
        result = f'『{bot_name}』を登録しました'
        await ctx.send(result)

    def _validate_bot_name(self, bot_name):
        """入力名チェック（とりあえず長さのみ）"""
        max_length = self.bot.rules['bot_name_max_length']
        min_length = self.bot.rules['bot_name_min_length']

        error_msg = ''
        if not bot_name:
            error_msg = '登録するボットの名前が入力されていません'
        elif len(bot_name) > max_length:
            error_msg = f'{max_length + 1}文字以上の名前は登録できません'
        elif len(bot_name) <= min_length:
            error_msg = f'{min_length}文字以下の名前は登録できません'

        return error_msg

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
    bot.add_cog(BotRegister(bot))
