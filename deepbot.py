# インストールした discord.py を読み込む
import discord
#import requests

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'Njk5NTg1NjcyNTc4NTk2OTc0.XpWl6Q.QstVlSWVekdLUhg_fieZGuG_5Mg'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    
    if message.content == '/pic':
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(r.content)
        await

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)