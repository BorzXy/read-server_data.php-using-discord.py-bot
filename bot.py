#reader discord.py made by ImDanilo & BorzXy
#Inspired by ClayneID (https://github.com/ClayneID)
import discord
from discord.ext import commands
import requests

daniloboi = commands.Bot(command_prefix=">")

@daniloboi.event
async def on_ready():
	print('Bot Made by ImDanilo & BorzXy')
	print(f"-----\nLogged in as: {daniloboi.user.name} : {daniloboi.user.id}\n-----")
	print("Error Logs:")
	activity = discord.Game(name="Playing Reader By ImDanilo#9999 & BorzXy#0001", type=3)
	await daniloboi.change_presence(activity=discord.Game(name="bot made by BorzXy#0001 & ImDanilo#9999"))

@daniloboi.command()
async def test(ctx):
	await ctx.send('Bot Already Online Type >read <IP> to read someone server server_data.php')

@daniloboi.command()
async def reader(ctx, message):
    await ctx.message.delete()
    await ctx.send('Please Wait...')
    reader = requests.post(f'http://{message}/growtopia/server_data.php')
    print(reader)
    await ctx.send(f'```css\n{reader.text}\n```')
#Update 1
@daniloboi.command()
async def read(ctx, message):
    await ctx.message.delete()
    await ctx.send('Please Wait...')
    reader = requests.post(f'http://{message}/growtopia/server_data.php')
    print(reader)
    read = discord.Embed(title=f"{message} Result:", colour=000000, timestamp=ctx.message.created_at)
    read.add_field(name=f"Result:", value= f'```\n{reader.text}\n```')
    await ctx.send(embed=read)
#Update 2 embed

daniloboi.run('Your bot token')
