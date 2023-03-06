import utils
import init
import discord



TOKEN=init.get_token()

GUILD = "H2O"
print(type(TOKEN),str(TOKEN))



# ---------------------------------------Bot Init---------------------------------------

# intents决定了机器人能干什么，default为默认，后续代码将向intents添加权限
intents = discord.Intents.default()
# Change authorisation in init.access
for i in init.access:
    exec("intents."+i+" = True")
client = discord.Client(intents=intents)
# ---------------------------------------Bot Init---------------------------------------


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    # for guild in client.guilds:
    #     print(guild.id)



'''
@client.event
async def on_ready():
    for guild in client.guilds:
        
        if guild.name == '???':
            print(guild.name)
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    #print(f'Guild Members:\n - {members}')
    for i in guild.members:
        #print(i.name,'-',i.id)

'''

@client.event
async def on_message(message):
    #print(message.content)
    result=utils.reader(message.content)
    #print(result)
    if result is not None:
        await message.channel.send(result)
    
# @client.event
# async def on_voice_state_update(member, before, after):
#     
#     member_x=GUId.get_member(id)
#     member_y=GUId.get_member()#wo
#     status=member_y.voice
#     # if status.channel!=chufang:
#     #     await member_x.move_to(chufang)
#     #     print("!!!!")
#     # status=member_y.voice
#     if status.channel!=main_channel:
#         await member_y.move_to(None)
#         print("!!!!")
client.run(TOKEN)
