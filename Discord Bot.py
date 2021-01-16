import asyncio
import random
import time

import discord
from discord.ext import commands

from discord import Guild, Member, User, channel
from discord.ext.commands import bot


client = discord.Client(intents=discord.Intents.all())

#########################################################################

print('Bot wird gestarted...')
time.sleep(1)
print('...')

h = True

antworten = ['Ja', 'Nein', 'Vielleicht', 'Wahrscheinlich', 'Sieht so aus', 'Sehr wahrscheinlich',
             'Sehr unwahrscheinlich', 'drei', '9999999999999999999999999999999999999999999999999']

@client.event
async def on_ready():
    print('Du bist eingeloggt als Bot mit dem Namen: {}\n.....................................................................................................................................................................................................................................................................\nHier können Sie nun alle commands nachverfolgen:'.format(client.user.name))
    client.loop.create_task(status_task())


async def status_task():

    await client.change_presence(activity=discord.Game('type .help'), status=discord.Status.online)
    await asyncio.sleep(20)
    await client.change_presence(activity=discord.Game('then you can specify'), status=discord.Status.online)
    await asyncio.sleep(2)
    guild: Guild = client.get_guild(658960248345853952)


def is_not_pinned(mess):
    return not mess.pinned


@client.event
async def on_member_join(member):
    guild: Guild = member.guild
    if not member.bot:
        embed = discord.Embed(title='Willkommen auf dem Superguay Server {} \n(va a ser superguay)'.format(member.name),
                              description='Wir heißen dich herzlich Willkommen auf unserem Server! \nBitte beachte alle Regeln und sei vernünftig', color=0x22a7f0)
        embed.set_thumbnail(url= member.avatar_url)
        embed.set_footer(text='Hab Spaß')

        try:
            if not member.dm_channel:
                await member.create_dm()
            await member.dm_channel.send(embed=embed)
        except discord.errors.Forbidden:
            print('Es konnte keine Willkommensnachricht an {} gesendet werden.'.format(
                member.name))

countercommand = 0
counterhelp = 0
counterall = 0
counterban = 0
counteruserinfo = 0
counterkick = 0
counterunban = 0
counterclear = 0
counteraua = 0
counterwarum = 0
counterspanisch = 0
counterdeutschland = 0
counterhokuspokus = 0

@client.event
async def on_message(message):    
    author = message.author    
    if message.author.bot:
        return
    if '.help' in message.content:  
        global counterall      
        counterall += 1
        counterhelp =+ 1
        print(f'@{author.name} hat .help benutzt' )
        await message.channel.send('```All the commands you can use for the moderationbot®\r\n'
                                   '1. .help \n2. .ban + .unban + .kick \n3. .userinfo \n4. .clear \n5. .hokuspokus \n6. .command \nif you want more detail about a command just type help+command (example: helpexamle)```')
    if '.command'in message.content:
        global countercommand
        counterall += 1
        countercommand = + 1
        embed = discord.Embed(title=f'Hallo @{author.name} ',
                              description=f'Ich wurde bereits {counterall} mal genutzt',
                              color=0x22a7f0)
        embed.set_thumbnail(url=author.avatar_url)
        embed.set_footer(text='Mach weiter so!')
        mess = await message.channel.send(embed=embed)

    if 'helpban' in message.content:
        print(f'@{author.name} hat helpban benutzt')
        await message.channel.send('**This command can be used by people with permisson to ban people. It has to be used like this: .ban MaxMustermann**')

    if 'helpkick' in message.content:
        print(f'@{author.name} hat helpkick benutzt')
        await message.channel.send('**This command can be used by people with permisson to kick people. It has to be used like this: .kick MaxMustermann**')

    if 'helpunban' in message.content:
        print(f'@{author.name} hat helpunban benutzt')
        await message.channel.send('**This command can be used by people with permisson to unban people. It has to be used like this: .unban MaxMustermann**')

    if 'helpuserinfo' in message.content:
        print(f'@{author.name} hat helpuserinfo benutzt')
        await message.channel.send('**With this command you can get all the infos you need about other server members. Can be used like this: .userinfo MaxMustermann**')

    if 'helphokuspokus' in message.content:
        print(f'@{author.name} hat helphokuspokus benutzt')
        await message.channel.send('**Just ask a question and the bot will answer you. Can be used like this: .hokuspokus Am I dumb?**')

    if 'helpclear' in message.content:
        print(f'@{author.name} hat helpclear benutzt')
        await message.channel.send('**This command can be used by people with permisson to clear the chat. Can be used like this: .clear 3**')

    if message.content.startswith('.ban') and message.author.guild_permissions.ban_members:
        global counterban
        counterall += 1
        counterban =+ 1
        print(f'@{author.name} hat .ban benutzt')
        count4=int(1)+1
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(
                lambda m: args[1] in m.name, message.guild.members)
            if member:
                mess = await message.channel.send(f'{member.name} wird in 10...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 9...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 8...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name}wird in 7...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 6...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 5...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 4...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 3...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 2...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 1...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 0 gebannt')
                time.sleep(0.5)
                await mess.edit(content=f'**@{member.name} wird von Big Mac :hamburger: gebannt**')
                await member.ban()
                deleted = await message.channel.purge(limit=count4, check=is_not_pinned)
                embed = discord.Embed(title=f'@Hw @bjarne \n@{member.name} wurde gebannt',
                              color=0x22a7f0)
                embed.set_footer(text='Es soll allen eine Lehre sein')
                mess = await message.channel.send(embed=embed)
                print(f'Big mac war da und hat @{member.name} gebannt')
            else:
                await message.channel.send(f'Kein user mit dem Namen {args[1]} gefunden.')

    if message.content.startswith('.unban') and message.author.guild_permissions.ban_members:
        global counterunban
        counterall += 1
        counterunban =+ 1
        print(f'@{author.name} hat .unban benutzt')
        args = message.content.split(' ')
        if len(args) == 2:
            user: User = discord.utils.find(lambda m: args[1] in m.user.name, await message.guild.bans()).user
            if user:
                await message.guild.unban(user)
                await message.channel.send(f'User {user.name} entbannt.')
            else:
                await message.channel.send(f'Kein user mit dem Namen {args[1]} gefunden.')

    if message.content.startswith('.kick') and message.author.guild_permissions.kick_members:
        global counterkick
        counterall += 1
        counterkick =+ 1
        print(f'@{author.name} hat .kick benutzt')
        count5 = int(1)
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(
                lambda m: args[1] in m.name, message.guild.members)
            if member:
                mess = await message.channel.send(f'@{member.name} wird in 10...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 9...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 8...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name}wird in 7...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 6...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 5...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 4...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 3...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 2...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 1...')
                time.sleep(0.5)
                await mess.edit(content=f'@{member.name} wird in 0 gekickt')
                time.sleep(0.5)
                await mess.edit(content=f'**@{member.name} wird von Big Mac :hamburger: gekickt**')
                await member.kick()
                deleted = await message.channel.purge(limit=count5, check=is_not_pinned)
                await mess.edit(embed = discord.Embed(title=f'@Hw @bjarne \n@{member.name} wurde gekickt',
                              color=0x22a7f0))
                embed.set_footer(text='Es soll allen eine Lehre sein')
                mess = await message.channel.send(embed=embed)
                print(f'Big mac war da und hat @{member.name} gekickt')
            else:
                await message.channel.send(f'Kein user mit dem Namen {args[1]} gefunden.')

    if message.content.startswith('.userinfo'):
        global counteruserinfo
        counterall += 1
        counteruserinfo =+ 1
        print(f'@{author.name} hat .userinfo benutzt')
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(
                lambda m: args[1] in m.name, message.guild.members)
            if member:
                embed = discord.Embed(title='Userinfo für {}'.format(member.name),
                                      description='Dies ist eine Userinfo für den User {}'.format(
                                          member.mention),
                                      color=0x22a7f0)
                embed.add_field(name='Server beigetreten', value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                embed.add_field(name='Discord beigetreten', value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                rollen = ''
                for role in member.roles:
                    if not role.is_default():
                        rollen += '{} \r\n'.format(role.mention)
                if rollen:
                    embed.add_field(name='Rollen', value=rollen, inline=True)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text='Mit der Hilfe vom moderationbot')
                mess = await message.channel.send(embed=embed)
                await mess.add_reaction('🚍')
                await mess.add_reaction('🚍')
                await mess.add_reaction('🚍')

    if message.content.startswith('.clear'):
        global counterclear
        counterall += 1
        counterclear =+ 1
        print(f'@{author.name} hat .clear benutzt')
        if message.author.permissions_in(message.channel).manage_messages:
            args = message.content.split(' ')
            if len(args) == 2:
                if args[1].isdigit():
                    count = int(args[1]) + 1
                    count2 = int(1)
                    deleted = await message.channel.purge(limit=count, check=is_not_pinned)
                    await message.channel.send('{} Nachrichten gelöscht.'.format(len(deleted) - 1))
                    time.sleep(3.7)
                    deleted = await message.channel.purge(limit=count2, check=is_not_pinned)

    if message.content.startswith('.hokuspokus'):
        global counterhokuspokus
        counterall += 1
        counterhokuspokus =+ 1
        print(f'@{author.name} hat .hokuspokus benutzt')
        args = message.content.split(' ')
        if len(args) >= 2:
            frage = ' '.join(args[1:])
            mess = await message.channel.send('Ich versuche deine Frage `{0}` zu beantworten.'.format(frage))
            await asyncio.sleep(2)
            await mess.edit(content='Chill bro...')
            await asyncio.sleep(2)
            await mess.edit(content='Deine Antwort zur Frage `{0}` lautet: `{1}`'.format(frage,
                                                                                         random.choice(antworten)))
    
    if message.content.startswith('.aua'):
        global counteraua
        counterall += 1
        counteraua =+ 1
        print(f'@{author.name} hat .aua benutzt')
        await message.channel.send('Wird schon wieder')    
    if message.content.startswith('warum'):
        global counterwarum
        counterall += 1
        counterwarum =+ 1
        print(f'@{author.name} hat warum benutzt')
        await message.channel.send('darum')
    if message.content.startswith('.spanisch'):
        global counterspanisch
        counterall += 1
        counterspanisch =+ 1
        print(f'@{author.name} hat .spanisch benutzt')
        await message.channel.send('Hola cómo estas?') 
    if message.content.startswith('deutschland'):
        global counterdeutschland
        counterall += 1
        counterdeutschland =+ 1
        print(f'@{author.name} hat deutschland benutzt')
        await message.channel.send('moskau moskau')
    
    

    if 'Hurensohn' in message.content or 'Huso' in message.content or 'hurensohn' in message.content or 'huso' in message.content or 'Wixxer' in message.content or 'wixxer' in message.content or 'Bastard' in message.content or 'bastard' in message.content or 'Du Hund' in message.content or 'du Hund' in message.content or 'du hund' in message.content or 'Du hund' in message.content or 'hundesohn' in message.content or 'nutte' in message.content or 'nuttensohn' in message.content or 'bitch' in message.content or 'moritz meyka' in message.content or 'hentschel' in message.content or 'dummkopf' in message.content or 'schlampe' in message.content or 'Schlampe' in message.content or 'Nutte' in message.content or 'Dummkopf' in message.content or 'Fotze' in message.content or 'Send Nudes' in message.content or 'nudes' in message.content or 'sex' in message.content or 'nigga' in message.content or 'Nigga' in message.content or 'Nibba' in message.content or 'nibba' in message.content or 'Neger' in message.content or 'neger' in message.content or 'Schwuchtel' in message.content or 'schwuchtel' in message.content or 'schwul' in message.content or 'Lesbe' in message.content or 'Kek' in message.content or 'Fettsack' in message.content or 'fettsack' in message.content or 'Mülleimer' in message.content or 'vergewaltige' in message.content or 'rape' in message.content or 'tits' in message.content or 'sex' in message.content:
        count3 = int(3)+1
        author = message.author        
        embed = discord.Embed(title=f'@Hw @bjarne \n@{author.name} wird wegen Beleidigungen gebannt',
                              description= f'(Beleidigung die er geschrieben hat: {message.content}) ',
                              color= 0x22a7f0)
        embed.set_thumbnail(url=author.avatar_url)
        embed.set_footer(text='Es soll ihm eine Lehre sein')     
        mess = await message.channel.send(embed=embed)
        
        mess = await message.channel.send(f'{author.name} wird in 10...')
        time.sleep(0.5)
        await mess.edit(content= f'@{author.name} wird in 9...')
        time.sleep(0.5)
        await mess.edit(content= f'@{author.name} wird in 8...')
        time.sleep(0.5)
        await mess.edit(content= f'@{author.name}wird in 7...')
        time.sleep(0.5)
        await mess.edit(content= f'@{author.name} wird in 6...')
        time.sleep(0.5)
        await mess.edit(content= f'@{author.name} wird in 5...')
        time.sleep(0.5)
        await mess.edit(content= f'@{author.name} wird in 4...')
        time.sleep(0.5)
        await mess.edit(content= f'@{author.name} wird in 3...')
        time.sleep(0.5)
        await mess.edit(content= f'@{author.name} wird in 2...')
        time.sleep(0.5)
        await mess.edit(content= f'@{author.name} wird in 1...')
        time.sleep(0.5)
        await mess.edit(content= f'@{author.name} wird in 0 gebannt')
        time.sleep(0.5)  
        await mess.edit(content= f'**@{author.name} wird von Big Mac :hamburger: gebannt**')
        await author.ban()
        time.sleep(2)
        deleted = await message.channel.purge(limit=count3, check=is_not_pinned)
        embed = discord.Embed(title= f'@Hw @bjarne \n@{author.name} wurde wegen Beleidigungen gebannt',                              
                              color=0x22a7f0)    
        embed.set_footer(text='Es soll allen eine Lehre sein')
        mess = await message.channel.send(embed=embed)
        print(f'Big mac war da und hat @{message.author} gebannt')



    if counterall == 100:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 100 commands beantworten\n', color=0x22a7f0))
        print('Ich wurde bisher insgesamt 100 mal benutzt')     
    if counterall == 200:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 200 commands beantworten\n', color=0x22a7f0))
        print('Ich wurde bisher insgesamt 200 mal benutzt')
    if counterall == 500:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 500 commands beantworten\n', color=0x22a7f0))
        print('Ich wurde bisher insgesamt 500 mal benutzt')
    if counterall == 1000:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 1000 commands beantworten\n', color=0x22a7f0))
        print('Ich wurde bisher insgesamt 1000 mal benutzt')
    if counterall == 3000:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 3000 commands beantworten\n', color=0x22a7f0))
        print('Ich wurde bisher insgesamt 3000 mal benutzt')
    if counterhelp == 100:        
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 100 mal den helpcommand beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 100 mal den helpcommand benutzt')
    if counterhelp == 500:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 500 mal den helpcommand beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 500 mal den helpcommand benutzt')
    if counterban == 100:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 100 mal den bancommand beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 100 mal den bancommand benutzt')
    if counterban == 500:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 500 mal den bancommand beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 500 mal den bancommand benutzt')
    if counteruserinfo == 100:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 100 mal den userinfocommand beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 100 mal den userinfocommand benutzt')
    if counteruserinfo == 500:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 500 mal den userinfo command beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 500 mal den userinfocommand benutzt')
    if counterkick == 100:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 100 mal den kick command beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 100 mal den kickcommand benutzt')
    if counterkick == 500:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 500 mal den kick command beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 500 mal den kickcommand benutzt')
    if counterunban == 100:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 100 mal den unbancommand beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 100 mal den unbancommand benutzt')
    if counterunban == 500:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 500 mal den unban command beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 500 mal den unbancommand benutzt')
    if counterclear == 100:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 100 mal den clearcommand beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 100 mal den clearcommand benutzt')
    if counterclear == 500:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 500 mal den clearcommand beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 500 mal den clearcommand benutzt')
    if counterhokuspokus == 100:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 100 mal den hokuspokuscommand beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 100 mal den hokuspokuscommand benutzt')
    if counterhokuspokus == 500:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 500 mal den hokuspokuscommand beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 500 mal den hokuspokuscommand benutzt')
    if counteraua == 200:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 200 mal den auacommand beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 200 mal den auascommand benutzt')
    if counterwarum == 300:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 300 mal den warumcommand beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 300 mal den warumcommand benutzt')
    if counterspanisch == 100:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 100 mal den spanischcommand beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 100 mal den spanischcommand benutzt')
    if counterdeutschland == 100:
        channel = client.get_channel(777277378191425557)
        await channel.send(embed=discord.Embed(title=f'Congratualations @everyone\nich durfte schon insgesamt 100 mal den deutschlandcommand beantworten\n', color=0x22a7f0))
        print('Ich habe bisher insgesamt 100 mal den deutschlandcommand benutzt')
    while h == True:
        count7= int(1)
        channel = client.get_channel(777277378191425557)
        time.sleep(43200)
        deleted = await message.channel.purge(limit=count7, check=is_not_pinned)
        embed=discord.Embed(title=f'Ich wurde insgesammt {counterall} mal benutzt',
                            description = 'Diese Nachricht wird alle 12 Stunden erscheinen (also habt ihr ein halbtägiges update)',
                                               color=0x22a7f0)
        embed.set_thumbnail(url=author.avatar_url)
        embed.set_footer(text='Macht weiter so!!!')
        mess=await channel.send(embed=embed)
        print('insgesammt benutze commands: ', counterall)


    
    

client.run('')

