# Help for the user
![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)

## **How to run**

#### **Download Content**
- Download both files from the latest release
- Dowload Python 3.7.8
- Download an IDE of your choice, would recommend VsCode
- Enter 'pip install discord.py' into the command line
```ruby
pip install discord
```

#### **Setting up discord bot**
- Go over to the discord developer portal
- Create a bot
- Get the token for the bot 
- Invite it to the discord server
- Step by step from this yt video
https://www.youtube.com/watch?v=b61kcgfOm_4

#### **Finalising code**
- Paste your bot token within the '' of the client.run('add your token here') line
```ruby
#enter within brackets, keep qoutes
client.run('add your token here')
```
- Copy the correct path by right clicking the file and clicking 'copy path' for the flooded.txt file 
```ruby
#Line the needs to be replaced, keep qoutes and the r
await ctx.send(file=discord.File(r'enter you file path here'))
#example 
await ctx.send(file=discord.File(r'C\flooded.txt'))
```
- Then run the file in your IDE     


# **Discord commands**
- .octo to flood by creating new channels
- .delete to delete all channels in the server (probably should be first)


# **Errors**
- Make sure you have Python 3.7.8 installed
- Make sure discord.py is installed (Google how to install python packets)
- If all of the above have been tested download the oldest release, which will work 100% of the time
