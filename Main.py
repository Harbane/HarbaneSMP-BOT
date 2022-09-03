import discord
import random
import time
from time import gmtime, strftime
import typing as t
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice
from discord.ui import Button, View
from dotenv import load_dotenv
from os import getenv
import requests
import json
import pyautogui
import numpy as np
from datetime import datetime
import asyncio

#------------------------------------

load_dotenv()

#-----------------------------------

class aclient(discord.Client):
      def __init__(self):
            super().__init__(intents=discord.Intents.default())
            self.synced = False
            
      async def on_ready(self):
            await self.wait_until_ready()
            if not self.synced:
                  await tree.sync(guild = discord.Object(id = '872660349793472512'))#guild = discord.Object(id = '872660349793472512')
                  self.synced = True
            print('Logged in as ' + client.user.name)
            print('id: ' + str(client.user.id))
            print('------')
            print('Bot is online and ready to use')
            await client.change_presence(activity=discord.Game(name='Harbane SMP'))
            
#-----------------------------------------------------------------------------------------------------------------------------

def start():
      time.sleep(80)
      pyautogui.press('win')
      time.sleep(2)
      pyautogui.write('remote')
      time.sleep(2)
      pyautogui.press('enter')
      time.sleep(2)
      pyautogui.press('enter')


countDown = 30

#def count():
#      global countDown
#      
#      while countDown != 0:
#            time.sleep(0)
#            countDown -= 1
#            print(countDown)
#-----------------------------------

client = aclient()
tree = app_commands.CommandTree(client)

#-----------------------------------------------------------------------------------------------------------------------------


@tree.command(
      name = 'test', 
      description = "testing", 
      guild = discord.Object(id = '872660349793472512')
      )

@app_commands.choices( name=[
            Choice(name="hello", value="hello"),
            Choice(name="world", value="world"),
      ]
)

async def self(interaction: discord.Interaction, name: str):
      await interaction.response.send_message(f"Hello {name}", ephemeral = True)



#-----------------------------------------------------------------------------------------------------------------------------
@tree.command(
      name = 'vm', 
      description = "Turn on and off Virtual Machine", 
      guild = discord.Object(id = '872660349793472512')
      )

@app_commands.choices( option=[
            Choice(name="on", value="1"),
            Choice(name="off", value="0"),
      ])
@app_commands.checks.has_any_role(
      1013053147427643483, 'console'
)#1013053147427643483

async def self(interaction: discord.Interaction, option: str):
      global countDown
      
      button = Button(label= 'View on web', url='https://harbane.net/login', disabled=False)
      view = View()
      view.add_item(button)

      visable = False
      
      url = 'https://management.azure.com/subscriptions/' + getenv('SUBSCRIPTION') + '/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/instanceView?api-version=2022-03-01'
      headers = {
            'Authorization': 'Bearer ' + getenv('AUTH'),
            'content-type': 'text/plain',
      }

      responses = requests.get(url, headers=headers)

      print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: {str(responses)} api request')

      info = json.loads(responses.text)
      if info['statuses'][1]['displayStatus'] == 'VM running':
            if option == "1": # 1 is for on
                  em=discord.Embed(title="|          Control Panel          |", description="Virtual machine already on", color=0xE93E3E)
                  em.set_thumbnail(url="https://harbane.net/Images/server-icon5.png")
                  em.set_footer(text="- harbane.net")
                  visable = True              
                  print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: pc already on')
                  
                  

            elif option == "0": # 0 is for off
                  embed=discord.Embed(title="|          Control Panel          |", description="Virtual Machine Status - *Running*", color=0x22cc00)
                  embed.set_thumbnail(url="https://harbane.net/Images/server-icon5.png")
                  embed.add_field(name="Current Job:", value="*Stopping virtual machine*", inline=True)
                  embed.set_footer(text="- harbane.net")
                  
                  
                  em=discord.Embed(title="|          Control Panel          |", description="Stopped VM*", color=0x22cc00)
                  em.set_footer(text="- harbane.net")
                  
                  print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: pc turning off')

                  #stops vm
                  stopURL = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/deallocate?api-version=2022-03-01'
                  headers = {
                      'Authorization': 'Bearer ' + getenv('AUTH'),
                      'content-type': 'text/plain',
                  }

                  stopVM = requests.post(stopURL, headers=headers)

                  print(str(stopVM) + ': vm Stopping')
                  await interaction.response.send_message(embed=embed, view=view, ephemeral = visable)
                  

                  #---------

      elif info['statuses'][1]['displayStatus'] == 'VM deallocated':
            if option == "1": # 1 is for on
                  em=discord.Embed(title="|          Control Panel          |", description="virtual machine on", color=0x1ba300)
                  em.set_footer(text="- harbane.net")
                  
                  embed=discord.Embed(title="|          Control Panel          |", description="Virtual Machine Status - *Deallocated*", color=0x1ba300)
                  embed.set_thumbnail(url="https://harbane.net/Images/server-icon5.png")
                  embed.add_field(name="Current Job:", value="*Starting virtual machine*", inline=True)
                  embed.add_field(name="Time:", value=f"Estimated time of start up {random.randint(3, 6)} min", inline=False)
                  em.set_footer(text="- harbane.net")
                  
                  print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: starting pc')
                  
                  #starts vm
                  startURL = 'https://management.azure.com/subscriptions/'+getenv('SUBSCRIPTION')+'/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/start?api-version=2022-03-01'
                  headers = {
                      'Authorization': 'Bearer ' + getenv('AUTH'),
                      'content-type': 'text/plain',
                  }
                  startVM = requests.post(startURL, headers=headers)

                  print(str(startVM) + ': vm starting')
                  await interaction.response.send_message(embed=embed, view=view, ephemeral = visable)
                  start()
            
            elif option == "0": # 0 is for off
                  em=discord.Embed(title="|          Control Panel          |", description="Virtual machine already off", color=0xE93E3E)
                  em.set_thumbnail(url="https://harbane.net/Images/server-icon5.png")
                  em.set_footer(text="- harbane.net")
                  visable = True
                  print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: pc already off')
      
      
      await interaction.response.send_message(embed=em, view=view, ephemeral = visable)

# @tree.error
# async def on_app_command_error(interaction, error):
#       await interaction.response.send_message("Sorry, you either dont have the correct perms to use this command or there seems to be an internal error. (try doing the command again)", ephemeral = True)
#-----------------------------------------------------------------------------------------------------------------------------

@tree.command(
      description = "See status of Harbane SMP", 
      guild = discord.Object(id = '872660349793472512')
)

@app_commands.choices( list=[
            Choice(name="vm", value="SMP"),
            Choice(name="smp", value="SMP"),
            Choice(name="pvp server", value="PVP server"),
      ])

async def self(interaction: discord.Interaction, list: str):
      button = Button(label= 'View on web', url='https://harbane.net/login', disabled=False)
      view = View()
      view.add_item(button)
      
      ###############################################
      
      url = 'https://management.azure.com/subscriptions/' + getenv('SUBSCRIPTION') + '/resourceGroups/Mc-host/providers/Microsoft.Compute/virtualMachines/mchost01/instanceView?api-version=2022-03-01'
      headers = {
            'Authorization': 'Bearer ' + getenv('AUTH'),
            'content-type': 'text/plain',
      }

      responses = requests.get(url, headers=headers)

      print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: {str(responses)} api request')

      info = json.loads(responses.text)
      
      ###############################################
      
      if info['statuses'][1]['displayStatus'] == 'VM running':
            if list == "SMP":
                  url_smp = "http://20.28.163.224:25560/api/v1/servers/"+getenv('SMP')
                  
                  headers_smp = {
                    'apikey': getenv('KEY'),
                    'Content-Type': 'application/json'
                  }  
                  
                  response = requests.request("GET", url_smp, headers=headers_smp)
                  
                  info = json.loads(response.text)

                  print(info['status'])
                  
                  if info['status'] == 1:
                        em=discord.Embed(title="Harbane SMP", description="SMP is online       :green_circle:", color=0x1ba300)
                        em.set_footer(text="- harbane.net")
                  elif info['status'] == 0:
                        em=discord.Embed(title="Harbane SMP", description="SMP is offline       :red_circle:", color=0x1ba300)
                        em.set_footer(text="- harbane.net")
                  elif info['status'] == 3:
                        em=discord.Embed(title="Harbane SMP", description="SMP is being killed", color=0x1ba300)
                        em.set_footer(text="- harbane.net") 
                  elif info['status'] == 4:
                        em=discord.Embed(title="Harbane SMP", description="SMP is being restarted", color=0x1ba300)
                        em.set_footer(text="- harbane.net") 
                        
            elif list == 'PVP server':
                  url_pvp = "http://20.28.163.224:25560/api/v1/servers/"+getenv('SMP')
                  
                  headers_pvp = {
                    'apikey': getenv('KEY'),
                    'Content-Type': 'application/json'
                  }  
                  
                  response = requests.request("GET", url_pvp, headers=headers_pvp)
                  
                  info = json.loads(response.text)

                  print(info['status'])
                  
                  if info['status'] == 1:
                        em=discord.Embed(title="Harbane SMP", description="PVP server is online       :green_circle:", color=0x1ba300)
                        em.set_footer(text="- harbane.net")
                  elif info['status'] == 0:
                        em=discord.Embed(title="Harbane SMP", description="PVP server is offline       :red_circle:", color=0x1ba300)
                        em.set_footer(text="- harbane.net")
                  elif info['status'] == 3:
                        em=discord.Embed(title="Harbane SMP", description="PVP server is being killed", color=0x1ba300)
                        em.set_footer(text="- harbane.net") 
                  elif info['status'] == 4:
                        em=discord.Embed(title="Harbane SMP", description="PVP server is being restarted", color=0x1ba300)
                        em.set_footer(text="- harbane.net") 
            # print(f'[{strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}]: pc running')
           
      elif info['statuses'][1]['displayStatus'] == 'VM deallocated':
            em=discord.Embed(title="Harbane SMP", description="Virtual machine is deallocated", color=0x1ba300)
            em.footer(text='harbane.net')
      else:
            em=discord.Embed(title="Error", description="request failed, try again in abit", color=0x1ba300)
            em.footer(text='harbane.net')
      ###############################################
      
      await interaction.response.send_message(embed=em, view=view)

#-----------------------------------------------------------------------------------------------------------------------------


@tree.command(
      name = 'logs', 
      description = "Get SMP console logs", 
      guild = discord.Object(id = '872660349793472512')
)


async def self(interaction: discord.Interaction, lines: str):
      url = 'http://20.28.163.224:25560/api/v1/servers/0434a83d-764e-481f-a01c-074c5a06d7be/console?AmountOfLines='+lines+'&Reversed=true&takeFromBeginning=false'
      
      headers = {
                'apikey': getenv('KEY'),
      }
      
      response = requests.get(url, headers=headers)
      print(str(response) + ' api request, (logs lines = ' + lines +')')

      info = json.loads(response.text)
      
      with open('discord.py/file.txt', 'w') as f:
                    for lines in info:
                      f.write(lines)
                      f.write('\n')
      
      file = discord.File('discord.py/file.txt', filename = 'logs.txt')

      await interaction.response.send_message('here ya go', file=file)


#-----------------------------------------------------------------------------------------------------------------------------
      
      
@tree.command(
      name = 'server', 
      description = "Turn on and off SMP", 
      guild = discord.Object(id = '872660349793472512')
      )

@app_commands.choices( serverlist=[
            Choice(name="smp", value="SMP"),
            Choice(name="pvp server", value="PVP server"),
      ])

@app_commands.choices( option=[
            Choice(name="off", value="turned off",),
            Choice(name="on", value="turned on"),
            Choice(name="kill", value="killed"),
            Choice(name="restart", value="restarted"),
      ])
@app_commands.checks.has_any_role(
      1013053147427643483, 'console'
)#1013053147427643483

async def self(interaction: discord.Interaction, serverlist: str, option: str):
      if serverlist == "SMP":
            em=discord.Embed(title="", description=serverlist + " is now being " + option, color=0x1ba300)
            em.set_author(name="Harbane SMP", icon_url='https://harbane.net/Images/server-icon5.png')
            em.set_footer(text="harbane.net")
                      
            url = "http://20.28.163.224:25560/api/v1/servers/"+getenv('SMP')+"/execute/action"        

            if option == "turned off":
                  payload = json.dumps({
                    "Guid": getenv('SMP'),
                    "Action": '1'
                  })
                  headers = {
                    'apikey': getenv('KEY'),
                    'action': '1',
                    'Content-Type': 'application/json'
                  }     
            elif option == "turned on":
                  payload = json.dumps({
                    "Guid": getenv('SMP'),
                    "Action": '2'
                  })
                  headers = {
                    'apikey': getenv('KEY'),
                    'action': '2',
                    'Content-Type': 'application/json'
                  }
            elif option == "killed":
                  payload = json.dumps({
                    "Guid": getenv('SMP'),
                    "Action": '3'
                  })
                  headers = {
                    'apikey': getenv('KEY'),
                    'action': '3',
                    'Content-Type': 'application/json'
                  }  
            elif option == "restarted":
                  payload = json.dumps({
                    "Guid": getenv('SMP'),
                    "Action": '4'
                  })
                  headers = {
                    'apikey': getenv('KEY'),
                    'action': '4',
                    'Content-Type': 'application/json'
                  }     
      if serverlist == "PVP server":
            em=discord.Embed(title="", description=serverlist + " is now being " + option, color=0x1ba300)
            em.set_author(name="Harbane SMP", icon_url='https://harbane.net/Images/pvpserver-icon.png')    
            em.set_footer(text="harbane.net")   
            
            url = "http://20.28.163.224:25560/api/v1/servers/"+getenv('PVP')+"/execute/action"        

            if option == "turned off":
                  payload = json.dumps({
                    "Guid": getenv('PVP'),
                    "Action": '1'
                  })
                  headers = {
                    'apikey': getenv('KEY'),
                    'action': '1',
                    'Content-Type': 'application/json'
                  }     
            elif option == "turned on":
                  payload = json.dumps({
                    "Guid": getenv('PVP'),
                    "Action": '2'
                  })
                  headers = {
                    'apikey': getenv('KEY'),
                    'action': '2',
                    'Content-Type': 'application/json'
                  }
            elif option == "killed":
                  payload = json.dumps({
                    "Guid": getenv('PVP'),
                    "Action": '3'
                  })
                  headers = {
                    'apikey': getenv('KEY'),
                    'action': '3',
                    'Content-Type': 'application/json'
                  }  
            elif option == "restarted":
                  payload = json.dumps({
                    "Guid": getenv('PVP'),
                    "Action": '4'
                  })
                  headers = {
                    'apikey': getenv('KEY'),
                    'action': '4',
                    'Content-Type': 'application/json'
                  }     
                  

      response = requests.request("POST", url, headers=headers, data=payload)

      print(f'[{response}] api request, SMP option {option}')
      
      button = Button(label= 'View on web', url='https://harbane.net/login', disabled=False)
      view = View()
      view.add_item(button)
      
      await interaction.response.send_message(embed=em, view=view)



#-----------------------------------------------------------------------------------------------------------------------------



@tree.command(
      name = 'whitelist', 
      description = "Whitelist someone to Harbane SMP", 
      guild = discord.Object(id = '872660349793472512')
      )

@app_commands.choices( option=[
            Choice(name="add", value="add"),
            Choice(name="remove", value="remove"),
      ])

@app_commands.checks.has_any_role(
      1013053147427643483, 'console'
)#1013053147427643483

async def self(interaction: discord.Interaction, option: str, user: str):
      url = "http://20.28.163.224:25560/api/v1/servers/0434a83d-764e-481f-a01c-074c5a06d7be/execute/command"

      payload = json.dumps({
        "Guid": "0434a83d-764e-481f-a01c-074c5a06d7be",
        "command": 'whitelist ' + option + ' ' + user
      })
      headers = {
        'apikey': getenv('KEY'),
        'command': 'whitelist ' + option + ' ' + user,
        'Content-Type': 'application/json'
      }

      response = requests.request("POST", url, headers=headers, data=payload)

      print(f'{response} api request, whitelist {option} {user}')

      if option == 'add':
            em=discord.Embed(title="Whitelist", description="Added " + user + ' to whitelist', color=0x1ba300)
            em.set_author(name="Harbane SMP", icon_url='https://harbane.net/Images/server-icon5.png')
            em.set_footer(text="harbane.net")
      else:
            em=discord.Embed(title="Whitelist", description="Removed " + user + ' from whitelist', color=0x1ba300)
            em.set_author(name="Harbane PVP", icon_url='https://harbane.net/Images/server-icon5.png')
            em.set_footer(text="harbane.net")
            
      button = Button(label= 'View on web', url='https://harbane.net/login', disabled=False)
      view = View()
      view.add_item(button)
      
      await interaction.response.send_message(embed=em, view=view)
      
      
@tree.command(
      name = 'metrics', 
      description = "request server metrics", 
      guild = discord.Object(id = '872660349793472512')
      )

async def self(interaction: discord.Interaction):
      file = discord.File('discord.py/foo.png', filename="image.png")
      em=discord.Embed(title="|          Control Panel          |", description="Virtual Machine Status - *Deallocated*", color=0x1ba300)
      # em.set_thumbnail(url="https://harbane.net/Images/server-icon5.png")
      em.add_field(name="Current Job:", value="*ok*", inline=True)
      em.set_thumbnail(url='attachment://image.png')
      em.set_footer(text="- harbane.net")
      await interaction.response.send_message(file=file, embed=em)
    
#-----------------------------------------------------------------------------------------------------------------------------

      
      
client.run(getenv('TOKEN')) 
 








#------------------Test API------------------ 
# url = 'https://20.92.208.175:25560/api/v1/servers'

# headers = {, 
#           'content-type': 'application/x-www-form-urlencoded',
#           'username': getenv('USER'),
#           'password': getenv('PASS')
# }

# response = requests.get(url, headers=headers)
# print(str(response) + ' api request successfully')


#-----------------------------------
                
