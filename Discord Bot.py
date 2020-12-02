import asyncio
import random

import discord
from discord import Member, Guild

client = discord.Client()


#edit your answers here
antworten =['yes', 'no']


@client.event
async def on_ready():
    print('we are logged in as {} '
    .format(client.user.name))
    client.loop.create_task(status_task())

#edit your status
async def status_task():

    while True:
        await client.change_presence(activity=discord.Game('Gandalf'), status=discord.Status.online)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game('Mr. Robot'), status=discord.Status.online)
        await asyncio.sleep(5)


def is_not_pinned(mess):
    return not mess.pinned


@client.event


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if '~help' in message.content:
        await message.channel.send('**following commands can be used:**\r\n'
                                   '~help - shows this message \r\n~userinfo + name - shows all userinfos \n~clear + number - errase messages \n~fragerunde + your question - gives you an answer on everything')


    if message.content.startswith('!ban') and message.author.guild_permissions.ban_members:
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                await member.ban()
                await message.channel.send(f'Member {member.name} banned.')
            else:
                await message.channel.send(f'No user with name  {args[1]} found.')
    if message.content.startswith('!unban') and message.author.guild_permissions.ban_members:
        args = message.content.split(' ')
        if len(args) == 2:
            user: User = discord.utils.find(lambda m: args[1] in m.user.name, await message.guild.bans()).user
            if user:
                await message.guild.unban(user)
                await message.channel.send(f'User {user.name} unbanned.')
            else:
                await message.channel.send(f'no user with {args[1]} found.')
    if message.content.startswith('!kick') and message.author.guild_permissions.kick_members:
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                await member.kick()
                await message.channel.send(f'Member {member.name} kicked.')
            else:
                await message.channel.send(f'No user  {args[1]} found.')

    if message.content.startswith('~userinfo'):
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                embed = discord.Embed(title='Userinfo for {}'.format(member.name),
                                      description='this is the userinfo for {}'.format(member.mention),
                                      color=0x22a7f0)
                embed.add_field(name='Server joined', value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                embed.add_field(name='Discord joined', value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                rollen = ''
                for role in member.roles:
                    if not role.is_default():
                        rollen += '{} \r\n'.format(role.mention)
                if rollen:
                    embed.add_field(name='roles', value=rollen, inline=True)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text='Created with EmbedFooter.')
                mess = await message.channel.send(embed=embed)
                await mess.add_reaction('🦾')
                await mess.add_reaction('👾')
                await mess.add_reaction('📝')
                await mess.add_reaction('🤖')
                await mess.add_reaction('👨‍💻')
    if message.content.startswith('~clear'):
        if message.author.permissions_in(message.channel).manage_messages:
            args = message.content.split(' ')
            if len(args) == 2:
                if args[1].isdigit():
                    count = int(args[1]) + 1
                    deleted = await message.channel.purge(limit=count, check=is_not_pinned)
                    await message.channel.send('{} messages errased'.format(len(deleted)-1))
    if message.content.startswith('~fragerunde'):
        args = message.content.split(' ')
        if len(args) >= 2:
            frage = ' '.join(args[1:])
            mess = await message.channel.send('I try to answer your question `{0}` '.format(frage))
            await asyncio.sleep(3)
            await mess.edit(content='Chill bro...')
            await asyncio.sleep(4)
            await mess.edit(content='Your answer to this question`{0}` is: `{1}`'
                            .format(frage, random.choice(antworten)))


#Your client number here
client.run('')