import discord
import os
import time
from discord.ext import tasks
from datetime import datetime
import asyncio

mod_channel_id = 838288771040149534
support_1_id = 837962582152445972
support_2_id = 837945208914182154
support_3_id = 838011782483410965
support_4_id = 838011799026663424
support_5_id = 838011813261213746
support_6_id = 838073827304407040
support_7_id = 838073845247246357

ratelimitVar1 = 0
ratelimitVar2 = 0
ratelimitVar3 = 0
ratelimitVar4 = 0
ratelimitVar5 = 0
ratelimitVar6 = 0
ratelimitVar7 = 0

lockedVar1 = 0
lockedVar2 = 0
lockedVar3 = 0
lockedVar4 = 0
lockedVar5 = 0
lockedVar6 = 0
lockedVar7 = 0

lockedVarUp1 = 0
lockedVarUp2 = 0
lockedVarUp3 = 0
lockedVarUp4 = 0
lockedVarUp5 = 0
lockedVarUp6 = 0
lockedVarUp7 = 0

lastText1 = 0
lastText2 = 0
lastText3 = 0
lastText4 = 0
lastText5 = 0
lastText6 = 0
lastText7 = 0

lastTextTimeout = 20
rateLimit = 15

support_1_val = 0
support_2_val = 0
support_3_val = 0
support_4_val = 0
support_5_val = 0
support_6_val = 0
support_7_val = 0

support_1_msg = 0
support_2_msg = 0
support_3_msg = 0
support_4_msg = 0
support_5_msg = 0
support_6_msg = 0
support_7_msg = 0

runtime_status = 0

help_value_msg = "The channels with ✅ is ready to ask help, \n The channels with ❕ is in use."
help_value1_msg = "Make sure your question have enough content for others to understand"
help_value2_msg = "After your question is solved type **!close** to make the channel \navailable for others"

help_embed=discord.Embed(
    title="How to use the bot?",
    description="Make sure you read this before asking a **question**.",
    color=0x00adb5
    )
help_embed.add_field(
    name="Step 1 : Find a Avaiable channel.",
    value="".join(help_value_msg),
    inline=False)
help_embed.add_field(
    name="Step 2 : Enter your question clearly.",
    value="".join(help_value1_msg),
    inline=False)    
help_embed.add_field(
    name="Step 3 : Wait for others to answer your Question!",
    value="".join(help_value2_msg),
    inline=False)       
help_embed.set_footer(text="This bot is developed by RohitTechZone#4756")
avai_msg = "**Message Below to claim the channel** \n Your Message will be pinned for others to help"
#avai_footer_msg = "It will automatically open when you send a message. \n \n Subscribe to [**RohitTechZone**](https://www.youtube.com/c/RohitTechZone/)"
unavai_msg = "**Your Question is pinned** \n Now wait for Helpers to help you"
avai_value_msg = "• Anyone can post a question \n • Make sure your question is understandable \n \n **Bot Developed By :** \n [**  RohitTechZone**](https://www.youtube.com/channel/UCHuclaeGtkhW5nN6gBRwMrg/)" 
unavai_value_msg = "• Anyone can post a question \n • Make sure your question is understandable" 
locked_msg = "Channel will be unlocked soon. \n For help look for other open channels" 
timeout_msg = "The Channel is closed now due to inactivity. \n If your question has not yet answered, claim another help channel" 
client = discord.Client()

avai_embed=discord.Embed(
    title=":white_check_mark: Channel Available!",
    description="".join(avai_msg),
    color=0x00ff00)
avai_embed.add_field(
    name="Note :",
    value="".join(avai_value_msg))

   #print(message.message.server)
   #avai_embed.set_thumbnail(url=message.server.avatar_url)
avai_embed.set_footer(text="It will automatically open when you send a message.")
timeout_embed=discord.Embed(
    title="Timeout! No message has been sent in past 20 minutes",
    description="".join(timeout_msg),
    color=0xff0000)
init_embed=discord.Embed(
    title="Bot initialized!",
    description="The bot has been resetted",
    color=0xa0fff0)    
@tasks.loop(seconds=30)
async def check():
  global support_1_val
  global support_2_val
  global support_2_msg
  global support_1_msg
  global support_3_val
  global support_4_val
  global support_3_msg
  global support_4_msg
  global support_5_val
  global support_6_val
  global support_5_msg
  global support_6_msg
  global support_7_val
  global support_7_msg
  global ratelimitVar1
  global ratelimitVar2
  global ratelimitVar3
  global ratelimitVar4
  global ratelimitVar5
  global ratelimitVar6
  global ratelimitVar7
  global lockedVar1
  global lockedVar2
  global lockedVar3
  global lockedVar4
  global lockedVar5
  global lockedVar6
  global lockedVar7
  global lastText1
  global lastText2
  global lastText3
  global lastText4
  global lastText5
  global lastText6
  global lastText7
  global lastTextUp1
  global lastTextUp2
  global lastTextUp3
  global lastTextUp4
  global lastTextUp5
  global lastTextUp6
  global lastTextUp7
  global lastTextTimeout
  global rateLimit
  global mod_channel
  global runtime_status
  current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
  if lastText1 >=0 and lastText1 < lastTextTimeout and current_time >= 1440-lastTextTimeout and current_time < 1440:
     current_time = -1
  if lastText1 <= current_time and support_1_val == 1 and lastTextUp1 == 1:
    await client.get_channel(support_1_id).send(embed=timeout_embed)
    await support_1_msg.unpin()
    await client.get_channel(support_1_id).send(embed=avai_embed)
    support_1_val = 0
    await client.get_channel(support_1_id).edit(name="✅｜Support-1")

  current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
  if lastText2 >=0 and lastText2 < lastTextTimeout and current_time >= 1440-lastTextTimeout and current_time < 1440:
     current_time = -1  
  if lastText2 <= current_time and support_2_val == 1 and lastTextUp2 == 1:
    await client.get_channel(support_2_id).send(embed=timeout_embed)
    await support_2_msg.unpin()
    await client.get_channel(support_2_id).send(embed=avai_embed)
    support_2_val = 0
    await client.get_channel(support_2_id).edit(name="✅｜Support-2")  

  current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
  if lastText3 >=0 and lastText3 < lastTextTimeout and current_time >= 1440-lastTextTimeout and current_time < 1440:
     current_time = -1  
  if lastText3 <= current_time and support_3_val == 1 and lastTextUp3 == 1:
    await client.get_channel(support_3_id).send(embed=timeout_embed)
    await support_3_msg.unpin()
    await client.get_channel(support_3_id).send(embed=avai_embed)
    support_3_val = 0
    await client.get_channel(support_3_id).edit(name="✅｜Support-3")   

  current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
  if lastText4 >=0 and lastText4 < lastTextTimeout and current_time >= 1440-lastTextTimeout and current_time < 1440:
     current_time = -1  
  if lastText4 <= current_time and support_4_val == 1 and lastTextUp4 == 1:
    await client.get_channel(support_4_id).send(embed=timeout_embed)
    await support_4_msg.unpin()
    await client.get_channel(support_4_id).send(embed=avai_embed)
    support_4_val = 0
    await client.get_channel(support_4_id).edit(name="✅｜Support-4")   

  current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
  if lastText5 >=0 and lastText5 < lastTextTimeout and current_time >= 1440-lastTextTimeout and current_time < 1440:
     current_time = -1  
  if lastText5 <= current_time and support_5_val == 1 and lastTextUp5 == 1:
    await client.get_channel(support_5_id).send(embed=timeout_embed)
    await support_5_msg.unpin()
    await client.get_channel(support_5_id).send(embed=avai_embed)
    support_5_val = 0
    await client.get_channel(support_5_id).edit(name="✅｜Support-5")       

  current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
  if lastText6 >=0 and lastText6 < lastTextTimeout and current_time >= 1440-lastTextTimeout and current_time < 1440:
     current_time = -1   
  if lastText6 <= current_time and support_6_val == 1 and lastTextUp6 == 1:
    await client.get_channel(support_6_id).send(embed=timeout_embed)
    await support_6_msg.unpin()
    await client.get_channel(support_6_id).send(embed=avai_embed)
    support_6_val = 0
    await client.get_channel(support_6_id).edit(name="✅｜Support-6")    

  current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
  if lastText7 >=0 and lastText7 < lastTextTimeout and current_time >= 1440-lastTextTimeout and current_time < 1440:
     current_time = -1    
  if lastText7 <= current_time and support_7_val == 1 and lastTextUp7 == 1:
    await client.get_channel(support_7_id).send(embed=timeout_embed)
    await support_7_msg.unpin()
    await client.get_channel(support_7_id).send(embed=avai_embed)
    support_7_val = 0
    await client.get_channel(support_7_id).edit(name="✅｜Support-7")           
  print("test")
  print(lastText1, current_time, lockedVar1 == 1)
  print(lastText3, current_time, lockedVar3 == 1)
  print(lastText7, current_time, lockedVar7 == 1)
  current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
  if ratelimitVar1 >=0 and ratelimitVar1 < rateLimit and current_time >= 1440-rateLimit and current_time < 1440:
     current_time = -1
  if ratelimitVar1 <= current_time and lockedVar1 == 1:
      await client.get_channel(support_1_id).send(embed=avai_embed)
      support_1_val = 0
      await support_1_msg.unpin()
      channel = client.get_channel(support_1_id)
      overwrite = channel.overwrites_for(channel.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)
      lockedVar1 = 0 
      await client.get_channel(support_1_id).edit(name="✅｜Support-1")
  current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])    
  if ratelimitVar2 >=0 and ratelimitVar2 < rateLimit and current_time >= 1440-rateLimit and current_time < 1440:
     current_time = -1    
  if ratelimitVar2 <= current_time and lockedVar2 == 1:
      await client.get_channel(support_2_id).send(embed=avai_embed)
      support_2_val = 0
      await support_2_msg.unpin()
      channel = client.get_channel(support_2_id)
      overwrite = channel.overwrites_for(channel.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)
      lockedVar2 = 0 
      await client.get_channel(support_2_id).edit(name="✅｜Support-2") 
  current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])    
  if ratelimitVar3 >=0 and ratelimitVar3 < rateLimit and current_time >= 1440-rateLimit and current_time < 1440:
     current_time = -1    
  if ratelimitVar3 <= current_time and lockedVar3 == 1:
      await client.get_channel(support_3_id).send(embed=avai_embed)
      support_3_val = 0
      channel = client.get_channel(support_3_id)
      overwrite = channel.overwrites_for(channel.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)
      await support_3_msg.unpin()
      lockedVar3 = 0 
      await client.get_channel(support_3_id).edit(name="✅｜Support-3")   
  current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])        
  if ratelimitVar4 >=0 and ratelimitVar4 < rateLimit and current_time >= 1440-rateLimit and current_time < 1440:
     current_time = -1    
  if ratelimitVar4 <= current_time and lockedVar4 == 1:
      await client.get_channel(support_4_id).send(embed=avai_embed)
      support_4_val = 0
      channel = client.get_channel(support_4_id)
      overwrite = channel.overwrites_for(channel.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)
      await support_4_msg.unpin()
      lockedVar4 = 0 
      await client.get_channel(support_4_id).edit(name="✅｜Support-4") 
  current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])    
  if ratelimitVar5 >=0 and ratelimitVar5 < rateLimit and current_time >= 1440-rateLimit and current_time < 1440:
     current_time = -1              
  if ratelimitVar5 <= current_time and lockedVar5 == 1:
      await client.get_channel(support_5_id).send(embed=avai_embed)
      support_5_val = 0
      channel = client.get_channel(support_5_id)
      overwrite = channel.overwrites_for(channel.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)
      await support_5_msg.unpin()
      lockedVar5 = 0 
      await client.get_channel(support_5_id).edit(name="✅｜Support-5")       
  current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])    
  if ratelimitVar6 >=0 and ratelimitVar6 < rateLimit and current_time >= 1440-rateLimit and current_time < 1440:
     current_time = -1    
  if ratelimitVar6 <= current_time and lockedVar6 == 1:
      await client.get_channel(support_6_id).send(embed=avai_embed)
      support_6_val = 0
      channel = client.get_channel(support_6_id)
      overwrite = channel.overwrites_for(channel.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)
      await support_6_msg.unpin()
      lockedVar6 = 0 
      await client.get_channel(support_6_id).edit(name="✅｜Support-6")
  current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])    
  if ratelimitVar7 >=0 and ratelimitVar7 < rateLimit and current_time >= 1440-rateLimit and current_time < 1440:
     current_time = -1    
  if ratelimitVar7 <= current_time and lockedVar7 == 1:
      await client.get_channel(support_7_id).send(embed=avai_embed)
      support_7_val = 0
      channel = client.get_channel(support_7_id)
      overwrite = channel.overwrites_for(channel.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)
      await support_7_msg.unpin()
      lockedVar7 = 0 
      await client.get_channel(support_7_id).edit(name="✅｜Support-7")      
  if runtime_status == 0:
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="rohittechzone"))
     runtime_status = 1
  else:   
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="!help"))
     runtime_status = 0
@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))
    
    print(datetime.now())

    await check.start()

@client.event
async def on_message(message):
   if message.author == client.user:
      return
   global support_1_val
   global support_2_val
   global support_2_msg
   global support_1_msg
   global support_3_val
   global support_4_val
   global support_3_msg
   global support_4_msg
   global support_5_val
   global support_6_val
   global support_5_msg
   global support_6_msg
   global support_7_val
   global support_7_msg
   global ratelimitVar1
   global ratelimitVar2
   global ratelimitVar3
   global ratelimitVar4
   global ratelimitVar5
   global ratelimitVar6
   global ratelimitVar7
   global lockedVar1
   global lockedVar2
   global lockedVar3
   global lockedVar4
   global lockedVar5
   global lockedVar6
   global lockedVar7
   global lastText1
   global lastText2
   global lastText3
   global lastText4
   global lastText5
   global lastText6
   global lastText7
   global lastTextUp1
   global lastTextUp2
   global lastTextUp3
   global lastTextUp4
   global lastTextUp5
   global lastTextUp6
   global lastTextUp7
   global lastTextTimeout
   global rateLimit

   if message.content == "!initialize" and message.channel.id == mod_channel_id:
      support_1_val = 0
      support_2_val = 0
      support_3_val = 0
      support_4_val = 0
      support_5_val = 0
      support_6_val = 0
      support_7_val = 0
      channel = client.get_channel(support_1_id)
      overwrite = channel.overwrites_for(channel.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)

      channel = client.get_channel(support_2_id)
      overwrite = channel.overwrites_for(channel.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)

      channel = client.get_channel(support_3_id)
      overwrite = channel.overwrites_for(channel.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)

      channel = client.get_channel(support_4_id)
      overwrite = channel.overwrites_for(channel.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)

      channel = client.get_channel(support_5_id)
      overwrite = channel.overwrites_for(channel.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)

      channel = client.get_channel(support_6_id)
      overwrite = channel.overwrites_for(channel.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)

      channel = client.get_channel(support_7_id)
      overwrite = channel.overwrites_for(channel.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)
      await client.get_channel(support_1_id).send(embed=avai_embed)
      await client.get_channel(support_2_id).send(embed=avai_embed)
      await client.get_channel(support_3_id).send(embed=avai_embed)
      await client.get_channel(support_4_id).send(embed=avai_embed)
      await client.get_channel(support_5_id).send(embed=avai_embed)
      await client.get_channel(support_6_id).send(embed=avai_embed)
      await client.get_channel(support_7_id).send(embed=avai_embed)
      lockedVar1 = 0
      lockedVar2 = 0
      lockedVar3 = 0
      lockedVar4 = 0
      lockedVar5 = 0
      lockedVar6 = 0
      lockedVar7 = 0

      try:
          await support_1_msg.unpin()
      except:
          print("boot 1")
      try:
          await support_2_msg.unpin()
      except:
          print("boot 2")
      try:
          await support_3_msg.unpin()
      except:
          print("boot 3")
      try:
          await support_4_msg.unpin()
      except:
          print("boot 4")
      try:
          await support_5_msg.unpin()
      except:
          print("boot 5")
      try:
          await support_6_msg.unpin()
      except:
          print("boot 6")
      try:
          await support_7_msg.unpin()
      except:
          print("boot 7")
      await message.channel.send(embed=init_embed)
      await client.get_channel(support_1_id).edit(name="✅｜Support-1")
      await client.get_channel(support_2_id).edit(name="✅｜Support-2")
      await client.get_channel(support_3_id).edit(name="✅｜Support-3")
      await client.get_channel(support_4_id).edit(name="✅｜Support-4")
      await client.get_channel(support_5_id).edit(name="✅｜Support-5")
      await client.get_channel(support_6_id).edit(name="✅｜Support-6")
      await client.get_channel(support_7_id).edit(name="✅｜Support-7")


   if message.channel.id == support_1_id:
     lastText1 = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
     if lastText1 > (1440-lastTextTimeout-1):
        lastText1 = (lastTextTimeout-(1440-lastText1))
     else:
        lastText1 = lastText1+lastTextTimeout
     lastTextUp1 = 1
   elif message.channel.id == support_2_id:
     lastText2 = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
     if lastText2 > (1440-lastTextTimeout-1):
        lastText2 = (lastTextTimeout-(1440-lastText2))
     else:
        lastText2 = lastText2+lastTextTimeout
     lastTextUp2 = 1 
   elif message.channel.id == support_3_id:
     lastText3 = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
     if lastText3 > (1440-lastTextTimeout-1):
        lastText3 = (lastTextTimeout-(1440-lastText3))
     else:
        lastText3 = lastText3+lastTextTimeout
     lastTextUp3 = 1        
   elif message.channel.id == support_4_id:
     lastText4 = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
     if lastText4 > (1440-lastTextTimeout-1):
        lastText4 = (lastTextTimeout-(1440-lastText4))
     else:
        lastText4 = lastText4+lastTextTimeout
     lastTextUp4 = 1     
   elif message.channel.id == support_5_id:
     lastText5 = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
     if lastText5 > (1440-lastTextTimeout-1):
        lastText5 = (lastTextTimeout-(1440-lastText5))
     else:
        lastText5 = lastText5+lastTextTimeout
     lastTextUp5 = 1      
   elif message.channel.id == support_6_id:
     lastText6 = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
     if lastText6 > (1440-lastTextTimeout-1):
        lastText6 = (lastTextTimeout-(1440-lastText6))
     else:
        lastText6 = lastText6+lastTextTimeout
     lastTextUp6 = 1    
   elif message.channel.id == support_7_id:
     lastText7 = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
     if lastText7 > (1440-lastTextTimeout-1):
        lastText7 = (lastTextTimeout-(1440-lastText7))
     else:
        lastText7 = lastText7+lastTextTimeout
     lastTextUp7 = 1    
   re_close_embed=discord.Embed(
    title="Channel is already closed",
    description="".join(avai_msg),
    color=0x00f0ff)
   locked_embed=discord.Embed(
    title="Channel is locked",
    description="".join(locked_msg),
    color=0xff00ff)
   unavai_embed=discord.Embed(
    title="Channel Open!",
    description="".join(unavai_msg),
    color=0xffff00)
   #print(message.message.server)
   #avai_embed.set_thumbnail(url=message.server.avatar_url)
   unavai_embed.set_footer(text="Closes after a period of inactivity, or when you send !close.")
   
   if support_1_val == 0 and message.content != "!close" and message.channel.id == support_1_id:
      support_1_val = 1
      await message.channel.send(embed=unavai_embed)
      await message.pin()
      support_1_msg = message
      ratelimitVar1 = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
      if ratelimitVar1 > (1440-rateLimit-1):
        ratelimitVar1 = (rateLimit-(1440-ratelimitVar1))
      else:
        ratelimitVar1 = ratelimitVar1+rateLimit     
      await message.channel.edit(name="❕｜Support-1")
   elif support_2_val == 0 and message.content != "!close" and message.channel.id == support_2_id:
      support_2_val = 1
      await message.channel.send(embed=unavai_embed)
      await message.pin()
      support_2_msg = message
      ratelimitVar2 = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
      if ratelimitVar2 > (1440-rateLimit-1):
        ratelimitVar2 = (rateLimit-(1440-ratelimitVar2))
      else:
        ratelimitVar2 = ratelimitVar2+rateLimit     
      await message.channel.edit(name="❕｜Support-2")  
   elif support_3_val == 0 and message.content != "!close" and message.channel.id == support_3_id:
      support_3_val = 1
      await message.channel.send(embed=unavai_embed)
      await message.pin()
      support_3_msg = message
      ratelimitVar3 = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
      if ratelimitVar3 > (1440-rateLimit-1):
        ratelimitVar3 = (rateLimit-(1440-ratelimitVar3))
      else:
        ratelimitVar3 = ratelimitVar3+rateLimit     
      await message.channel.edit(name="❕｜Support-3")     
   elif support_4_val == 0 and message.content != "!close" and message.channel.id == support_4_id:
      support_4_val = 1
      await message.channel.send(embed=unavai_embed)
      await message.pin()
      support_4_msg = message
      ratelimitVar4 = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
      if ratelimitVar4 > (1440-rateLimit-1):
        ratelimitVar4 = (rateLimit-(1440-ratelimitVar4))
      else:
        ratelimitVar4 = ratelimitVar4+rateLimit     
      await message.channel.edit(name="❕｜Support-4")   
   elif support_5_val == 0 and message.content != "!close" and message.channel.id == support_5_id:
      support_5_val = 1
      await message.channel.send(embed=unavai_embed)
      await message.pin()
      support_5_msg = message
      ratelimitVar5 = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
      if ratelimitVar5 > (1440-rateLimit-1):
        ratelimitVar5 = (rateLimit-(1440-ratelimitVar5))
      else:
        ratelimitVar5 = ratelimitVar5+rateLimit     
      await message.channel.edit(name="❕｜Support-5")   
   elif support_6_val == 0 and message.content != "!close" and message.channel.id == support_6_id:
      support_6_val = 1
      await message.channel.send(embed=unavai_embed)
      await message.pin()
      support_6_msg = message
      ratelimitVar6 = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
      if ratelimitVar6 > (1440-rateLimit-1):
        ratelimitVar6 = (rateLimit-(1440-ratelimitVar6))
      else:
        ratelimitVar6 = ratelimitVar6+rateLimit
      await message.channel.edit(name="❕｜Support-6")   
   elif support_7_val == 0 and message.content != "!close" and message.channel.id == support_7_id:
      support_7_val = 1
      await message.channel.send(embed=unavai_embed)
      await message.pin()
      support_7_msg = message
      ratelimitVar7 = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
      if ratelimitVar7 > (1440-rateLimit-1):
        ratelimitVar7 = (rateLimit-(1440-ratelimitVar7))
        if ratelimitVar7 == 0:
           ratelimitVar7 = ratelimitVar7+1
      else:
        ratelimitVar7 = ratelimitVar7+rateLimit     
      await message.channel.edit(name="❕｜Support-7")   
   
   text = message.content
   text = text.lower()
   
   if message.content.startswith('!'):
     text = text.replace('!', '')
     if text == "ping":
        ping_embed=discord.Embed(
          title=f"{round(((round(client.latency, 4))*1000), 4)} ms",
          description='',
          color=0xaaffaa)
        await message.channel.send(embed=ping_embed)
     elif text == "help":
        await message.channel.send(embed=help_embed)  
     elif text == "close":
        if message.channel.id == support_1_id:
          if support_1_val == 1 and (message.author == support_1_msg.author or message.author.guild_permissions.administrator):
            current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
            if ratelimitVar1 >=0 and ratelimitVar1 < rateLimit and current_time >= 1440-rateLimit and current_time < 1440:
               current_time = -1
            if ratelimitVar1 <= current_time:
              await message.channel.send(embed=avai_embed)
              support_1_val = 0 
              try:
                await support_1_msg.unpin()
              except:
                return  
              await message.channel.edit(name="✅｜Support-1")
            else:
                 await message.channel.send(embed=locked_embed)
                 overwrite = message.channel.overwrites_for(message.guild.default_role)
                 overwrite.send_messages = False
                 await message.channel.set_permissions(message.guild.default_role, overwrite=overwrite)
                 #await message.channel.send('Channel locked.')    
                 lockedVar1 = 1
          elif support_1_val == 0:
              await message.channel.send(embed=re_close_embed)    
        elif message.channel.id == support_2_id:
          if support_2_val == 1 and (message.author == support_2_msg.author or message.author.guild_permissions.administrator):
            current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
            if ratelimitVar2 >=0 and ratelimitVar2 < rateLimit and current_time >= 1440-rateLimit and current_time < 1440:
               current_time = -1
            if ratelimitVar2 <= current_time:
              await message.channel.send(embed=avai_embed)
              support_2_val = 0
              try:
                await support_2_msg.unpin()
              except:
                return  
              await message.channel.edit(name="✅｜Support-2")   
            else:
                 await message.channel.send(embed=locked_embed)
                 overwrite = message.channel.overwrites_for(message.guild.default_role)
                 overwrite.send_messages = False
                 await message.channel.set_permissions(message.guild.default_role, overwrite=overwrite)    
                 lockedVar2 = 1
          elif support_2_val == 0:
              await message.channel.send(embed=re_close_embed)    
        elif message.channel.id == support_3_id:
          if support_3_val == 1 and (message.author == support_3_msg.author or message.author.guild_permissions.administrator):
            current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
            if ratelimitVar3 >=0 and ratelimitVar3 < rateLimit and current_time >= 1440-rateLimit and current_time < 1440:
               current_time = -1
            if ratelimitVar3 <= current_time:
              await message.channel.send(embed=avai_embed)
              support_3_val = 0
              try:
                await support_3_msg.unpin()
              except:
                return 
              await message.channel.edit(name="✅｜Support-3")  
            else:
                 await message.channel.send(embed=locked_embed)   
                 overwrite = message.channel.overwrites_for(message.guild.default_role)
                 overwrite.send_messages = False
                 await message.channel.set_permissions(message.guild.default_role, overwrite=overwrite)
                 lockedVar3 = 1;  
          elif support_3_val == 0:
              await message.channel.send(embed=re_close_embed)    
        elif message.channel.id == support_4_id:
          if support_4_val == 1 and (message.author == support_4_msg.author or message.author.guild_permissions.administrator):
            current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
            if ratelimitVar4 >=0 and ratelimitVar4 < rateLimit and current_time >= 1440-rateLimit and current_time < 1440:
               current_time = -1
            if ratelimitVar4 <= current_time:
              await message.channel.send(embed=avai_embed)
              support_4_val = 0
              try:
                await support_4_msg.unpin()
              except:
                return  
              await message.channel.edit(name="✅｜Support-4")   
            else:
                 await message.channel.send(embed=locked_embed)   
                 overwrite = message.channel.overwrites_for(message.guild.default_role)
                 overwrite.send_messages = False
                 await message.channel.set_permissions(message.guild.default_role, overwrite=overwrite) 
                 lockedVar4 = 1
          elif support_4_val == 0:
              await message.channel.send(embed=re_close_embed)    
        elif message.channel.id == support_5_id:
          if support_5_val == 1 and (message.author == support_5_msg.author or message.author.guild_permissions.administrator):
            current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
            if ratelimitVar5 >=0 and ratelimitVar5 < rateLimit and current_time >= 1440-rateLimit and current_time < 1440:
               current_time = -1
            if ratelimitVar5 <= current_time:
              await message.channel.send(embed=avai_embed)
              support_5_val = 0
              try:
                await support_5_msg.unpin()
              except:
                return  
              await message.channel.edit(name="✅｜Support-5")   
            else:
                 await message.channel.send(embed=locked_embed)  
                 overwrite = message.channel.overwrites_for(message.guild.default_role)
                 overwrite.send_messages = False
                 await message.channel.set_permissions(message.guild.default_role, overwrite=overwrite) 
                 lockedVar5 = 1
          elif support_5_val == 0:
              await message.channel.send(embed=re_close_embed)    
        elif message.channel.id == support_6_id:
          if support_6_val == 1 and (message.author == support_6_msg.author or message.author.guild_permissions.administrator):
            current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
            if ratelimitVar6 >=0 and ratelimitVar6 < rateLimit and current_time >= 1440-rateLimit and current_time < 1440:
               current_time = -1
            if ratelimitVar6 <= current_time:
              await message.channel.send(embed=avai_embed)
              support_6_val = 0
              try:
                await support_6_msg.unpin()
              except:
                return  
              await message.channel.edit(name="✅｜Support-6")   
            else:
                 await message.channel.send(embed=locked_embed)   
                 overwrite = message.channel.overwrites_for(message.guild.default_role)
                 overwrite.send_messages = False
                 await message.channel.set_permissions(message.guild.default_role, overwrite=overwrite) 
                 lockedVar6 = 1
          elif support_6_val == 0:
              await message.channel.send(embed=re_close_embed)    
        elif message.channel.id == support_7_id:
          if support_7_val == 1 and (message.author == support_7_msg.author or message.author.guild_permissions.administrator):
            current_time = int(str(str(datetime.now()).split(" ")[1]).split(":")[0])*60+int(str(str(datetime.now()).split(" ")[1]).split(":")[1])
            if ratelimitVar7 >=0 and ratelimitVar7 < rateLimit and current_time >= 1440-rateLimit and current_time < 1440:
               current_time = -1
            if ratelimitVar7 <= current_time:
              await message.channel.send(embed=avai_embed)
              support_7_val = 0
              try:
                await support_7_msg.unpin()
              except:
                return  
              await message.channel.edit(name="✅｜Support-7")   
            else:
                 await message.channel.send(embed=locked_embed) 
                 overwrite = message.channel.overwrites_for(message.guild.default_role)
                 overwrite.send_messages = False
                 await message.channel.set_permissions(message.guild.default_role, overwrite=overwrite)   
                 lockedVar7 = 1
          elif support_7_val == 0:
              await message.channel.send(embed=re_close_embed)  
     
client.run(os.getenv('TOKEN')) 