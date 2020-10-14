import discord
from discord.ext import commands


class bot_show(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.max_bot_list_length = 1950  # 出力の際の文字数制限

    @commands.command(aliases=['show', 'view'])
    async def show_bots(self, ctx):
        """ボットのデータを一覧で出力（現時点では2000文字制限未対応）"""
        if ctx.author.bot:
            return

        await self._put_bot_list_all(ctx)

    async def _put_bot_list_all(self, ctx):
        bot_list = ''
        break_msg = ''
        break_suffix = ''
        count = 0
        for name in self.bot.bots_data.values():
            if len(bot_list) > self.max_bot_list_length:
                break_msg = f'※ {self.max_bot_list_length}文字を超えたので全部は表示していません'
                break_suffix = '… …'
                break
            count += 1
            bot_list += f'{count}. {name}\n'

        if len(bot_list) <= 0:
            bot_list = '登録されているボットはありません'

        embed = discord.Embed(
            title=f'{len(self.bot.bots_data)}件の登録がありました',
            description=f'{bot_list}{break_suffix}',
            color=self.bot.border_color
        )
        if break_msg:
            embed.set_footer(
                text=break_msg
            )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(bot_show(bot))
