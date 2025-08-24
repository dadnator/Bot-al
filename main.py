import os
import discord
from discord import app_commands
from discord.ext import commands
from keep_alive import keep_alive
import random

# --- TOKEN ET INTENTS ---
token = os.environ['TOKEN_BOT_DISCORD']
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# Définissez ici votre liste de 12 noms
liste_de_noms = [
    "Tamayo", "Kinuro", "Momako", "Heiji", "Haruka", "Izusu",
    "Miyaji", "Numezawa", "Suko", "Tomi", "Kentora", "Hikura"
]

# --- Commande /al pour choisir un nom au hasard ---
@bot.tree.command(name="al", description="Tire au sort un nom parmi une liste de 12.")
async def al(interaction: discord.Interaction):
    # Choix d'un nom au hasard dans la liste
    nom_gagnant = random.choice(liste_de_noms)

    # Création de l'embed pour afficher le résultat
    embed = discord.Embed(
        title="🎉 Objectif de drop !",
        description=f"Et le grand gagnant est  **{nom_gagnant}** !",
        color=discord.Color.green()
    )

    # Envoi de l'embed
    await interaction.response.send_message(embed=embed)

@bot.event
async def on_ready():
    """
    Se déclenche lorsque le bot est connecté à Discord et prêt.
    """
    print(f'Connecté en tant que {bot.user.name} !')
    try:
        # Synchronise toutes les commandes slash avec Discord
        synced = await bot.tree.sync()
        print(f"Synchronisé {len(synced)} commande(s).")
    except Exception as e:
        print(f"Erreur lors de la synchronisation : {e}")

# --- ACTIVER LE BOT ---
keep_alive()
bot.run(token)
