import discord
import youtube_dl
from discord.ext import commands, tasks

client = commands.Bot(command_prefix='*')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('สวัสดีผมแอดสิน'))
    print('We have logged in as {0.user}'.format(client))
    print('Sinxao bot is ready')
    print('This bot made by zunzu#9145')

@client.event
async def on_member_join(member):
    print(f'{member} ได้ทำการเชื่อมต่อเข้ามาในเซิฟเวอร์')

@client.event
async def on_member_remove(member):
    print(f'ไอ้โง่ {member} ได้ทำการออกจากเซิฟเวอร์')

@client.command()
async def ping(ctx):
    await ctx.send(f'ปิงตอนนี้อยู่ที่ {round(client.latency * 1000)}ms')

@client.command()
@commands.has_role('Kawaii')
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} ได้ถูกเตะออกจากเซิฟเวอร์')

@client.command()
@commands.has_role('Kawaii')
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} ได้ถูกแบนออกจากเซิฟเวอร์')

@client.command()
async def kuy(ctx,member):
    await ctx.send(f'ควยไรไอ้สัส {member}')

@client.command()
async def aomsin(ctx):
    await ctx.send(f'สินหล่อเท่')

@client.event
async def on_message(message):
    if message.content == "*helps":
        embed = discord.Embed(title="Command ของบอท", description="สามารถใช้ command ทั้งหมดนี้ได้")
        embed.add_field(name="*helps", value="command ช่วยเหลือ")
        embed.add_field(name="*kick", value="เตะคนที่อยู่ในเซิฟเวอร์นี้")
        embed.add_field(name="*ban", value="แบนคนที่อยู่ในเซิฟเวอร์นี้")
        await message.channel.send(content=None, embed=embed)

client.login(process.env.BOT_TOKEN)
