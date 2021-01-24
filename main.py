import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

resp_text = ["Look at this good boy!", 
            "This pupper always makes my day better!",
            "What a chonker!",
            "Just the goodest boy!",
            "You can't look at this face without smiling..","Look who's here to meet you!"]

commands = {'$breed': ' {{name of breed}} - use this to see a              picture of a specific breed', 
            '$del': ' {{name of breed}} - use this to delete a breed from list of favourite breeds',
            '$dog': ' - use this to see a random picture of a dog',
            '$help': ' - use this to see a list of all commands',
            '$hi': ' - use this to see if I am online',
            '$more': ' - use this to see another picture of the last breed you saw',
            '$new': ' {{name of breed}} - use this to add a specific breed to list of favourite breeds'}


fav_breeds = []

last_breed = ""
breed_help = True

def get_dog():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    json_data = json.loads(response.text)
    image = json_data['message']
    status = json_data['status']
    print(status)
    breed = image.split('/')[4]
    global last_breed
    last_breed = breed
    print(last_breed)
    print(breed)
    return (image, breed)


def get_breed(breed):
    global last_breed
    last_breed = breed
    response = requests.get('https://dog.ceo/api/breed/{}/images/random'.format(breed))
    json_data = json.loads(response.text)
    image = json_data['message']
    status = json_data['status']
    print(last_breed)
    print(status)
    return(image)
    

def update_fav_breeds(breed):
    if 'fav_breeds' in db.keys():
        fav_breeds = db['fav_breeds']
        fav_breeds.append(breed)
        db['fav_breeds'] = fav_breeds
    else:
        db['fav_breeds'] = [breed]


@client.event
async def on_ready():
    print('{0.user} is ready to go for a walk'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$hi'):
        await message.channel.send ('Woof! Sorry, I meant Hello!')
        await message.channel.send ('If you need any help remembering all of the commands I know, just type $help!')

    if msg.startswith('$dog'):
        await message.channel.send(random.choice(resp_text))
        [image, breed] = get_dog()
        await message.channel.send(image)
        global breed_help
        if breed_help:
          await message.channel.send("This is a {0}. If you are like me and find this face irresistible, you can add it to your favourite breeds with the command '$new {0}' and call it anytime by typing '$breed {0}'".format(breed))
          breed_help = False
        
        

    if msg.startswith('$breed'):
      breed = msg.split('$breed ', 1)[1]
      await message.channel.send("I get it I love {} too!".format(breed))
      await message.channel.send(get_breed(breed))

    if any(word in msg for word in sad_words):
        await message.channel.send(get_dog()[0])

  
    if msg.startswith('$new'):
        breed = msg.split('$new ', 1)[1]
        update_fav_breeds(breed)
        await message.channel.send("{} added to favourites!".format(breed))

    if msg.startswith('$more'):
      await message.channel.send(get_breed(last_breed))

    if msg.startswith('$help'):
      await message.channel.send('These are all of the commands I know:')
      for key,value in commands.items():
        command = key + value
        await message.channel.send(command)

    
client.run(os.getenv('TOKEN'))
