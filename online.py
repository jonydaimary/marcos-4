import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import aiohttp		


Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="MultiVerse Official Bot", command_prefix=commands.when_mentioned_or("!!"), pm_help = True)
client.remove_command('help')



async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='!!help'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='with '+str(len(set(client.get_all_members())))+' users'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='in '+str(len(client.servers))+' servers'))
        await asyncio.sleep(5)
	
	
	
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started New here ')
    print('Created by MARCOS')
    client.loop.create_task(status_task())
	
def is_owner(ctx):
    return ctx.message.author.id == "498378677512437762" #replace_it_with_your_discord_id

def is_soyal(ctx):
    return ctx.message.author.id == "498378677512437762" 		



@client.event
async def on_message(message):
    channel = client.get_channel('519791076803084288')
    if message.server is None and message.author != client.user:
        await client.send_message(channel, '{} : <@{}> : '.format(message.author.name, message.author.id) + message.content)
    await client.process_commands(message)
	
@client.event
async def on_reaction_add(reaction, user):
  if reaction.message.server is None:
      if reaction.emoji == '😁':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='FUN COMMANDS')
        embed.add_field(name = '``!!botinvite``',value ='``!!virus @user <text>``, ``!!meme``, ``!!lovedetect user1 user2``,')
        my_msg = await client.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await client.delete_message(my_msg)
        
      if reaction.emoji == '⚙':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='MODERATION COMMANDS')
        embed.add_field(name = '``!!botinvite``',value ='``!!dm @user <text>``, ``!!muteinchannel @user <time in minutes>``, ``!!setupwelcomer``, ``!!embed <text>``, ``!!role @user <rolename>``, ``!!setnick @user <New nickname>``, ``!!serverinfo``, ``!!userinfo @user``, ``!!lock #channel or mv!lock``, ``!!unlock #channel or mv!unlock``, ``!!membercount``, ``!!say <text>``, ``!!kick @user``, ``!!mute @user <time in minutes>``, ``!!unmute @user``, ',inline = False)
        react_message = await client.send_message(user,embed=embed)
        await client.add_reaction(react_message, reaction)
        await asyncio.sleep(30)
        await client.delete_message(react_message)
    
        
        
        
      if reaction.emoji == '👥':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='GENERAL COMMANDS')
        embed.add_field(name = '``!!botinvite``',value ='``!!help``, ``!!google <anything>``, ``!!youtube <anything>``, ``!!botinvite``, ``!!ping``, ``!!serverinvite``, ``!!avatar or mv!avatar @user``, ',inline = False)
        react_message = await client.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await client.delete_message(react_message)
        
        
        
      if reaction.emoji == '⏱':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='EMOJI COMMANDS')
        embed.add_field(name = '``!!botinvite``',value ='``!!wow``',inline = False)
        react_message = await client.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await client.delete_message(react_message)
  else:
      if reaction.emoji == '🇻':
            role = discord.utils.get(user.server.roles, name='Verified')
            await client.add_roles(user, role)



@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.set_author(name='Help')
      embed.add_field(name = 'Please Join my Server and Help and Support !! Server Link:',value ='https://discord.gg/zxBfDY7',inline = False)
      embed.add_field(name = 'React with ⚙ ',value ='MODERATION COMMANDS.',inline = False)
      embed.add_field(name = 'React with 😁 ',value ='FUN COMMANDS.',inline = False)
      embed.add_field(name = 'React with 👥 ',value ='GENERAL COMMANDS',inline = False)
      embed.add_field(name = 'React with ⏱ ',value ='EMOJI COMMANDS',inline = False)
      dmmessage = await client.send_message(author,embed=embed)
      reaction1 = '⚙'
      reaction2 = '😁'
      reaction3 = '👥'
      reaction4 = '⏱'
      await client.add_reaction(dmmessage, reaction1)
      await client.add_reaction(dmmessage, reaction2)
      await client.add_reaction(dmmessage, reaction3)
      await client.add_reaction(dmmessage, reaction4)
      await client.say('I sent you the list of commands in a private message. Check your direct messages')
    
	
	
	
@client.command(pass_context = True)
async def meme(ctx):
    colour = '0x' + '008000'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()
            embed = discord.Embed(title='Random Meme',color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)		
	
	
	
	
	
	

@client.command(pass_context=True)
async def tweet(ctx, usernamename:str, *, txt:str):
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={usernamename}&text={txt}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            embed.title = "{} twitted: {}".format(usernamename, txt)
            await client.say(embed=embed)

		

		
@client.command(pass_context=True)
async def virus(ctx,user: discord.Member=None,*,hack=None):
    nome = ctx.message.author
    if not hack:
        hack = 'discord'
    else:
        hack = hack.replace(' ','_')
    channel = ctx.message.channel
    x = await client.send_message(channel, '``[▓▓▓                    ] / {}-virus.exe Packing files.``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓                ] - {}-virus.exe Packing files..``'.format(hack))
    await asyncio.sleep(0.3)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {}-virus.exe Packing files...``'.format(hack))
    await asyncio.sleep(1.2)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {}-virus.exe Initializing code.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {}-virus.exe Initializing code..``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {}-virus.exe Finishing.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {}-virus.exe Finishing..``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``Successfully downloaded {}-virus.exe``'.format(hack))
    await asyncio.sleep(2)
    x = await client.edit_message(x,'``Injecting virus.   |``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus..  /``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus... -``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus....\``')
    await client.delete_message(x)
    await client.delete_message(ctx.message)
        
    if user:
        await client.say('`{}-virus.exe` successfully injected into **{}**\'s system.'.format(hack,user.name))
        await client.send_message(user,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
    else:
        await client.say('**{}** has hacked himself ¯\_(ツ)_/¯.'.format(name.name))
        await client.send_message(name,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
	
		
		
		
@client.command(pass_context=True)
async def lovedetect(ctx, user: discord.Member = None, *, user2: discord.Member = None):
    shipuser1 = user.name
    shipuser2 = user2.name
    useravatar1 = user.avatar_url
    useravatar2s = user2.avatar_url
    self_length = len(user.name)
    first_length = round(self_length / 2)
    first_half = user.name[0:first_length]
    usr_length = len(user2.name)
    second_length = round(usr_length / 2)
    second_half = user2.name[second_length:]
    finalName = first_half + second_half
    score = random.randint(0, 100)
    filled_progbar = round(score / 100 * 10)
    counter_ = '█' * filled_progbar + '‍ ‍' * (10 - filled_progbar)
    url = f"https://nekobot.xyz/api/imagegen?type=ship&user1={useravatar1}&user2={useravatar2s}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f"{shipuser1} ❤ {shipuser2} Love each others", description=f"Love\n`{counter_}` Score:**{score}% **\nLoveName:**{finalName}**", color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            await client.say(embed=embed)	
	
	
	
@client.command(pass_context=True, aliases=['em', 'e'])
async def modmail(ctx, *, msg=None):
    channel = discord.utils.get(client.get_all_channels(), name='📬mod-mails📬')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    color = discord.Color((r << 16) + (g << 8) + b)
    if not msg:
        await client.say("Please specify a message to send")
    else:
        await client.send_message(channel, embed=discord.Embed(color=color, description=msg + '\n Message From-' + ctx.message.author.id))
        await client.delete_message(ctx.message)
    return
	
@client.command()
async def servers():
  servers = list(client.servers)
  await client.say(f"Connected on {str(len(servers))} servers:")
  await client.say('\n'.join(server.name for server in servers))

@client.command(pass_context = True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    await client.say("Ping: {}ms".format(round((t2-t1)*1000)))


@client.command(pass_context=True)
async def google(ctx, *, message):
    new_message = message.replace(" ", "+")
    url = f"https://www.google.com/search?q={new_message}"
    await client.say(url)

@client.command(pass_context=True)
async def youtube(ctx, *, message: str):
    new_message = message.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={new_message}"
    await client.say(url)


@client.command(pass_context=True)
async def skincolor(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    random.seed(user.id)
    skins = ["White", "Black", "Blue", "Green", "Rainbow", "Purple", "Brown", "Pink", "Cream", "Orange"]
    if user == ctx.message.author:
        embed2 = discord.Embed(title="You should know your own skin color", color = discord.Color((r << 16) + (g << 8) + b))
        await client.say(embed=embed2)
    else:
        embed = discord.Embed(color=0xcb287a)
        embed.add_field(name=f"{user.name}'s skin color", value=random.choice(skins))
        await client.say(embed=embed)
	
	
@client.command(pass_context=True)
async def unverify(ctx):
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Unverified')
    await client.add_roles(ctx.message.author, role)
    
@client.command(pass_context=True)
async def verify(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.delete_message(ctx.message)
      role = discord.utils.get(ctx.message.server.roles, name='Verified')
      await client.add_roles(ctx.message.author, role)	
	
 
	
@client.command(pass_context=True)
@commands.check(is_soyal)
async def botdm(ctx, user: discord.Member, *, msg: str):
    await client.send_typing(user)
    await client.send_message(user, msg)
	
@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def announce(ctx, channel: discord.Channel=None, *, msg: str):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title="Announcement", description="{}".format(msg), color = discord.Color((r << 16) + (g << 8) + b))
    await client.send_message(channel, embed=embed)
    await client.delete_message(ctx.message)


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def embed(ctx, *args):
    if ctx.message.author.bot:
      return
    else:
      argstr = " ".join(args)
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      text = argstr
      color = discord.Color((r << 16) + (g << 8) + b)
      await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
      await client.delete_message(ctx.message)    

	
	
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def dm(ctx, user: discord.Member, *, msg: str):
    try:
        await client.send_message(user, msg)
        await client.delete_message(ctx.message)          
        await client.say("Success! Your DM has made it! :white_check_mark: ")
    except discord.ext.commands.MissingPermissions:
        await client.say("Aw, come on! You thought you could get away with DM'ing people without permissions.")
    except:
        await client.say("Error :x:. Make sure your message is shaped in this way: ^dm [tag person] [msg]")

		
	
	
@client.command(pass_context = True)
async def botinvite(ctx):
    if ctx.message.author.bot:
      return
    else:
      embed=discord.Embed(title="Click on this link to invite:", description="https://discordapp.com/api/oauth2/authorize?client_id=520267296506249216&permissions=8&scope=bot" , color=0x00fd1b)
      await client.say(embed=embed)


@client.command(pass_context = True)
async def test(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.send_message(ctx.message.author, 'Hii bro what supp')
      await client.say('Check your dm ')

@client.command(pass_context=True)  
@commands.has_permissions(administrator=True)    
async def kick(ctx,user:discord.member):
    if user.server_permissions.kick_members:
      await client.say('**He is mod/admin and i am unable to kick him/her**')
      return
    else:
      await client.kick(user)
      await client.say(user.name+' was kicked. Good bye '+user.name+'!')
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == 'Soyal-log':
            embed=discord.Embed(title="User kicked!", description="**{0}** is kicked by **{1}**!".format(user, ctx.message.author), color=0xFDE112)
            await client.send_message(channel, embed=embed)


	
	

        

@client.command(pass_context = True)
async def happybirthday(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify a user to wish")
    await client.say('Happy birthday have a nice day' + msg + ' http://imgur.com/gallery/PbyNCR2')
    return



@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def emojiids(ctx):
  for emoji in ctx.message.author.server.emojis:
    print(f"<:{emoji.name}:{emoji.id}>")
    print(" ")    
			
@client.command(pass_context = True)
async def wow(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:WOW:515854429485006848>')
	
@client.command(pass_context = True)
async def dank(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:OnThaCoco:515853700682743809>')

@client.command(pass_context = True)
async def santa(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:santa:517232271678504970>')
	
@client.command(pass_context = True)
async def hi(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:hi:517232279148429313>')
	
@client.command(pass_context = True)
async def lol(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:lol:517232283670020096>')
	
@client.command(pass_context = True)
async def love(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:love:517232300912672774>')
	
@client.command(pass_context = True)
async def mad(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:mad:517232301176913951>')
	
@client.command(pass_context = True)
async def alien(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:alien:517232332663422986>')

@client.command(pass_context = True)
async def fearfromme(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:shiroeglassespush:516174320532193289>')
	   	
@client.command(pass_context = True)
async def angry(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:angear:516174316950388772>')
	
@client.command(pass_context = True)
async def surprised(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:eyebigger:516174315058626560>')
		
@client.command(pass_context = True)
async def cat(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:agooglecat:516174312294842389>')
		
@client.command(pass_context = True)
async def thinking1(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:thinking:516183328613990400>')
	







@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setuplog(ctx):
    if ctx.message.author.bot:
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, 'information-log',everyone)

	

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setupwelcome(ctx):
    if ctx.message.author.bot:
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, 'welcome_swagat',everyone)
	
	
@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == 'welcome_swagat':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check rules and never try to break any one of them', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/486489391083159574/520207004334292992/Loading.gif') 
            embed.set_image(url = member.avatar_url)
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining', value=member.joined_at)
            await client.send_message(channel, embed=embed)	
		

@client.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == 'welcome_swagat':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} just left {member.server.name}', description='Bye bye 👋! We will miss you 😢', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**Hope you will be back soon 😕.**', inline=True)
            embed.add_field(name='Your join position was', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await client.send_message(channel, embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def rolesetup(ctx):
    author = ctx.message.author
    server = ctx.message.server
    mod_perms = discord.Permissions(manage_messages=True, kick_members=True, manage_nicknames =True,mute_members=True)
    admin_perms = discord.Permissions(ADMINISTRATOR=True)

    await client.create_role(author.server, name="Owner", permissions=admin_perms)
    await client.create_role(author.server, name="Admin", permissions=admin_perms)
    await client.create_role(author.server, name="Senior Moderator", permissions=mod_perms)
    await client.create_role(author.server, name="G.O.H")
    await client.create_role(author.server, name="Moderator", permissions=mod_perms)
    await client.create_role(author.server, name="Muted")
    await client.create_role(author.server, name="Friend of Owner")


@commands.has_permissions(manage_roles=True)     
async def role(ctx, user: discord.Member, *, role: discord.Role = None):
        if role is None:
            return await client.say("You haven't specified a role! ")

        if role not in user.roles:
            await client.add_roles(user, role)
            return await client.say("{} role has been added to {}.".format(role, user))

        if role in user.roles:
            await client.remove_roles(user, role)
            return await client.say("{} role has been removed from {}.".format(role, user))
 
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str): 
    await client.send_message(userName, "You have been warned for: **{}**".format(message))
    await client.say(":warning: __**{0} Has Been Warned!**__ :warning: ** Reason:{1}** ".format(userName,message))
    pass


@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)

    if not msg: await client.say("Please specify a message to send")
    else: await client.say(msg)
    return

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def friend(ctx, user:discord.Member,):
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Friend of Owner')
    await client.add_roles(ctx.message.mentions[0], role)


@client.command(pass_context=True)
async def ownerinfo(ctx):
    embed = discord.Embed(title="Information about owner", description="Bot Name- MARCOS", color=0x00ff00)
    embed.set_footer(text="MARCOS")
    embed.set_author(name=" Bot Owner Name- MARCOS")
    embed.add_field(name="Site- coming soon...", value="Thanks for adding our bot", inline=True)
    await client.say(embed=embed)		



@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)
async def getuser(ctx, role: discord.Role = None):
    if role is None:
        await client.say('There is no "STAFF" role on this server!')
        return
    empty = True
    for member in ctx.message.server.members:
        if role in member.roles:
            await client.say("{0.name}: {0.id}".format(member))
            empty = False
    if empty:
        await client.say("Nobody has the role {}".format(role.mention))


@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member):
    if ctx.message.author.bot:
      return
    else:
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
      embed.add_field(name="Name", value=user.name, inline=True)
      embed.add_field(name="ID", value=user.id, inline=True)
      embed.add_field(name="Status", value=user.status, inline=True)
      embed.add_field(name="Highest role", value=user.top_role)
      embed.add_field(name="Joined", value=user.joined_at)
      embed.set_thumbnail(url=user.avatar_url)
      await client.say(embed=embed)




@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
@commands.cooldown(rate=5,per=86400,type=BucketType.user) 
async def access(ctx, member: discord.Member):
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='access')
      await client.add_roles(member, role)
      await client.say("Gave access to {}".format(member))
      for channel in member.server.channels:
        if channel.name == 'soyal-log':
            embed=discord.Embed(title="User Got Access!", description="**{0}** got access from **{1}**!".format(member, ctx.message.author), color=0x020202)
            await client.send_message(channel, embed=embed)
            await asyncio.sleep(45*60)
            await client.remove_roles(member, role)


@client.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member, *, nickname):
    await client.change_nickname(user, nickname)
    await client.delete_message(ctx.message)
    for channel in user.server.channels:
      if channel.name == 'soyal-log':
          embed=discord.Embed(title="Changed Nickname of User!", description="**{0}** nickname was changed by **{1}**!".format(member, ctx.message.author), color=0x0521F6)
          await client.send_message(channel, embed=embed)



@client.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await client.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await client.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await client.edit_message(react_message, embed=embed)


@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member):
    if user.server_permissions.ban_members:
      await client.say('**He is mod/admin and i am unable to ban him/her**')
      return
    else:
      await client.ban(user)
      await client.say(user.name+' was banned. Good bye '+user.name+'!')
      for channel in member.server.channels:
        if channel.name == 'information-log':
            embed=discord.Embed(title="User banned!", description="**{0}** banned by **{1}**!".format(member, ctx.message.author), color=0x38761D)
            await client.send_message(channel, embed=embed)


@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     
async def unban(ctx):
    ban_list = await client.get_bans(ctx.message.server)

    # Show banned users
    await client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
      await client.say('Ban list is empty.')
      return
    else:
      await client.unban(ctx.message.server, ban_list[-1])
      await client.say('Unbanned user: `{}`'.format(ban_list[-1].name))
      for channel in member.server.channels:
        if channel.name == 'soyal-log':
            embed=discord.Embed(title="User unbanned!", description="**{0}** unbanned by **{1}**!".format(ban_list[-1].name, ctx.message.author), color=0x38761D)
            await client.send_message(channel, embed=embed)


@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     

async def serverinfo(ctx):
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color = discord.Color((r << 16) + (g << 8) + b));
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await client.say(embed = join);


@client.command(pass_context=True)
async def apply(ctx, *, msg: str):
    channel = client.get_channel('520830825021964305')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='Application for bot', value='-------------------',inline = False) 
    embed.add_field(name='User ID:', value='{}'.format(ctx.message.author.id),inline = False)
    embed.add_field(name='User Name:', value='{}'.format(ctx.message.author.name),inline = False)
    embed.add_field(name='Server Name:', value='{}'.format(ctx.message.server.name),inline = False)
    embed.add_field(name='Bot information:', value=msg, inline=False)
    await client.send_message(channel, embed=embed) 
    await client.delete_message(ctx.message)


@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def makemod(ctx, user: discord.Member):
    nickname = '[̲̅M̲̅]' + user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    await client.add_roles(user, role)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Congratulations Message')
    embed.add_field(name = '__Congratulations__',value ='**Congratulations for mod.Hope you will be more active here. Thanks for your help and support.**',inline = False)
    embed.set_image(url = 'https://preview.ibb.co/i1izTz/ezgif_5_e20b665628.gif')
    await client.send_message(user,embed=embed)
    await client.delete_message(ctx.message)


@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def makeadmin(ctx, user: discord.Member):
    nickname = 'Ѧ'+ user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Admin')
    await client.add_roles(user, role)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Congratulations Message')
    embed.add_field(name = '__Congratulations__',value ='**Congratulations for Admin.Hope you will be more active here. Thanks for your help and support.**',inline = False)
    embed.set_image(url = 'https://preview.ibb.co/i1izTz/ezgif_5_e20b665628.gif')
    await client.send_message(user,embed=embed)
    await client.delete_message(ctx.message)


@client.command(pass_context = True)
async def sorry(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please Sorry")
    await client.say('Sorry ' + msg + ' http://imgur.com/gallery/Dif2lYI')
    return


@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  
async def clear(ctx, number):
 
    if ctx.message.author.server_permissions.manage_messages:
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)            
       
    try:
        await client.delete_messages(mgs)          
        await client.say(str(number)+' messages deleted')
     
    except discord.Forbidden:
        await client.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await client.say('clear failed.')
        return         
   
 
    await client.delete_messages(mgs)      

 
@client.event
async def on_message_delete(message):
    if not message.author.bot:
      channelname = 'information-log'
      logchannel=None
      for channel in message.server.channels:
        if channel.name == channelname:
          user = message.author
      for channel in user.server.channels:
        if channel.name == 'soyal-log':
          logchannel = channel
          r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
          embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
          embed.set_author(name='Message deleted')
          embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
          embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
          embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
          await client.send_message(logchannel,  embed=embed)	
		
@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(ctx.message.author.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/520159870448566287/520829749095038977/pubg.png') 
        embed.set_image(url = ctx.message.author.avatar_url)
        await client.say(embed=embed)
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/520159870448566287/520829749095038977/pubg.png') 
        embed.set_image(url = user.avatar_url)
        await client.say(embed=embed)



@client.command(pass_context=True, aliases=['server'])
@commands.has_permissions(kick_members=True)
async def membercount(ctx, *args):
    """
    Shows stats and information about current guild.
    ATTENTION: Please only use this on your own guilds or with explicit
    permissions of the guilds administrators!
    """
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em = Embed(title="Membercount")
    em.description =    "```\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await client.send_message(ctx.message.channel, embed=em)
    await client.delete_message(ctx.message)
	
	
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def channelsetup(ctx):
    author = ctx.message.author
    server = ctx.message.server
    mod_perms = discord.Permissions(manage_messages=True, kick_members=True, manage_nicknames =True,mute_members=True)
    admin_perms = discord.Permissions(ADMINISTRATOR=True)

    await client.create_role(author.server, name="Owner", permissions=admin_perms)
    await client.create_role(author.server, name="Admin", permissions=admin_perms)
    await client.create_role(author.server, name="Moderator", permissions=mod_perms)
    await client.create_role(author.server, name="Muted")
    
    await client.create_role(author.server, name="Friend of Owner")
    await client.create_role(author.server, name="Verified")
    everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
    everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
    user_perms = discord.PermissionOverwrite(read_messages=True)
    user = discord.ChannelPermissions(target=server.default_role, overwrite=user_perms)
    private_perms = discord.PermissionOverwrite(read_messages=False)
    private = discord.ChannelPermissions(target=server.default_role, overwrite=private_perms)    
    await client.create_channel(server, 'welcome_suagat',everyone)
    await client.create_channel(server, 'left_mat-ja-yar',everyone)
    await client.create_channel(server, 'announcement',everyone)
    await client.create_channel(server, 'give_away',everyone)
    await client.create_channel(server, 'self_assignable_roles',everyone)
    await client.create_channel(server, 'g_e_n_e_r_a_l',user)
    await client.create_channel(server, 'screenshot_image',user)
    await client.create_channel(server, 'promote_links',user)
    await client.create_channel(server, 'dark_memers',user)
    await client.create_channel(server, 'aki__play',user)
    await client.create_channel(server, 'spam_here',user)
    await client.create_channel(server, 'bot_commands',user)
    await client.create_channel(server, 'private_chat',private)
    await client.create_channel(server, 'General', type=discord.ChannelType.voice)
    await client.create_channel(server, 'music_commands',user)
    await client.create_channel(server, 'music', type=discord.ChannelType.voice)
    await client.create_channel(server, 'pokémon_catching',user)
    await client.create_channel(server, 'pokémon_dueling',user)
    await client.create_channel(server, 'pokémon_commands',user)
    await client.create_channel(server, 'A_F_K', type=discord.ChannelType.voice)




client.run(os.getenv('Token')) 
