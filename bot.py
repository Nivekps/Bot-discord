import discord
import logging
from random import choice
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

alegrar = ["Ser feliz sem motivo é a mais autêntica forma de felicidade."
           "Quase sempre a maior ou menor felicidade depende do grau de decisão de ser feliz"]

triste = ["solidão", "infeliz", "sofro", "sofreu", "depresão", ]
ofensa = ["fdp", "porra", "desfraçado", "foda-se", "cuzão"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = message.content
    user = message.author.name

    if msg.startswith("%oi"):
        await message.channel.send("Olá, {}".format(user))

    if msg in triste:
        await message.channel.send(f"{user}, {choice(alegrar)}")

    if msg in ofensa:
        await message.channel.send(f"{user}, atitudes derespeitosas não são permitidas.")

client.run("Insira o 'TOKEN' aqui")
