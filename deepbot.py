# インストールした discord.py を読み込む
from discord.ext import commands

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'Njk5NTg1NjcyNTc4NTk2OTc0.XpWl6Q.QstVlSWVekdLUhg_fieZGuG_5Mg'
prefix='/'

class DeepBot(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
	
    # 起動時に動作する処理
    #@client.event
    #async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
        #print('ログインしました')

    @commands.command()
    async def neko(self, ctx):
        '''にゃーん'''
        await ctx.send(f'にゃーん')

    @commands.command()
    async def hello(self, ctx):
        '''出会いのあいさつをする'''
        await ctx.send(f'どうも、{ctx.author.name}さん!')

    @commands.command()
    async def goodbye(self, ctx):
        '''別れの挨拶をする'''
        await ctx.send(f'じゃあね、{ctx.author.name}さん!')

bot = commands.Bot(command_prefix=prefix)
bot.add_cog(DeepBot(bot=bot))
bot.run(TOKEN)
