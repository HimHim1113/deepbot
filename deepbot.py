# インストールした discord.py を読み込む
from discord.ext import commands

import os
import traceback


# 読み込むコグの名前
INITIAL_EXTENSIONS = [
    'cogs.cat',
    'cogs.greet',
    'cogs.omikuji',
    'cogs.sample'
]

class DeepBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)
        
        # INITIAL_COGSに格納されている名前から、コグを読み込む。
        # エラーが発生した場合は、エラー内容を表示。
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()
	
    # 起動時に動作する処理
    async def on_ready(self):
        # 起動したらターミナルにログイン通知が表示される
        print('ログインしました')


# DeepBotのインスタンス化及び起動処理
if __name__ == '__main__':
    TOKEN = os.environ.get('DISCORD_TOKEN') # 環境変数からトークンを読み込む
    bot = DeepBot(command_prefix='%')
    bot.run(TOKEN)
