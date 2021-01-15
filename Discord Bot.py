

import asyncio
import random
import time
import discord
from discord import Member, Guild, User


client = discord.Client(intents=discord.Intents.all())
#########################################################################

songliste = ['Herzbeben', '99 luftballons']
antworten = ['Ja', 'Nein', 'Vielleicht', 'Wahrscheinlich', 'Sieht so aus', 'Sehr wahrscheinlich',
             'Sehr unwahrscheinlich', 'drei', '9999999999999999999999999999999999999999999999999']

autoroles = {
    658960248345853952: {'memberroles': [667129769397059596, 667129722995474460], 'botroles': [667129686131736586]},
    643782995869827092: {'memberroles': [], 'botroles': []}
}


@client.event
async def on_ready():
    print('Du bist eingeloggt als Bot mit dem Namen: {}'.format(client.user.name))
    client.loop.create_task(status_task())


async def status_task():

    await client.change_presence(activity=discord.Game('type .help'), status=discord.Status.online)
    await asyncio.sleep(20)
    await client.change_presence(activity=discord.Game('then specify'), status=discord.Status.online)
    await asyncio.sleep(2)
    guild: Guild = client.get_guild(658960248345853952)


def is_not_pinned(mess):
    return not mess.pinned


@client.event
async def on_member_join(member):
    guild: Guild = member.guild
    if not member.bot:
        embed = discord.Embed(title='Willkommen auf dem Superguay Server {} (va a ser superguay)'.format(member.name),
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
        autoguild = autoroles.get(guild.id)
        if autoguild and autoguild['memberroles']:
            for roleId in autoguild['memberroles']:
                role = guild.get_role(roleId)
                if role:
                    await member.add_roles(role, reason='AutoRoles', atomic=True)
    else:
        autoguild = autoroles.get(guild.id)
        if autoguild and autoguild['botroles']:
            for roleId in autoguild['botroles']:
                role = guild.get_role(roleId)
                if role:
                    await member.add_roles(role, reason='AutoRoles', atomic=True)


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if '.help' in message.content:
        await message.channel.send('```All the commands you can use for the moderationbot®\r\n'
                                   '1. .help \n2. .ban + .unban + .kick \n3. .userinfo \n4. .clear \n5. .hokuspokus \nif you want more detail about a command just type help+command (example: helpexamle)```')

    if 'helpban' in message.content:
        await message.channel.send('**This command can be used by people with permisson to ban people. It has to be used like this: .ban MaxMustermann**')

    if 'helpkick' in message.content:
        await message.channel.send('**This command can be used by people with permisson to kick people. It has to be used like this: .kick MaxMustermann**')

    if 'helpunban' in message.content:
        await message.channel.send('**This command can be used by people with permisson to unban people. It has to be used like this: .unban MaxMustermann**')

    if 'helpuserinfo' in message.content:
        await message.channel.send('**With this command you can get all the infos you need about other server members. Can be used like this: .userinfo MaxMustermann**')

    if 'helphokuspokus' in message.content:
        await message.channel.send('**Just ask a question and the bot will answer you. Can be used like this: .hokuspokus Am I dumb?**')

    if 'helpclear' in message.content:
        await message.channel.send('**This command can be used by people with permisson to clear the chat. Can be used like this: .clear 3**')

    if message.content.startswith('.ban') and message.author.guild_permissions.ban_members:
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(
                lambda m: args[1] in m.name, message.guild.members)
            if member:
                await member.ban()
                await message.channel.send(f'Member {member.name} gebannt.')
            else:
                await message.channel.send(f'Kein user mit dem Namen {args[1]} gefunden.')

    if message.content.startswith('.unban') and message.author.guild_permissions.ban_members:
        args = message.content.split(' ')
        if len(args) == 2:
            user: User = discord.utils.find(lambda m: args[1] in m.user.name, await message.guild.bans()).user
            if user:
                await message.guild.unban(user)
                await message.channel.send(f'User {user.name} entbannt.')
            else:
                await message.channel.send(f'Kein user mit dem Namen {args[1]} gefunden.')

    if message.content.startswith('.kick') and message.author.guild_permissions.kick_members:
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(
                lambda m: args[1] in m.name, message.guild.members)
            if member:
                await member.kick()
                await message.channel.send(f'Member {member.name} gekickt.')
            else:
                await message.channel.send(f'Kein user mit dem Namen {args[1]} gefunden.')

    if message.content.startswith('.userinfo'):
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

    if message.content.startswith('.clear'):
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
        args = message.content.split(' ')
        if len(args) >= 2:
            frage = ' '.join(args[1:])
            mess = await message.channel.send('Ich versuche deine Frage `{0}` zu beantworten.'.format(frage))
            await asyncio.sleep(2)
            await mess.edit(content='Chill bro...')
            await asyncio.sleep(2)
            await mess.edit(content='Deine Antwort zur Frage `{0}` lautet: `{1}`'.format(frage,
                                                                                         random.choice(antworten)))
    if message.content.startswith('.song'):
        args = message.content.split(' ')
        if len(args) >= 2:
            frage = ' '.join(args[1:])
            mess = await message.channel.send('Ich suche nach einem passenden Song.')
            await asyncio.sleep(2)
            await mess.edit(content='Ich habe einen passenden Song gefunden...')
            await asyncio.sleep(2)
            await mess.edit(content='Hier ist der passende Song `{0}` reads: {1}'.format
                                                                                (random.choice(songliste)))
    if message.content.startswith('.avatar'):
        args = message.content.split(' ')
        if len(args) >= 2:
            member: Member = discord.utils.find(
                lambda m: args[1] in m.name, message.guild.members)
            if member:
                embed = discord.Embed(title=f'Avatar von {member.name}',
                                      color=0x22a7f0)
                embed.set_image(url=member.avatar_url)
                embed.set_footer(text='moderationbot')
client.run('')
