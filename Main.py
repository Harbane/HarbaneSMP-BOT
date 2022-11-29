import discord
from aiohttp import request
import random
from time import gmtime, strftime
from discord import app_commands
from discord.app_commands import Choice
from discord.ui import Button, View
from dotenv import load_dotenv
from os import getenv
import requests
import json
import pyautogui
from datetime import datetime
import asyncio
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

#------------------------------------
load_dotenv()

#-----------------------------------

class aclient(discord.Client):
      def __init__(self):
            intents = discord.Intents.default()
            intents.members = True
            super().__init__(intents=intents)
            self.synced = False

      async def on_ready(self):
            await self.wait_until_ready()
            if not self.synced:
                  await tree.sync(guild = discord.Object(id = '872660349793472512'))#guild = discord.Object(id = '872660349793472512')
                  self.synced = True
            print('------')
            print('Logged in as ' + client.user.name)
            print('------')
            await client.change_presence(activity=discord.Game(name='Harbane SMP'))

      async def on_member_join(self, member):
        guild = member.guild
        servers = 0
        for i in client.guilds:
            print(i)
            servers + 1
            print(servers)
        print(f'Bot is in #{servers}')
        if guild.system_channel is not None and guild == client.get_guild(872660349793472512):
            print(guild.system_channel)
            ids = member.mention[2:-1]
            user = client.get_user(int(ids))
            print(str(user) + ' has joined the server')
            members = 0
            for membered in guild.members:
                  print(membered)
                  members += 1
            oka = member.avatar.url
            print(oka)
            response = requests.get(oka)

            filed = open("avatar.png", "wb")
            filed.write(response.content)
            filed.close()
            #--------------------------------
            width = 1100
            height = 500
            #--------------------------------
            with Image.open(r'discord.py/Background/'+str(random.randint(1,6))+'.png') as card:
                  card = card.convert("RGBA")
            #--------------------------------
            profile_img = Image.open('avatar.png')
            newsize = (260, 260)
            img2 = profile_img.resize(newsize)
            #--------------------------------
            logo = Image.open('Icon1.png')
            logo_size = (100, 100)
            logo_image = logo.resize(logo_size)
            #--------------------------------
            img  = Image.new( mode = "RGBA", size = (width, height), color = (23, 24, 30, 12))
            text = f'{user}, has joined the server'
            text2 = f"Member #{members}"
            if len(text) >= 46:
              fnt = ImageFont.truetype('discord.py/OpenSans-Regular.ttf', 35)
            else:
              fnt = ImageFont.truetype('discord.py/OpenSans-Regular.ttf', 42)
            fnt2 = ImageFont.truetype('discord.py/OpenSans-Regular.ttf', 30)
            draw = ImageDraw.Draw(img)
            mask_im = Image.open('mask_circle.jpg').resize(img2.size).convert('L')
            # mask_logo = Image.open('mask_circle.jpg').resize(logo_image.size).convert('L')
            draw.rectangle((1048, 474, 48, 26), fill=(0, 0, 0, 150))
            draw.text((550,335),  text=text, font=fnt, anchor='mt',fill=(255, 255, 255))
            draw.text((550,390), text=text2, font=fnt2, anchor='mt',fill=('#A5A5A5'))
            img.paste(img2, (420,60), mask_im)
            out = Image.alpha_composite(card, img)
            out.save('card.png')

            to_send = f'{member.mention} has joined the server'
            file = discord.File('card.png', filename="card.png")

            await guild.system_channel.send(to_send, file=file)


      async def on_member_remove(self, member):
        guild = member.guild
        if guild.system_channel is not None and guild == client.get_guild(872660349793472512):
            channel = client.get_channel(872714456403173426)
            ids = member.mention[2:-1]
            user = client.get_user(int(ids))
            print(str(user) + ' has left the server')
            to_send = f'**{user}** has left the server'
            await channel.send(to_send)  # type: ignore
            
      async def on_message(self, message):
        #print(f'Message from {message.author}: {message.content}')
        if message.content.startswith('!stats'):
              print('weee')
      
      # async def on_message_delete(self, message):
      #   msg = f'{message.author} has deleted message'
      #   await message.channel.send(msg)


#-----------------------------------------------------------------------------------------------------------------------------
# def start():
#       await asyncio.sleep(140)
#       pyautogui.press('win')
#       await asyncio.sleep(2)
#       pyautogui.write('remote')
#       await asyncio.sleep(2)
#       pyautogui.press('enter')
#       await asyncio.sleep(2)
#       pyautogui.press('enter')

countDown = 30

client = aclient()
tree = app_commands.CommandTree(client)
#----------------------------------------------------------------------------------------------------------------------------
@tree.command(
      name = 'hello',
      description = "Says hello",
      guild = discord.Object(id = '872660349793472512')
      )
async def self(interaction: discord.Interaction):  # type: ignore
      print('hi')
      await interaction.response.send_message('hi')
#-----------------------------------------------------------------------------------------------------------------------------

@tree.command(
      name = 'vm',
      description = "Turn on and off Virtual Machine",
      guild = discord.Object(id = '872660349793472512')
      )
@app_commands.choices( option=[
            Choice(name="on", value="1"),
            Choice(name="deallocate", value="0"),
            Choice(name="restart", value="2"),
            Choice(name="power off (credits still get charged)", value="3"),
      ])
@app_commands.checks.has_any_role(
      1013053147427643483, 'console'
)#1013053147427643483
async def self(interaction: discord.Interaction, option: str):  # type: ignore
      global countDown

      button = Button(label= 'Dashboard', url='https://harbane.net/login', disabled=False)
      view = View()
      view.add_item(button)
      visable = False

      url_token = "https://login.microsoft.com/acd94547-7d52-432f-98dc-c8d6c842128d/oauth2/token"

      payload_token='grant_type='+getenv('GRANT_TYPE')+'&client_id='+getenv('CLIENT_ID')+'&client_secret='+getenv('CLIENT_SECRET')+'&resource=https%3A%2F%2Fmanagement.azure.com%2F'  # type: ignore
      headers_token = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'fpc=AnhYGHqywbdEuuR4lmAnhpO0BYEYAQAAAPmIuNoOAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'
      }

      package_token = requests.request("POST", url_token, headers=headers_token, data=payload_token)
      token_json = package_token.json()
      token = token_json['access_token']

      url = 'https://management.azure.com/subscriptions/' + getenv('SUBSCRIPTION') + '/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/instanceView?api-version=2022-03-01'
      headers = {
            'Authorization': 'Bearer ' + token,
            'content-type': 'text/plain',
      }
      responses = requests.get(url, headers=headers)

      print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: {str(responses)} api request')

      info = json.loads(responses.text)
      if info['statuses'][1]['displayStatus'] == 'VM running' or info['statuses'][1]['displayStatus'] == 'VM starting':
            if option == "1": # 1 is for on
                  em=discord.Embed(title="Virtual Machine is already running", description="", color=0xE93434)
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()
                  visable = True
                  print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: pc already on')
                  await interaction.response.send_message(embed=em, view=view, ephemeral = visable)

            elif option == "0": # 0 is for off
                  embed=discord.Embed(title="Deallocating Virtual Machine", description="current status - deallocating", color=0xE93434)
                  embed.set_footer(text="- harbane.net")
                  embed.timestamp = datetime.now()

                  em=discord.Embed(title="Virtual Machine stopped", description="", color=0x22cc00)
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()

                  print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: pc turning off')

                  #stops vm
                  stopURL = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/deallocate?api-version=2022-03-01'
                  headers = {
                      'Authorization': 'Bearer ' + token,
                      'content-type': 'text/plain',
                  }
                  stopVM = requests.post(stopURL, headers=headers)

                  print(str(stopVM) + ': vm Stopping')
                  await interaction.response.send_message(embed=embed, view=view, ephemeral = visable)

            elif option == "2": # 2, restarts
                  em=discord.Embed(title="Virtual Machine Restarting", description="", color=0xe06f19)
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()
                  visable = True
                  print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: pc restarting')
                  RestartURL = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/restart?api-version=2022-08-01'
                  headers = {
                      'Authorization': 'Bearer ' + token,
                      'content-type': 'text/plain',
                  }
                  RestartVM = requests.post(RestartURL, headers=headers)
                  print(str(RestartVM) + ': vm Restarting')
                  await interaction.response.send_message(embed=em, view=view, ephemeral = visable)

            elif option == "3": # 3, power off
                  em=discord.Embed(title="Virtual Machine Powering off", description="*note: credits are still being used unless it is deallocated", color=0x737373)
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()
                  visable = True
                  print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: pc restarting')
                  StopURL = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/powerOff?api-version=2022-08-01'
                  headers = {
                      'Authorization': 'Bearer ' + token,
                      'content-type': 'text/plain',
                  }
                  StopVM = requests.post(StopURL, headers=headers)
                  print(str(StopVM) + ': vm powering off')
                  await interaction.response.send_message(embed=em, view=view, ephemeral = visable)
                  #---------

      elif info['statuses'][1]['displayStatus'] == 'VM deallocated' or info['statuses'][1]['displayStatus'] == 'VM stopped':
            if option == "1": # 1 is for on
                  await interaction.response.defer(ephemeral=False)

                  em=discord.Embed(title="Virtual Machine turning on", description=f"Estimated time of start up 2 min\n \n**current status** - starting virtual machine", color=0x1ba300)
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()

                  embed=discord.Embed(title="Virtual Machine Online", description="**current status** - Turning SMP on", color=0x1ba300)
                  
                  embed2=discord.Embed(title="SMP is now online", description="**current status** - standby", color=0x1ba300)
                  
                  print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: starting pc')

                  #starts vm
                  startURL = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/start?api-version=2022-03-01'
                  headers = {
                      'Authorization': 'Bearer ' + token,
                      'content-type': 'text/plain',
                  }
                  startVM = requests.post(startURL, headers=headers)
                  print(str(startVM) + ': vm starting')
                  await interaction.followup.send(embed=em, view=view, ephemeral = visable)
                  pyautogui.press('enter')
                  await asyncio.sleep(100)
                  pyautogui.press('win')
                  await asyncio.sleep(2)
                  pyautogui.write('remote')
                  await asyncio.sleep(2)
                  pyautogui.press('enter')
                  await asyncio.sleep(2)
                  pyautogui.press('enter')
                  await asyncio.sleep(1)
                  await interaction.followup.send(embed=embed, ephemeral = visable)
                  await asyncio.sleep(140)
                  IsComplete = False
                  check_url = "http://play.harbane.net:25560/api/v1/servers/0434a83d-764e-481f-a01c-074c5a06d7be?filter=2"

                  check_header = {
                        'apikey': getenv('KEY'),
                  }
                  while IsComplete == False:
                        async with request("GET", check_url, headers=check_header) as response:
                              status = await response.json()
                        print(status['status'])
                        await asyncio.sleep(5)
                        if status['status'] == 1:
                              print('activated')
                              await interaction.followup.send(embed=embed2, ephemeral = visable)
                              IsComplete = True
                              break

            else:
                  em=discord.Embed(title="Virtual Machine Currently Deallocated", description="", color=0x737373)
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()
                  visable = False
                  print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: pc already off')

                  await interaction.response.send_message(embed=em, view=view, ephemeral = visable)
      elif info['statuses'][1]['displayStatus'] == 'VM deallocating' or info['statuses'][1]['displayStatus'] == 'VM stopping':
            em=discord.Embed(title="Virtual Machine is currently being deallocated", description="Please wait for the virtual machine to completly deallocate before using the command", color=0x737373)
            em.set_footer(text="- harbane.net")
            em.timestamp = datetime.now()
            visable = False
            
            await interaction.response.send_message(embed=em, view=view, ephemeral = visable)
#-----------------------------------------------------------------------------------------------------------------------------
@tree.command(
      name = 'info',
      description = "Shows info of Harbane SMP",
      guild = discord.Object(id = '872660349793472512')
)
@app_commands.choices( list=[
            Choice(name="VM", value="VM"),
            Choice(name="SMP", value="SMP"),
            Choice(name="PvP server", value="PVP server"),
            Choice(name="Free world", value="FREE world"),
            Choice(name="Creative World", value="Creative World"),
      ])
async def self(interaction: discord.Interaction, list: str):
      button = Button(label= 'Dashboard', url='https://harbane.net/login', disabled=False)
      view = View()
      view.add_item(button)

      url_token = "https://login.microsoft.com/acd94547-7d52-432f-98dc-c8d6c842128d/oauth2/token"

      payload_token='grant_type='+getenv('GRANT_TYPE')+'&client_id='+getenv('CLIENT_ID')+'&client_secret='+getenv('CLIENT_SECRET')+'&resource=https%3A%2F%2Fmanagement.azure.com%2F'
      headers_token = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'fpc=AnhYGHqywbdEuuR4lmAnhpO0BYEYAQAAAPmIuNoOAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'
      }

      package_token = requests.request("POST", url_token, headers=headers_token, data=payload_token)
      token_json = package_token.json()
      token = token_json['access_token']


      ###############################################
      url = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/instanceView?api-version=2022-03-01'
      headers = {
                'Authorization': 'Bearer ' + token,
                'content-type': 'text/plain',}
      responses = requests.get(url, headers=headers)
      print('done1')
      infos = json.loads(responses.text)
      if infos['statuses'][1]['displayStatus'] != 'VM running':
            em=discord.Embed(title="Virtual Machine is currently deallocated", description="", color=0x737373)
            em.set_footer(text="- harbane.net")
            em.timestamp = datetime.now()
            print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: status, VM deallocated')
            await interaction.response.send_message(embed=em)
      elif infos['statuses'][1]['displayStatus'] == 'VM running':
            await interaction.response.defer(ephemeral=False)
            if list == "SMP":
                  url_smp = "http://play.harbane.net:25560/api/v1/servers/"+getenv('SMP')

                  headers_smp = {
                    'apikey': getenv('KEY'),
                    'Content-Type': 'application/json'
                  }

                  response = requests.request("GET", url_smp, headers=headers_smp)
                  info = json.loads(response.text)
                  print(info['status'])

                  if info['status'] == 1:
                        status = 'online'
                  elif info['status'] == 0:
                        status = 'offline'
                  elif info['status'] == 3:
                        status = 'killing'
                  elif info['status'] == 4:
                        status = 'restarting'
                  em=discord.Embed(title="Server Information", description="", color=0x1ba300)
                  em.add_field(name="Server name", value=f"```{info['name']}```")
                  em.add_field(name="Server Status", value=f"```{status}```", inline=True)
                  em.add_field(name="Description", value=f"```{info['description']}```", inline=False)
                  em.add_field(name="Allocated Memory", value=f"```{info['javaAllocatedMemory']} MB```", inline=True)
                  em.add_field(name="Set To Auto Start", value=f"```{info['isSetToAutoStart']}```", inline=True)
                  em.add_field(name="guid", value=f"```{info['guid']}             ```", inline=False)
                  em.add_field(name='Path To Folder', value=f"```{info['pathToFolder']}```", inline=False)
                  em.add_field(name='Folder name', value=f"```{info['folderName']}```", inline=True)
                  em.add_field(name="Server IP", value=f"```play.harbane.net```", inline=True)
                  em.set_thumbnail(url='https://harbane.net/Images/server-icon5.png')
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()

            elif list == 'PVP server':
                  url_pvp = "http://play.harbane.net:25560/api/v1/servers/"+getenv('PVP')

                  headers_pvp = {
                    'apikey': getenv('KEY'),
                    'Content-Type': 'application/json'
                  }

                  response = requests.request("GET", url_pvp, headers=headers_pvp)
                  info = json.loads(response.text)
                  print(info['status'])

                  if info['status'] == 1:
                        status = 'online'
                  elif info['status'] == 0:
                        status = 'offline'
                  elif info['status'] == 3:
                        status = 'killing'
                  elif info['status'] == 4:
                        status = 'restarting'

                  em=discord.Embed(title="Server Information", description="", color=0x1ba300)
                  em.add_field(name="Server name", value=f"```{info['name']}```")
                  em.add_field(name="Server Status", value=f"```{status}```", inline=True)
                  em.add_field(name="Description", value=f"```{info['description']}```", inline=False)
                  em.add_field(name="Allocated Memory", value=f"```{info['javaAllocatedMemory']} MB```", inline=True)
                  em.add_field(name="Set To Auto Start", value=f"```{info['isSetToAutoStart']}```", inline=True)
                  em.add_field(name="guid", value=f"```{info['guid']}             ```", inline=False)
                  em.add_field(name='Path To Folder', value=f"```{info['pathToFolder']}```", inline=False)
                  em.add_field(name='Folder name', value=f"```{info['folderName']}```", inline=True)
                  em.add_field(name="Server IP", value=f"```pvp.harbane.net```", inline=True)
                  em.set_thumbnail(url='https://harbane.net/Images/pvpserver-icon.png')
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()
            elif list == 'FREE world':
                  url_pvp = "http://play.harbane.net:25560/api/v1/servers/"+getenv('FREE')

                  headers_pvp = {
                    'apikey': getenv('KEY'),
                    'Content-Type': 'application/json'
                  }

                  response = requests.request("GET", url_pvp, headers=headers_pvp)
                  info = json.loads(response.text)
                  print(info['status'])

                  if info['status'] == 1:
                        status = 'online'
                  elif info['status'] == 0:
                        status = 'offline'
                  elif info['status'] == 3:
                        status = 'killing'
                  elif info['status'] == 4:
                        status = 'restarting'

                  em=discord.Embed(title="Server Information", description="", color=0x1ba300)
                  em.add_field(name="Server name", value=f"```{info['name']}```")
                  em.add_field(name="Server Status", value=f"```{status}```", inline=True)
                  em.add_field(name="Description", value=f"```{info['description']}```", inline=False)
                  em.add_field(name="Allocated Memory", value=f"```{info['javaAllocatedMemory']} MB```", inline=True)
                  em.add_field(name="Set To Auto Start", value=f"```{info['isSetToAutoStart']}```", inline=True)
                  em.add_field(name="guid", value=f"```{info['guid']}             ```", inline=False)
                  em.add_field(name='Path To Folder', value=f"```{info['pathToFolder']}```", inline=False)
                  em.add_field(name='Folder name', value=f"```{info['folderName']}```", inline=True)
                  em.add_field(name="Server IP", value=f"```fun.harbane.net```", inline=True)
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()

            elif list == 'Creative World':
                  url_pvp = "http://play.harbane.net:25560/api/v1/servers/"+getenv('CREATIVE')

                  headers_pvp = {
                    'apikey': getenv('KEY'),
                    'Content-Type': 'application/json'
                  }

                  response = requests.request("GET", url_pvp, headers=headers_pvp)
                  info = json.loads(response.text)
                  print(info['status'])

                  if info['status'] == 1:
                        status = 'online'
                  elif info['status'] == 0:
                        status = 'offline'
                  elif info['status'] == 3:
                        status = 'killing'
                  elif info['status'] == 4:
                        status = 'restarting'

                  em=discord.Embed(title="Server Information", description="", color=0x1ba300)
                  em.add_field(name="Server name", value=f"```{info['name']}```")
                  em.add_field(name="Server Status", value=f"```{status}```", inline=True)
                  em.add_field(name="Description", value=f"```{info['description']}```", inline=False)
                  em.add_field(name="Allocated Memory", value=f"```{info['javaAllocatedMemory']} MB```", inline=True)
                  em.add_field(name="Set To Auto Start", value=f"```{info['isSetToAutoStart']}```", inline=True)
                  em.add_field(name="guid", value=f"```{info['guid']}             ```", inline=False)
                  em.add_field(name='Path To Folder', value=f"```{info['pathToFolder']}```", inline=False)
                  em.add_field(name='Folder name', value=f"```{info['folderName']}```", inline=True)
                  em.add_field(name="Server IP", value=f"```fun.harbane.net```", inline=True)
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()


            elif list == 'VM':
                  em=discord.Embed(title="VM Info", description="", color=0x1ba300)
                  em.add_field(name='Computer', value=f"```{infos['computerName']}```", inline=True)
                  em.add_field(name='os Version', value=f"```{infos['osVersion']}```", inline=True)
                  em.add_field(name='os Name', value=f"```{infos['osName']}```", inline=False)
                  em.add_field(name='Time', value=f"```{infos['statuses'][0]['time']}```", inline=False)
                  em.add_field(name='Hyper-V Generation', value=f"```{infos['hyperVGeneration']}```", inline=True)
                  em.add_field(name='Status', value=f"```{infos['statuses'][1]['displayStatus']}```", inline=True)
                  em.add_field(name='Code', value=f"```{infos['statuses'][1]['code']}```", inline=False)
                  em.add_field(name='Disk', value=f"```{infos['disks'][0]['name']}```", inline=False)
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()
                  print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: status, VM info')
            await asyncio.sleep(5)
            await interaction.followup.send(embed=em, view=view)
      else:
            em=discord.Embed(title="Error", description="request failed, **try again** in abit", color=0x1ba300)
            em.set_footer(text='harbane.net')
            await interaction.response.send_message(embed=em)
      ###############################################



#-----------------------------------------------------------------------------------------------------------------------------
@tree.command(
      name = 'logs',
      description = "Get SMP console logs",
      guild = discord.Object(id = '872660349793472512')
)
@app_commands.choices( list=[
            Choice(name="smp", value="0434a83d-764e-481f-a01c-074c5a06d7be"),
            Choice(name="pvp server", value="08d1d3d5-a182-4476-9fcf-69cfcee71119"),
            Choice(name="free world", value="0967e29f-1354-4760-aee3-399140ee8846"),
            Choice(name="Creative World", value="756fee89-2e37-4142-a7bd-fc3ad3852234"),
      ])
async def self(interaction: discord.Interaction, list: str, lines: int):

      url_token = "https://login.microsoft.com/acd94547-7d52-432f-98dc-c8d6c842128d/oauth2/token"

      payload_token='grant_type='+getenv('GRANT_TYPE')+'&client_id='+getenv('CLIENT_ID')+'&client_secret='+getenv('CLIENT_SECRET')+'&resource=https%3A%2F%2Fmanagement.azure.com%2F'
      headers_token = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'fpc=AnhYGHqywbdEuuR4lmAnhpO0BYEYAQAAAPmIuNoOAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'
      }

      package_token = requests.request("POST", url_token, headers=headers_token, data=payload_token)
      token_json = package_token.json()
      token = token_json['access_token']

      url = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/instanceView?api-version=2022-03-01'
      headers = {
                'Authorization': 'Bearer ' + token,
                'content-type': 'text/plain',}
      responses = requests.get(url, headers=headers)
      infos = json.loads(responses.text)
      if infos['statuses'][1]['displayStatus'] != 'VM running':
            em=discord.Embed(title="Virtual Machine is currently deallocated", description="To turn on Virtual Machine use **/vm**", color=0xE93434)
            em.set_footer(text="- harbane.net")
            em.timestamp = datetime.now()
            print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: logs, VM deallocated')
            await interaction.response.send_message(embed=em, ephemeral=True)
      elif infos['statuses'][1]['displayStatus'] == 'VM running':
            url = 'http://play.harbane.net:25560/api/v1/servers/'+str(list)+'/console?AmountOfLines='+str(lines)+'&Reversed=true&takeFromBeginning=false'
            headers = {
                      'apikey': getenv('KEY'), }
            response = requests.get(url, headers=headers)
            await interaction.response.defer(ephemeral=False)
            await asyncio.sleep(3.5)
            print(str(response) + ' api request, (logs lines = ' + str(lines) +')')

            info = json.loads(response.text)
            with open('discord.py/file.txt', 'w') as f:
                          for line in info:
                            f.write(line)
                            f.write('\n')
            file = discord.File('discord.py/file.txt', filename = 'logs.txt')
            await interaction.followup.send(f'here you go, [{lines} lines requested]', file=file)
#-----------------------------------------------------------------------------------------------------------------------------
@tree.command(
      name = 'server',
      description = "Turn on and off servers",
      guild = discord.Object(id = '872660349793472512')
      )
@app_commands.choices( serverlist=[
            Choice(name="SMP", value="0434a83d-764e-481f-a01c-074c5a06d7be"),
            Choice(name="PvP server", value="08d1d3d5-a182-4476-9fcf-69cfcee71119"),
            Choice(name="Free world", value="0967e29f-1354-4760-aee3-399140ee8846"),
            Choice(name="Creative World", value="756fee89-2e37-4142-a7bd-fc3ad3852234")
      ])
@app_commands.choices( option=[
            Choice(name="start", value="2"),
            Choice(name="stop", value="1",),
            Choice(name="kill", value="3"),
            Choice(name="restart", value="4"),
      ])
@app_commands.checks.has_any_role(
      1013053147427643483, 'console'
)#1013053147427643483
async def self(interaction: discord.Interaction, serverlist: str, option: str):
      global action, finished, colour

      url_token = "https://login.microsoft.com/acd94547-7d52-432f-98dc-c8d6c842128d/oauth2/token"

      payload_token='grant_type='+getenv('GRANT_TYPE')+'&client_id='+getenv('CLIENT_ID')+'&client_secret='+getenv('CLIENT_SECRET')+'&resource=https%3A%2F%2Fmanagement.azure.com%2F'
      headers_token = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'fpc=AnhYGHqywbdEuuR4lmAnhpO0BYEYAQAAAPmIuNoOAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'
      }

      package_token = requests.request("POST", url_token, headers=headers_token, data=payload_token)
      token_json = package_token.json()
      token = token_json['access_token']

      url = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/instanceView?api-version=2022-03-01'
      headers = {
                'Authorization': 'Bearer ' + token,
                'content-type': 'text/plain',}
      package = requests.get(url, headers=headers)
      info = json.loads(package.text)

      if info['statuses'][1]['displayStatus'] != 'VM running':
            em=discord.Embed(title="Virtual Machine is currently deallocated", description="To turn on Virtual Machine use **/vm**", color=0xE93434)
            em.set_footer(text="- harbane.net")
            em.timestamp = datetime.now()
            print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: server, VM deallocated')
            await interaction.response.send_message(embed=em, ephemeral=True)

      elif info['statuses'][1]['displayStatus'] == 'VM running':
            await interaction.response.defer(ephemeral=False)

            if serverlist == '0434a83d-764e-481f-a01c-074c5a06d7be':
                  server = 'SMP'
            elif serverlist == '08d1d3d5-a182-4476-9fcf-69cfcee71119':
                  server = 'PvP Server'
            elif serverlist == '0967e29f-1354-4760-aee3-399140ee8846':
                  server = 'Free World'
            elif serverlist == '756fee89-2e37-4142-a7bd-fc3ad3852234':
                  server = 'Creative World'

            if option == '1':
                  action = 'stopping'
                  finished = ' is now offline'
                  colour = 0xE93434
                  stat = 'already offline'
            elif option == '2':
                  action = 'starting up'
                  finished = ' is now online'
                  colour = 0x1ba300
                  stat = 'already online'
            elif option == '3':
                  action = 'being killed'
                  finished = ' has successfully been killed'
                  colour = 0x737373
                  stat = 'not online'
            elif option == '4':
                  action = 'restarting'
                  finished = ' has successfully resatarted'
                  colour = 0xe06f19
                  stat = 'not online'

            status_url = "http://play.harbane.net:25560/api/v1/servers/"+serverlist
            headers = {
                  'apikey': getenv('KEY')
            }
            status_check = requests.request("GET", status_url, headers=headers)
            status = json.loads(status_check.text)
            print(status['status'])#int
            print(option)#str

            def approve(val1 = int(option), val2 = int(status['status'])):
                  if val1 == 1 and val2 == 0:
                        return False
                  elif val1 == 2 and val2 == 1:
                        return False
                  elif val1 == 3 and val2 != 1:
                        return False
                  elif val1 == 4 and val2 != 1:
                        return False
                  else:
                        print('option = '+ str(option))
                        print('status = ' + str(status['status']))
                        return True

            if approve(int(option), status['status']) == False:
                  print('Confirmed')
                  em = discord.Embed(title=server + ' is ' + stat, description='Please choose another option', color=0xE93434)
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()
                  await interaction.followup.send(embed=em)
            elif approve(int(option), status['status']) == True:
                  print('excuting order 66')
                  url = "http://play.harbane.net:25560/api/v1/servers/"+serverlist+"/execute/action"

                  em=discord.Embed(title=server, description=server + ' is now '+ action, color=colour)
                  em.set_footer(text="-harbane.net")
                  em.timestamp = datetime.now()

                  embed=discord.Embed(title=server+finished, description='', color=colour)
                  embed.set_footer(text="-harbane.net")
                  embed.timestamp = datetime.now()

                  payload = json.dumps({
                          "Guid": serverlist,
                          "Action": option,
                        })
                  headers = {
                          'apikey': getenv('KEY'),
                          'action': option,
                          'Content-Type': 'application/json'
                  }

                  response = requests.request("POST", url, headers=headers, data=payload)
                  await asyncio.sleep(2)
                  print(f'[{response}] api request, SMP option {option}')

                  button = Button(label= 'Dashboard', url='https://harbane.net/login', disabled=False)
                  view = View()
                  view.add_item(button)

                  await interaction.followup.send(embed=em, view=view)

                  IsComplete = False
                  check_url = "http://play.harbane.net:25560/api/v1/servers/"+serverlist+"?filter=2"

                  check_header = {
                        'apikey': getenv('KEY'),
                  }
                  while IsComplete == False:
                        async with request("GET", check_url, headers=check_header) as response:
                              status = await response.json()
                        await asyncio.sleep(3)
                        print(status['status'])
                        if option == '2' and status['status'] == 1 or option == '1' and status['status'] == 0 or option == '4' and status['status'] == 1 or option == '3' and status['status'] == 0:
                              print('activated')
                              await interaction.followup.send(embed=embed, view=view)
                              IsComplete = True
                              break
                  
#-----------------------------------------------------------------------------------------------------------------------------
@tree.command(
      name = 'whitelist',
      description = "Whitelist someone to Harbane SMP",
      guild = discord.Object(id = '872660349793472512')
      )
@app_commands.choices( serverlist=[
            Choice(name="SMP", value="0434a83d-764e-481f-a01c-074c5a06d7be"),
            Choice(name="PvP server", value="08d1d3d5-a182-4476-9fcf-69cfcee71119"),
            Choice(name="free world", value="0967e29f-1354-4760-aee3-399140ee8846"),
            Choice(name="Creative World", value="756fee89-2e37-4142-a7bd-fc3ad3852234"),
      ])
@app_commands.choices( option=[
            Choice(name="add", value="add"),
            Choice(name="remove", value="remove"),
      ])
@app_commands.checks.has_any_role(
      1013053147427643483, 'console'
)#1013053147427643483
async def self(interaction: discord.Interaction, serverlist: str, option: str, user: str):
      await interaction.response.defer(ephemeral=False)
      
      url_token = "https://login.microsoft.com/acd94547-7d52-432f-98dc-c8d6c842128d/oauth2/token"

      payload_token='grant_type='+getenv('GRANT_TYPE')+'&client_id='+getenv('CLIENT_ID')+'&client_secret='+getenv('CLIENT_SECRET')+'&resource=https%3A%2F%2Fmanagement.azure.com%2F'
      headers_token = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'fpc=AnhYGHqywbdEuuR4lmAnhpO0BYEYAQAAAPmIuNoOAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'
      }

      package_token = requests.request("POST", url_token, headers=headers_token, data=payload_token)
      token_json = package_token.json()
      token = token_json['access_token']

      url = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/instanceView?api-version=2022-03-01'
      headers = {
                'Authorization': 'Bearer ' + token,
                'content-type': 'text/plain',}
      responses = requests.get(url, headers=headers)
      info = json.loads(responses.text)
      if info['statuses'][1]['displayStatus'] != 'VM running':
            em=discord.Embed(title="Virtual Machine is currently deallocated", description="To turn on Virtual Machine use **/vm**", color=0xE93434)
            em.set_footer(text="- harbane.net")
            em.timestamp = datetime.now()
            print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: whitelist, VM deallocated')
            await interaction.response.send_message(embed=em, ephemeral=True)

      elif info['statuses'][1]['displayStatus'] == 'VM running':
            if serverlist == '0434a83d-764e-481f-a01c-074c5a06d7be':
                  server = 'SMP'
            elif serverlist == '08d1d3d5-a182-4476-9fcf-69cfcee71119':
                  server = 'PVP server'
            elif serverlist == '0967e29f-1354-4760-aee3-399140ee8846':
                  server = 'Free world'
            elif serverlist == '756fee89-2e37-4142-a7bd-fc3ad3852234':
                  server = 'Creative world'
                  
            url = "http://play.harbane.net:25560/api/v1/servers/"+serverlist+"/execute/command"

            payload = json.dumps({
              "Guid": serverlist,
              "command": 'whitelist ' + option + ' ' + user
            })
            headers = {
              'apikey': getenv('KEY'),
              'command': 'whitelist ' + option + ' ' + user,
              'Content-Type': 'application/json'}
            async with request("POST", url, headers=headers, data=payload) as response:
                  pass
            
            print(f'{response} api request, whitelist {option} {user}')
            em=discord.Embed(title=f"Whitelist - {server}", description=option + "ed " + user + ' to whitelist', color=0x1ba300)
            em.set_footer(text="harbane.net")
            em.timestamp = datetime.now()
            button = Button(label= 'Dashboard', url='https://harbane.net/login', disabled=False)
            view = View()
            view.add_item(button)

            await interaction.followup.send(embed=em, view=view)

@tree.command(
      name = 'metrics',
      description = "request server metrics",
      guild = discord.Object(id = '872660349793472512')
      )
@app_commands.choices( option=[
            Choice(name="cpu", value="CPU"),
            Choice(name="ram", value="RAM"),
])
async def self(interaction: discord.Interaction, option:str):

      url_token = "https://login.microsoft.com/acd94547-7d52-432f-98dc-c8d6c842128d/oauth2/token"

      payload_token='grant_type='+getenv('GRANT_TYPE')+'&client_id='+getenv('CLIENT_ID')+'&client_secret='+getenv('CLIENT_SECRET')+'&resource=https%3A%2F%2Fmanagement.azure.com%2F'
      headers_token = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'fpc=AnhYGHqywbdEuuR4lmAnhpO0BYEYAQAAAPmIuNoOAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'
      }

      package_token = requests.request("POST", url_token, headers=headers_token, data=payload_token)
      token_json = package_token.json()
      token = token_json['access_token']

      url = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/instanceView?api-version=2022-03-01'
      headers = {
                'Authorization': 'Bearer ' + token,
                'content-type': 'text/plain',}
      responses = requests.get(url, headers=headers)
      info = json.loads(responses.text)
      if info['statuses'][1]['displayStatus'] != 'VM running':
            em=discord.Embed(title="Virtual Machine is currently deallocated", description="To turn on Virtual Machine use **/vm**", color=0xE93434)
            em.set_footer(text="- harbane.net")
            print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: metrics, VM deallocated')
            await interaction.response.send_message(embed=em, ephemeral=True)
      elif info['statuses'][1]['displayStatus'] == 'VM running':
            if option == 'CPU':
                  url = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/providers/microsoft.insights/metrics?api-version=2018-01-01&metricnames=Percentage%20CPU'
                  headers = {
                              'Authorization': 'Bearer ' + token,
                              'content-type': 'text/plain',}
                  responses = requests.get(url, headers=headers)
                  info = json.loads(responses.text)
                  infos = info['value'][0]['timeseries'][0]['data']
                  a = []
                  b = []
                  for xy in infos[29:60]:
                    if len(xy) == 2:
                      b.append(int(xy['average']))
                      a.append(xy["timeStamp"][11:16])

                  fig, ax = plt.subplots(num=None, figsize=(30, 12), dpi=100, facecolor='w', edgecolor='k')
                  ax.set_facecolor("#2f3136")#15171A
                  #to change the border color around the back
                  fig.patch.set_facecolor('#2f3136')
                  x = a
                  y = b
                  # plotting the points
                  plt.plot(x, y, color='#FFFFFF', linewidth=5)#007AF5
                  plt.title('Harbane VM cpu metrics', fontsize=50, color='white')
                  plt.xlabel('Time (UTC)', fontsize=22)
                  plt.ylabel('Average (%)', fontsize=22)
                  ax.spines['right'].set_color('#2f3136')
                  ax.spines['top'].set_color('#2f3136')
                  ax.spines['left'].set_color('#FFFFFF')
                  ax.spines['bottom'].set_color('#FFFFFF')
                  ax.xaxis.label.set_color('white')
                  ax.yaxis.label.set_color('white')
                  ax.tick_params(axis='x', colors='#FFFFFF', labelsize=15, size=20)
                  ax.tick_params(axis='y', colors='#FFFFFF', labelsize=15, size=10)
                  # function to show the plot
                  plt.tight_layout(pad=2)
                  plt.savefig('discord.py/graph1.png')
                  #plt.show()
                  await interaction.response.defer(ephemeral=False)
                  await asyncio.sleep(2)
                  file = discord.File('discord.py/graph1.png', filename="image.png")
                  em=discord.Embed(title="Virtual Machine Cpu Metrics (Average)", description="Showing metrics for the last 30 minutes", color=0x1ba300)
                  # em.set_thumbnail(url="https://harbane.net/Images/server-icon5.png")
                  em.set_image(url='attachment://image.png')
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()
                  await interaction.followup.send(file=file, embed=em)
            elif option == "RAM":
                  url = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/providers/microsoft.insights/metrics?api-version=2018-01-01&metricnames=Percentage%20CPU'
                  headers = {
                              'Authorization': 'Bearer ' + token,
                              'content-type': 'text/plain',}
                  responses = requests.get(url, headers=headers)
                  info = json.loads(responses.text)
                  infos = info['value'][0]['timeseries'][0]['data']
                  a = []
                  b = []
                  for xy in infos[25:59]:
                        b.append(int(xy['average']))
                        a.append(xy["timeStamp"][11:16])
                  fig, ax = plt.subplots(num=None, figsize=(30, 10), dpi=38, facecolor='w', edgecolor='k')
                  ax.set_facecolor("#1e2124")#15171A
                  #to change the border color around the back
                  fig.patch.set_facecolor('#1e2124')
                  x = a
                  y = b
                  # plotting the points
                  plt.plot(x, y, color='#0642D4', linewidth=5, linestyle='--')#007AF5
                  plt.title('Harbane VM cpu metrics', fontsize=25, color='white')

                  plt.xlabel('Time (UTC)', fontsize=20)
                  plt.ylabel('Average (%)', fontsize=20)

                  ax.spines['right'].set_color('#1e2124')
                  ax.spines['top'].set_color('#1e2124')
                  ax.spines['left'].set_color('#FFFFFF')
                  ax.spines['bottom'].set_color('#FFFFFF')
                  ax.xaxis.label.set_color('white')
                  ax.yaxis.label.set_color('white')
                  ax.tick_params(axis='x', colors='#FFFFFF', labelsize=15, size=20)
                  ax.tick_params(axis='y', colors='#FFFFFF', labelsize=30, size=10)

                  # function to show the plot
                  plt.tight_layout()
                  plt.savefig('discord.py/graph1.png')
                  #plt.show()
                  file = discord.File('discord.py/graph1.png', filename="image.png")
                  em=discord.Embed(title="Harbane Metrics", description="Virtual Machine metrics", color=0x1ba300)
                  # em.set_thumbnail(url="https://harbane.net/Images/server-icon5.png")
                  em.set_image(url='attachment://image.png')
                  em.add_field(name="VM ram", value="*Showing ram metrics for the last 35 minutes*", inline=True)
                  em.set_footer(text="- harbane.net")
                  await interaction.response.send_message(file=file, embed=em)



@tree.command(
      name = 'tps',
      description = "Shows server tps (ticks per second)",
      guild = discord.Object(id = '872660349793472512')
)
@app_commands.choices( serverlist=[
            Choice(name="SMP", value="0434a83d-764e-481f-a01c-074c5a06d7be"),
            Choice(name="PvP server", value="08d1d3d5-a182-4476-9fcf-69cfcee71119"),
            Choice(name="Free world", value="0967e29f-1354-4760-aee3-399140ee8846"),
            Choice(name="Creative World", value="756fee89-2e37-4142-a7bd-fc3ad3852234")
])
async def self(interaction: discord.Interaction, serverlist: str):
      url_token = "https://login.microsoft.com/acd94547-7d52-432f-98dc-c8d6c842128d/oauth2/token"
      payload_token='grant_type='+getenv('GRANT_TYPE')+'&client_id='+getenv('CLIENT_ID')+'&client_secret='+getenv('CLIENT_SECRET')+'&resource=https%3A%2F%2Fmanagement.azure.com%2F'
      headers_token = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'fpc=AnhYGHqywbdEuuR4lmAnhpO0BYEYAQAAAPmIuNoOAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'
      }

      package_token = requests.request("POST", url_token, headers=headers_token, data=payload_token)
      token_json = package_token.json()
      token = token_json['access_token']

      url = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/instanceView?api-version=2022-03-01'
      headers = {
                'Authorization': 'Bearer ' + token,
                'content-type': 'text/plain',}
      responses = requests.get(url, headers=headers)
      info = json.loads(responses.text)
      if info['statuses'][1]['displayStatus'] != 'VM running':
            em=discord.Embed(title="Virtual Machine is currently deallocated", description="To turn on Virtual Machine use **/vm**", color=0xE93434)
            em.set_footer(text="- harbane.net")
            em.timestamp = datetime.now()
            await interaction.response.send_message(embed=em, ephemeral=True)
            print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: tps, VM deallocated')
            await interaction.response.send_message(embed=em, ephemeral=False)
      elif info['statuses'][1]['displayStatus'] == 'VM running':
            if serverlist == '0434a83d-764e-481f-a01c-074c5a06d7be':
                  server = 'SMP'
            elif serverlist == '08d1d3d5-a182-4476-9fcf-69cfcee71119':
                  server = 'PVP server'
            elif serverlist == '0967e29f-1354-4760-aee3-399140ee8846':
                  server = 'Free world'
            elif serverlist == '756fee89-2e37-4142-a7bd-fc3ad3852234':
                  server = 'Creative world'

            await interaction.response.defer(ephemeral=False)
            status_url = "http://play.harbane.net:25560/api/v1/servers/"+serverlist
            headers = {
                  'apikey': getenv('KEY')
            }

            status_check = requests.request("GET", status_url, headers=headers)
            status = json.loads(status_check.text)
            if status['status'] != 1:
                  em = discord.Embed(title=server + ' is not online', description='Please choose another server that is online', color=0xE93434)
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()
                  await interaction.followup.send(embed=em)
            elif status['status'] == 1:
                  url = "http://play.harbane.net:25560/api/v1/servers/"+serverlist+"/execute/command"
                  payload = json.dumps({
                    "Guid": serverlist,
                    "Command": "tps"
                  })
                  headers = {
                    'apikey': getenv('KEY'),
                    'command': 'tps',
                    'Content-Type': 'application/json'
                  }
                  async with request("POST", url, headers=headers, data=payload) as response:
                        print(response.status)
                        if response.status == 200:
                              urled = "http://play.harbane.net:25560/api/v1/servers/"+serverlist+"/console?AmountOfLines=5&Reversed=true&takeFromBeginning=false"
                              headered = {
                                'apikey': getenv('KEY')
                              }
                              async with request("GET", urled, headers=headered) as responsed:
                                    if response.status == 200:
                                          weee = await responsed.json()
                                          for line in reversed(weee):
                                                if line[17:20] == 'TPS':
                                                      tps = line
                                                      break
                                          print(tps)
                                          print(tps[44:46])
                                          if tps[45:46] == '.':
                                                if int(tps[44:45]) >= 19:
                                                      colour = 0x1ba300
                                                elif int(tps[44:45]) >= 15:
                                                      colour = 0xe06f19
                                                elif int(tps[44:45]) >= 0:
                                                      colour = 0xE93434
                                                      print(colour)
                                                print(tps[44:45])
                                          else:
                                                if int(tps[44:46]) >= 19:
                                                  colour = 0x1ba300
                                                elif int(tps[44:46]) >= 15:
                                                      colour = 0xe06f19
                                                elif int(tps[44:46]) >= 0:
                                                      colour = 0xE93434
                                          em = discord.Embed(title=server + ' TPS', description=tps[17:], color=colour)

                                          await interaction.followup.send(embed=em)

@tree.command(
      name = 'status',
      description = "Status of all harbane servers",
      guild = discord.Object(id = '872660349793472512')
)
@app_commands.choices( option=[
            Choice(name="minimum (fast)", value="minimum"),
            Choice(name="all (slow)", value="all"),
])
async def self(interaction: discord.Interaction, option: str):
      await interaction.response.defer(ephemeral=False)
      url_token = "https://login.microsoft.com/acd94547-7d52-432f-98dc-c8d6c842128d/oauth2/token"
      payload_token='grant_type='+getenv('GRANT_TYPE')+'&client_id='+getenv('CLIENT_ID')+'&client_secret='+getenv('CLIENT_SECRET')+'&resource=https%3A%2F%2Fmanagement.azure.com%2F'
      headers_token = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'fpc=AnhYGHqywbdEuuR4lmAnhpO0BYEYAQAAAPmIuNoOAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'
      }

      async with request("POST", url_token, headers=headers_token, data=payload_token) as package_token:
            token_json = await package_token.json()
            token = token_json['access_token']

            url = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/instanceView?api-version=2022-03-01'
            headers = {
                      'Authorization': 'Bearer ' + token,
                      'content-type': 'text/plain',}
            async with request("GET", url, headers=headers) as responses:
                  info = await responses.json()

      if info['statuses'][1]['displayStatus'] != 'VM running':
            em=discord.Embed(title="Statuses of servers", description="", color=0x737373)
            em.add_field(name='VM', value="```diff\n- offline                                        \n```", inline=False)
            em.add_field(name='SMP', value="```diff\n- offline\n```", inline=False)
            em.add_field(name='Pvp server', value="```diff\n- offline\n```", inline=False)
            em.add_field(name='Free World', value="```diff\n- offline\n```", inline=False)
            em.add_field(name='Creative World', value="```diff\n- offline\n```", inline=False)
            em.set_footer(text="- harbane.net")
            em.timestamp = datetime.now()
            print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: metrics, VM deallocated')
            await interaction.followup.send(embed=em, ephemeral=False)
      elif info['statuses'][1]['displayStatus'] == 'VM running':
            if option == 'minimum':
                  url = "http://play.harbane.net:25560/api/v1/servers"
                  headers = {
                    'apikey': getenv('KEY'),
                    'Content-Type': 'application/json'
                  }
                  async with request("GET", url, headers=headers) as response:
                        spot = await response.json()


                  def check(status):
                        print(status)
                        if status == 0:
                              bong = 'diff\n- offline\n'
                        elif status == 1:
                              bong = 'diff\n+ online\n'
                        elif status == 2:
                              bong = 'killing'
                        elif status == 3:
                              bong = 'fix\nstarting\n'
                        elif status == 4:
                              bong = 'fix\nstopping\n'
                        else:
                              bong = status
                        return f'```{bong}```'

                  em=discord.Embed(title="Statuses of servers", description='', color=0x1ba300)
                  em.add_field(name='VM', value="```diff\n+ online                                         \n```", inline=False)
                  em.add_field(name=spot[0]['name'], value=check(spot[0]['status']), inline=False)
                  em.add_field(name=spot[1]['name'], value=check(spot[1]['status']), inline=False)
                  em.add_field(name=spot[2]['name'], value=check(spot[2]['status']), inline=False)
                  em.add_field(name=spot[3]['name'], value=check(spot[3]['status']), inline=False)
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()
                  button = Button(label= 'Dashboard', url='https://harbane.net/login', disabled=False)
                  view = View()
                  view.add_item(button)

                  await interaction.followup.send(embed=em, view=view)

            elif option == 'all':
                  servers = ['0434a83d-764e-481f-a01c-074c5a06d7be', '08d1d3d5-a182-4476-9fcf-69cfcee71119', '0967e29f-1354-4760-aee3-399140ee8846', '756fee89-2e37-4142-a7bd-fc3ad3852234']
                  stat = []

                  url = "http://play.harbane.net:25560/api/v1/servers"
                  headers = {
                    'apikey': getenv('KEY'),
                    'Content-Type': 'application/json'
                  }
                  async with request("GET", url, headers=headers) as response:
                        spot = await response.json()

                  for server in servers:
                        url = "http://play.harbane.net:25560/api/v1/servers/"+server+"/stats"

                        headers = {
                          'apikey': getenv('KEY')
                        }

                        async with request("GET", url, headers=headers) as stats:
                              des = await stats.json()

                        stat.append(des)
                        print(stat)

                  stats_json = json.dumps(stat)
                  load_json = json.loads(stats_json)
                  print(load_json[0]['latest']['playerLimit'])
                  print(load_json[0]['latest']['playersOnline'], )

                  def check(status, cpu_check, ram , ram_limit, online, limit):
                        print(status)
                        if status == 0:
                              bong = 'diff\n-offline'
                        elif status == 1:
                              bong = 'diff\n+online'
                        elif status == 2:
                              bong = 'killing'
                        elif status == 3:
                              bong = 'fix\nstarting'
                        elif status == 4:
                              bong = 'fix\nstopping'
                        else:
                              bong = status

                        print(cpu_check)
                        if str(cpu_check) == 'None':
                              cpu = cpu_check
                        elif str(cpu_check) != 'None':
                              cpu = str(cpu_check)+'%'

                        return f'```{bong} | cpu: {cpu} | ram: {ram}/{ram_limit} MB | {online}/{limit}\n```'

                  em=discord.Embed(title="Statuses of servers", description='', color=0x1ba300)
                  em.add_field(name='VM', value="```diff\n+ online                                         \n```", inline=False)
                  em.add_field(name=spot[0]['name'], value=check(spot[0]['status'], load_json[0]['latest']['cpu'], load_json[0]['latest']['memoryUsed'], load_json[0]['latest']['memoryLimit'], load_json[0]['latest']['playersOnline'], load_json[0]['latest']['playerLimit']), inline=False)
                  em.add_field(name=spot[1]['name'], value=check(spot[1]['status'], load_json[1]['latest']['cpu'], load_json[1]['latest']['memoryUsed'], load_json[1]['latest']['memoryLimit'], load_json[1]['latest']['playersOnline'], load_json[1]['latest']['playerLimit']), inline=False)
                  em.add_field(name=spot[2]['name'], value=check(spot[2]['status'], load_json[2]['latest']['cpu'], load_json[2]['latest']['memoryUsed'], load_json[2]['latest']['memoryLimit'], load_json[2]['latest']['playersOnline'], load_json[2]['latest']['playerLimit']), inline=False)
                  em.add_field(name=spot[3]['name'], value=check(spot[3]['status'], load_json[3]['latest']['cpu'], load_json[3]['latest']['memoryUsed'], load_json[3]['latest']['memoryLimit'], load_json[3]['latest']['playersOnline'], load_json[3]['latest']['playerLimit']), inline=False)
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()
                  button = Button(label= 'Dashboard', url='https://harbane.net/login', disabled=False)
                  view = View()
                  view.add_item(button)

                  await interaction.followup.send(embed=em, view=view)


@tree.command(
      name = 'execute',
      description = "excute a server command",
      guild = discord.Object(id = '872660349793472512')
)
@app_commands.choices( serverlist=[
            Choice(name="PvP server", value="08d1d3d5-a182-4476-9fcf-69cfcee71119"),
            Choice(name="Free world", value="0967e29f-1354-4760-aee3-399140ee8846"),
            Choice(name="Creative World", value="756fee89-2e37-4142-a7bd-fc3ad3852234")
])
@app_commands.checks.has_any_role(
      1013053147427643483, 'console'
)#1013053147427643483
async def self(interaction: discord.Interaction, serverlist: str ,command: str):
      url_token = "https://login.microsoft.com/acd94547-7d52-432f-98dc-c8d6c842128d/oauth2/token"
      payload_token='grant_type='+getenv('GRANT_TYPE')+'&client_id='+getenv('CLIENT_ID')+'&client_secret='+getenv('CLIENT_SECRET')+'&resource=https%3A%2F%2Fmanagement.azure.com%2F'
      headers_token = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'fpc=AnhYGHqywbdEuuR4lmAnhpO0BYEYAQAAAPmIuNoOAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'
      }

      package_token = requests.request("POST", url_token, headers=headers_token, data=payload_token)
      token_json = package_token.json()
      token = token_json['access_token']

      url = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/instanceView?api-version=2022-03-01'
      headers = {
                'Authorization': 'Bearer ' + token,
                'content-type': 'text/plain',}
      responses = requests.get(url, headers=headers)
      info = json.loads(responses.text)
      if info['statuses'][1]['displayStatus'] != 'VM running':
            em=discord.Embed(title="Virtual Machine is currently deallocated", description="To turn on Virtual Machine use **/vm**", color=0xE93434)
            em.set_footer(text="- harbane.net")
            em.timestamp = datetime.now()
            await interaction.response.send_message(embed=em, ephemeral=True)
            print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: tps, VM deallocated')
            await interaction.response.send_message(embed=em, ephemeral=False)
      elif info['statuses'][1]['displayStatus'] == 'VM running':
            if serverlist == '0434a83d-764e-481f-a01c-074c5a06d7be':
                  server = 'SMP'
            elif serverlist == '08d1d3d5-a182-4476-9fcf-69cfcee71119':
                  server = 'PVP server'
            elif serverlist == '0967e29f-1354-4760-aee3-399140ee8846':
                  server = 'Free world'
            elif serverlist == '756fee89-2e37-4142-a7bd-fc3ad3852234':
                  server = 'Creative world'

            await interaction.response.defer(ephemeral=False)
            status_url = "http://play.harbane.net:25560/api/v1/servers/"+serverlist
            headers = {
                  'apikey': getenv('KEY')
            }

            status_check = requests.request("GET", status_url, headers=headers)
            status = json.loads(status_check.text)
            if status['status'] != 1:
                  em = discord.Embed(title=server + ' is not online', description='Please choose another server that is online', color=0xE93434)
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()
                  await interaction.followup.send(embed=em)
            elif status['status'] == 1:
                  url = "http://play.harbane.net:25560/api/v1/servers/"+serverlist+"/execute/command"

                  payload = json.dumps({
                    "Guid": serverlist,
                    "Command": command
                  })
                  headers = {
                    'apikey': getenv('KEY'),
                    'command': command,
                    'Content-Type': 'application/json'
                  }
                  response = requests.request("POST", url, headers=headers, data=payload)
                  print(response.text)
                  em=discord.Embed(title=f"Excuted command on - {server}", description=f"command - {command}", color=0x1ba300)
                  em.set_footer(text="- harbane.net")
                  em.timestamp = datetime.now()
                  await interaction.followup.send(embed=em)


#-----------------------------------------------------------------------------------------------------------------------------
# @tree.error
# async def on_app_command_error(interaction : discord.Interaction, error : app_commands.AppCommandError):
      # if isinstance(error, app_commands.MissingAnyRole):
            # print('permission error')
            # await interaction.response.send_message("You don't have the required permission [<@&1013053147427643483>] to use this command", ephemeral = True)
      # else: 
            # return error

client.run(getenv('TOKEN'))

#------------------Test API Call------------------
# url = 'https://20.92.208.175:25560/api/v1/servers'

# headers = {,
#           'content-type': 'application/x-www-form-urlencoded',
#           'username': getenv('USER'),
#           'password': getenv('PASS')
# }

# response = requests.get(url, headers=headers)
# print(str(response) + ' api request successfully')



#-----------------------------------
