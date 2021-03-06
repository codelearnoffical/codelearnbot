import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
import time
import json
import requests
import inspect
import aiohttp

bot = commands.Bot(command_prefix='>')
bot.remove_command('help')
async def loop():
    while True:
        await bot.change_presence(game=discord.Game(name=">help", type=2))
        await asyncio.sleep(15)
        await bot.change_presence(game=discord.Game(name="some dope people", type=2))
        await asyncio.sleep(15)

@bot.event
async def on_ready():
    print ("Bot has Booted!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="mmgamerbot.com", url="https://twitch.tv/MMgamerBOT", type=1))
    await loop()


@bot.command(pass_context=True)
async def remove_cmd(ctx, cmd):
    if ctx.message.author.id != '397745647723216898':
        return await bot.say("No perms from developers")
    bot.remove_command(cmd)


@bot.command(pass_context=True)
async def ftn(ctx, player, platform = None):
    if platform == None:
        platform = "pc"
    headers = {'TRN-Api-Key': '5d24cc04-926b-4922-b864-8fd68acf482e'}
    r = requests.get('https://api.fortnitetracker.com/v1/profile/{}/{}'.format(platform, player), headers=headers)
    stats = json.loads(r.text)
    stats = stats["stats"]

    #Solos
    Solo = stats["p2"]
    KDSolo = Solo["kd"]
    KDSolovalue = KDSolo["value"]
    TRNSoloRanking = Solo["trnRating"]
    winsDataSolo = Solo["top1"]
    Soloscore = Solo["score"]
    SoloKills = Solo["kills"]
    SoloMatches = Solo["matches"]
    SoloKPG = Solo["kpg"]
    SoloTop5 = Solo["top5"]
    SoloTop25 = Solo["top25"]

    embed = discord.Embed(colour=0x66009D)
    embed.set_author(icon_url="https://i.ebayimg.com/images/g/6ekAAOSw3WxaO8mr/s-l300.jpg", name="Solo stats:")
    embed.add_field(name="K/D", value=KDSolovalue)
    embed.add_field(name="Score", value=Soloscore["value"])
    embed.add_field(name="Wins", value=winsDataSolo["value"])
    embed.add_field(name="TRN Rating", value=TRNSoloRanking["value"])
    embed.add_field(name="Kills", value=SoloKills["value"], inline=True)
    embed.add_field(name="Matches Played:", value=SoloMatches["value"], inline=True)
    embed.add_field(name="Kills Per Game:", value=SoloKPG["value"], inline=True)
    embed.add_field(name="Top 5:", value=SoloTop5["value"])
    embed.add_field(name="Top 25:", value=SoloTop25["value"])

    #Duos
    Duo = stats["p10"]
    KDDuo = Duo["kd"]
    KDDuovalue = KDDuo["value"]
    TRNDuoRanking = Duo["trnRating"]
    winsDataDuo = Duo["top1"]
    Duoscore = Duo["score"]
    DuoKills = Duo["kills"]
    DuoMatches = Duo["matches"]
    DuoKPG = Duo["kpg"]
    DuoTop5 = Duo["top5"]
    DuoTop25 = Duo["top25"]

    duo = discord.Embed(color=0x008000)
    duo.set_author(icon_url="https://i.ebayimg.com/images/g/6ekAAOSw3WxaO8mr/s-l300.jpg", name="Duo stats:")
    duo.add_field(name="K/D", value=KDDuovalue)
    duo.add_field(name="Score", value=Duoscore["value"])
    duo.add_field(name="Wins", value=winsDataDuo["value"])
    duo.add_field(name="TRN Rating", value=TRNDuoRanking["value"])
    duo.add_field(name="Kills", value=DuoKills["value"], inline=True)
    duo.add_field(name="Matches Played:", value=DuoMatches["value"], inline=True)
    duo.add_field(name="Kills Per Game:", value=DuoKPG["value"], inline=True)
    duo.add_field(name="Top 5:", value=DuoTop5["value"])
    duo.add_field(name="Top 25:", value=DuoTop25["value"])

    Squad = stats["p9"]
    KDSquad = Squad["kd"]
    KDSquadvalue = KDSquad["value"]
    TRNSquadRanking = Squad["trnRating"]
    winsDataSquad = Squad["top1"]
    Squadscore = Squad["score"]
    SquadKills = Squad["kills"]
    SquadMatches = Squad["matches"]
    SquadKPG = Squad["kpg"]
    SquadTop5 = Squad["top5"]
    SquadTop25 = Squad["top25"]

    squad = discord.Embed(color=0x008000)
    squad.set_author(icon_url="https://i.ebayimg.com/images/g/6ekAAOSw3WxaO8mr/s-l300.jpg", name="Squad stats:")
    squad.add_field(name="K/D", value=KDSquadvalue)
    squad.add_field(name="Score", value=Squadscore["value"])
    squad.add_field(name="Wins", value=winsDataSquad["value"])
    squad.add_field(name="TRN Rating", value=TRNSquadRanking["value"])
    squad.add_field(name="Kills", value=SquadKills["value"], inline=True)
    squad.add_field(name="Matches Played:", value=SquadMatches["value"], inline=True)
    squad.add_field(name="Kills Per Game:", value=SquadKPG["value"], inline=True)
    squad.add_field(name="Top 5:", value=SquadTop5["value"])
    squad.add_field(name="Top 25:", value=SquadTop25["value"])

    await bot.say(embed=embed)
    await bot.say(embed=duo)
    await bot.say(embed=squad)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(ctx, discord.ext.commands.errors.CommandNotFound):
        embed = discord.Embed(title="Error:",
                              description="Damm it! I cant find that! Try `!help`.",
                              colour=0xe73c24)
        await bot.send_message(error.message.channel, embed=embed)
    else:
        embed = discord.Embed(title="Error:",
                              description=f"{ctx}",
                              colour=0xe73c24)
        await bot.send_message(error.message.channel, embed=embed)
        raise(ctx)


@bot.command(pass_context=True)
async def cat(ctx):
    embed=discord.Embed(title="Cat", color=0x008000)
    embed.set_image(url="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
    embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom bot for <code/learn>!")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def dog(ctx):
    embed=discord.Embed(title="A dog as requested:", color=0x008000)
    embed.set_image(url="https://media.giphy.com/media/Bc3SkXz1M9mjS/giphy.gif")
    embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom bot for <code/learn>!")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def slap(ctx):
    embed=discord.Embed(title="Slap Slap Slap", color=0x008000)
    embed.set_image(url="https://media.giphy.com/media/s5zXKfeXaa6ZO/giphy.gif")
    embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom bot for <code/learn>!")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def add(ctx, a: int, b: int):
    await bot.say(a+b)


@bot.command(pass_context=True)
async def multiply(ctx, a: int, b: int):
    await bot.say(a*b)

@bot.command(pass_context=True)
async def pfp(ctx, member: discord.Member):
     embed=discord.Embed(title="The users profile picture", color=0x008000)
     embed.set_image(url=member.avatar_url)
     embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom bot for <code/learn>!")
     await bot.say(embed=embed)

@bot.command(pass_context=True, name="StatChange", aliases=['cp'])
async def cp(ctx, pt: int, *, name):
    """
    Changes the bot status (Admin-Only)
    """
    if ctx.message.author.server_permissions.administrator:
        await client.change_presence(game=discord.Game(name=name, type=pt))
        embed = discord.Embed(title='Status changed!', description='The bot status was changed!', colour=mc)
        await bot.say(embed=embed)
    else:
        embed=discord.Embed(title='No perms', description='You dont have perms to change the bot status', color=mc)
        await bot.say(embed=embed)



@bot.command(pass_context=True)
async def help(ctx):
        embed=discord.Embed(title="All Help", description="""
        Info Commands:
        •`>ftn pc <player>` - Gets fortnite players status (pc only).
        •`>info <@mention>` - Gets some info on the server.
        •`>all_servers` - Shows all servers the bot is in.
        •`>urban <querey>` -Searches the urbandic for your query
        •`>pfp <@user>` - Shows a users's profile picture
        •`>all_servers` - Shows all servers the bot is in.
        Fun commands:
         •`>cat` - Gets you a select cat GIF.
         •`>dog` - Gets you a cool dog GIF.
         •`>slap` - Slapy Slpay Scratchy Bitey.
         •`>add` - Adds two numbers.
         •`>multipy` - Multipys two numbers.
        Moderation Commands:
        •`>warn <user> <reason>` - Warns a user (Also DM's)
        •`>kick <@user>` - Kicks the user from the server
        •`>ban <@user>` - Bans a user for the server
        •`>mute <@user>` - Mutes a user
        •`>leave` - Makes the bot leave the server
        Misc Commands:
        •`>ami <@role>|<rolename>` - Tells you if you have that specific role in the server
        •`>github` - Gets you codelearns github repo
        """, color=0x008000)
        embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom bot for <code/learn>!")
        await bot.whisper(embed=embed)
        await bot.say("Check your DMs")

@bot.command(pass_context=True)
async def urban(ctx, *, message):
        r = requests.get("http://api.urbandictionary.com/v0/define?term={}".format(' '.join(message)))
        r = json.loads(r.text)
        file = open('urban.txt', 'w')
        file.write("**Definition for {}** \n\n\n {}{}".format(r['list'][0]['word'],r['list'][0]['definition'],r['list'][0]['permalink']))
        file.close()
        tmp = open('urban.txt', 'rb')
        await bot.send_file(ctx.message.channel, 'urban.txt', content=tmp)

@bot.command(pass_context=True)
async def github(ctx):
    embed=discord.Embed(title="GitHub Repo",description="Our github repo: https://github.com/codelearnoffical", color=0x008000)
    embed.set_author(icon_url="https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png",name="MMgamer")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(colour=0x008000)
    embed.set_image(url=random.choice([ "https://max-media.imgix.net/transfers/2016/6/2/35493eb9ea00b43d76f504388a7d98eac01d9471.jpg?w=640&fit=max&auto=format&q=70", "https://max-media.imgix.net/transfers/2016/6/2/7b4575d386865d39cf75d5446516fa638828622e.png?w=640&fit=max&auto=format&q=70", "https://max-media.imgix.net/transfers/2016/6/2/34df8440609218f69c7466a1f19ab5aef6120596.png?w=640&fit=max&auto=format&q=70", "https://max-media.imgix.net/transfers/2016/6/2/7d41985b2e8962398df13d1272a6c258470ed53d.jpg?w=640&fit=max&auto=format&q=70", "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi0k8_b0NPbAhWDaVAKHWdJAOkQjRx6BAgBEAU&url=https%3A%2F%2Fwww.memecenter.com%2Fsearch%2Fcheese&psig=AOvVaw3u9-NYrnxSlBDWcRFEoGYG&ust=1529081497518231"]))
    embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom Bot For The Coding Lounge")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def mute(ctx, member: discord.Member, time: int, *, reason):
    if ctx.message.author.server_permissions.administrator != True:
        return await bot.say("No perms!")
    await bot.send_message(member, f"You have been muted for {time} Seconds in {ctx.message.server.name}! Be sure to read the rules again! ")
    role = discord.utils.get(ctx.message.server.roles, name="Muted")
    await bot.add_roles(member, role)
    embed = discord.Embed(title="MUTED", description="{} You have been Muted for **{}** Seconds. Reason: {}".format(member.mention, time, reason), color=0x008000)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)
    await asyncio.sleep(time)
    await bot.remove_roles(member, role)
    await bot.send_message(member, f"You have been unmuted! Be careful!")
    embed = discord.Embed(title="Member unmuted", description="{} Has been UnMuted".format(member.mention), color=0x008000)
    embed.set_author(name=member.name, icon_url=member.avatar_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def ami(ctx,*, role):
    if role in [role.name for role in ctx.message.author.roles]:
        await bot.say("Yes")
    else:
        await bot.say("No")

@bot.command(pass_context=True)
async def all_servers(ctx):
    if ctx.message.author.server_permissions.administrator:
        embed = discord.Embed(title="All servers", description="lists all servers the bot is in.", color=0x008000)
        tmp = 1
        for i in bot.servers:
            embed.add_field(name=str(tmp), value=i.name, inline=False)
            tmp += 1
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def source(ctx, *, text: str):
    nl2 = '`'
    nl = f"``{nl2}"
    source_thing = inspect.getsource(bot.get_command(text).callback)
    await bot.say(f"{nl}py\n{source_thing}{nl}")

@bot.command(pass_context=True)
async def ping(ctx):
        t1 = time.perf_counter()
        tmp = await bot.say("pinging...")
        t2 = time.perf_counter()
        await bot.say("Ping: {}ms".format(round((t2-t1)*1000)))
        await bot.delete_message(tmp)
@bot.command(pass_context = True)
async def ban(ctx, member: discord.Member):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '397745647723216898':
        try:
            await bot.ban(member)
            await bot.say(":thumbsup: Succesfully issued a ban!")
        except discord.errors.Forbidden:
            await bot.say(":x: No perms!")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member=None):
    if user is None:
        embed = discord.Embed(color=0x008000)
        embed.set_author(name=ctx.message.author.display_name)
        embed.add_field(name=":desktop:ID:", value=ctx.message.author.id, inline=True)
        embed.add_field(name=":satellite:Status:", value=ctx.message.author.status, inline=True)
        embed.add_field(name=":star2:Joined server::", value=ctx.message.author.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":date:Created account:", value=ctx.message.author.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":bust_in_silhouette:Nickname:", value=user.display_name)
        embed.add_field(name=":robot:Is Bot:", value=user.bot)
        embed.add_field(name=':ballot_box_with_check: Top role:', value=ctx.message.author.top_role.name, inline=True)
        embed.add_field(name=':video_game: Playing:', value=ctx.message.author.game, inline=True)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await asyncio.sleep(0.3)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(color=0x008000)
        embed.set_author(name=ctx.message.author.display_name)
        embed.add_field(name=":desktop:ID:", value=ctx.message.author.id, inline=True)
        embed.add_field(name=":satellite:Status:", value=ctx.message.author.status, inline=True)
        embed.add_field(name=":star2:Joined server::", value=ctx.message.author.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":date:Created account:", value=ctx.message.author.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":bust_in_silhouette:Nickname:", value=user.display_name)
        embed.add_field(name=":robot:Is Bot:", value=user.bot)
        embed.add_field(name=':ballot_box_with_check: Top role:', value=ctx.message.author.top_role.name, inline=True)
        embed.add_field(name=':video_game: Playing:', value=ctx.message.author.game, inline=True)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await asyncio.sleep(0.3)
        await bot.say(embed=embed)


@bot.command(pass_context=True)
async def checkuser(ctx, user: discord.Member=None):
    if user is None:
        embed = discord.Embed(color=0x008000)
        embed.set_author(name=ctx.message.author.name ,icon_url=ctx.message.author.avatar_url)
        embed.add_field(name=":star2:Joined server:", value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":date:Created account:", value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        await bot.say (embed=embed)
    else:
        embed = discord.Embed(color=0x008000)
        embed.set_author(name=ctx.message.author.name , icon_url=ctx.message.author.avatar_url)
        embed.add_field(name=":star2:Joined server:", value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":date:Created account:", value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        await bot.say (embed=embed)

@bot.command(pass_context=True)
async def warn(ctx, userName: discord.Member ,*, reason: str):
    if "Staff" in [role.name for role in ctx.message.author.roles] or ctx.message.author.server_permissions.administrator:
        embed = discord.Embed(title="Warned", description="{} You have been warned for **{}**".format(userName.mention, reason), color=0x008000)
        embed.set_thumbnail(url=userName.avatar_url)
        embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await bot.send_message(bot.get_channel("461818016909492224"), embed=embed)
        await bot.say(embed=embed)
        await bot.send_message(userName, "You Have Been Warned. Reason: {}".format(reason))
    else:
        await bot.say("{} :x: You are not allowed to use this command!".format(ctx.message.author.mention))
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def delete(ctx, number):
    msgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        msgs.append(x)
    await bot.delete_messages(msgs)
    embed = discord.Embed(title=f"{number} messages deleted", description="Wow, somebody's been spamming", color=0x008000)
    test = await bot.say(embed=embed)
    await asyncio.sleep(10)
    await bot.delete_message(test)

@bot.command(pass_context = True)
async def kick(ctx, member: discord.Member):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '397745647723216898':
        try:
            await bot.kick(member)
            await bot.say("Kicked that BAD coder!")
        except discord.errors.Forbidden:
            await bot.say(":x: No perms!")
    else:
        await bot.say("You dont have perms")

@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="test", description="my name jeff", color=0x008000)
    embed.set_footer(text="this is a footer")
    embed.set_author(name="MMgamer")
    embed.add_field(name="This is a field", value="no it isn't", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def get_inv(ctx):
    for i in bot.servers:
        var = await bot.create_invite(i.channels[0])
        await bot.say(str(var))


@bot.command(pass_context=True)
async def server(ctx):
    embed = discord.Embed(description="Here's what I could find:", color=0x008000)
    embed.add_field(name="Name", value=ctx.message.server.name)
    embed.add_field(name="Owner", value=ctx.message.server.owner)
    embed.add_field(name="Region", value=ctx.message.server.region)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles))
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.add_field(name="Channels", value=len(ctx.message.server.channels))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def gif(ctx):
    embed=discord.Embed(title="Random GIF:", color=0x008000)
    embed.set_image(url=random.choice(["https://media1.giphy.com/media/kHzsbx2ZCRfkIS5BLo/200w.gif", "https://media2.giphy.com/media/1jkYrQtUrRoI2Y9Yoa/200w.gif", "https://media0.giphy.com/media/vN3fMMSAmVwoo/200w.gif", "https://media0.giphy.com/media/WyrdDeIxGOlQA/200w.gif", "https://media2.giphy.com/media/QHE5gWI0QjqF2/giphy.gif", "https://media2.giphy.com/media/5ntdy5Ban1dIY/200w.gif"]))
    embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom bot for <code/learn>")
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def bird(ctx):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://random.birb.pw/tweet/') as resp:
                _url = (await resp.read()).decode("utf-8")
                url = f"http://random.birb.pw/img/{str(_url)}"
                embed = discord.Embed(color=0x008000)
                embed.description = "**Random bird image :bird:**"
                embed.set_image(url=url)
                embed.set_footer(text=f"{self.bot.user.name}")
                embed.timestamp = datetime.utcnow()
                await bot.say(embed=embed)
    except Exception as e:
        await bot.say(':negative_squared_cross_mark: **API is unavailable now. Try again later!**' + e)


@bot.command(pass_context=True)
async def ball(ctx, question):
    await bot.say(random.choice(["NO", "Ofc", "Magic dosen't have all the awnsers", "No Idea"]))

@bot.command(pass_context=True)
async def leave(ctx):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '397745647723216898':
        if ctx.message.author != bot.user:
            await bot.leave_server(ctx.message.server)
        else:
            await bot.say(":x: No Perms")
    else:
        await bot.say("To low perms")

@bot.command(pass_context=True)
async def remove_all_servers(ctx):
    if ctx.message.author.id == '279714095480176642':
        tmp = bot.servers
        for server in tmp:
            await bot.leave_server(server)
        await bot.say("Operation completed")
@bot.command(pass_context=True)
async def say(ctx, *, message):
    if ctx.message.author.id == bot.user.id:
        return
    else:
        await bot.say(message)

@bot.command(pass_context=True)
async def reboot(ctx):
    if not (ctx.message.author.id == '279714095480176642' or ctx.message.author.id == '449641568182206476'):
        return await bot.say(":x: You **Must** Be Bot Owner Or Developer")
    await bot.logout()
@bot.event
async def on_message(message):
    await bot.process_commands(message)
@bot.event
async def on_member_join(member: discord.Member):
    await bot.say("Welcome {} whenver you are ready to start learning use <#461503129146359810>".format(member.name))






bot.run(os.getenv('TOKEN'))
