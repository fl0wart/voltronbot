import asyncio
import discord
from discord.ext.commands import Bot


Mike = Bot('s!')

@Mike.event
async def on_ready():
    print ("Starting up")
    print ("My username is " + Mike.user.name + " and i am running with the ID: " + Mike.user.id)
    await Mike.change_presence(game=discord.Game(name="the police station! 👀", type=3))
    print ("Started")
    
Mike.remove_command('help')

@Mike.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await Mike.delete_message(ctx.message)
    return await Mike.say(mesg)


Mike.run('NTU4NTQyODkwMzA2MTA5NDUy.D3YXMg.nHPbOLS3AFV3J-D9s3jK6DZWwEg')
