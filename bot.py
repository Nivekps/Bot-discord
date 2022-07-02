import discord
from discord.ext import commands
import logging
from random import choice
import json
import requests
#Linhas de código para mostar erros do código 
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#Início do bot - discord
bot = commands.Bot(command_prefix="!")

alegrar = ["Ser feliz sem motivo é a mais autêntica forma de felicidade."
           "Quase sempre a maior ou menor felicidade depende do grau de decisão de ser feliz"]

triste = ["solidão", "infeliz", "sofro", "sofreu", "depresão", ]
ofensa = ["fdp", "porra", "desfraçado", "foda-se", "cuzão"]


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@bot.event
async def on_message(message):
    msg = message.content
    user = message.author.name

    if msg.startswith("%oi"):
        await message.channel.send("Olá, {}".format(user))

    if msg in triste:
        await message.channel.send(f"{user}, {choice(alegrar)}")

    if msg in ofensa:
        await message.channel.send(f"{user}, atitudes derespeitosas não são permitidas.")
@bot.command()
async def covid_estado(ctx, sigla_estado):
    resp = requests.get("https://covid19-brazil-api.now.sh/api/report  /v1/brazil/uf/{}".format(sigla_estado))
    json_data = json.loads(resp.text)
    for a, b in json_data.items():
       await ctx.send(f"Casos de covid em {sigla_estado}")
       await ctx.send(f"{a}: {b}")
@bot.command()
async def covid_pais(ctx, sigla_pais):
    resp = requests.get("https://covid19-brazil-api.now.sh/api/report  /v1/{}".format(sigla_pais))
    json_data = json.loads(resp.text)
    for a, b in json_data["data"].items():
       await ctx.send(f"Casos de covid: {sigla_pais}")
       await ctx.send(f"{a}: {b}")
client.run("Insira o 'TOKEN' aqui")
