import asyncio
import discord
from discord.ext.commands import Bot


Mike = Bot('x!')

@Mike.event
async def on_ready():
    print ("Starting up")
    print ("My username is " + Mike.user.name + " and i am running with the ID: " + Mike.user.id)
    await Mike.change_presence(game=discord.Game(name="in heaven... 💫", type=0))
    print ("Started")
    
Mike.remove_command('help')

@Mike.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await Mike.delete_message(ctx.message)
    return await Mike.say(mesg)


Mike.run('NTU4NTQyODkwMzA2MTA5NDUy.D3YanQ.gM-hClkh5jZzwanTY_fyrISjx80')
