import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=";", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command("organictrash")
async def organic_trash(ctx):
    organic = ("exhibit1.jpg", "exhibit2.jpg")
    with open(f"organic/{random.choice(organic)}", "rb") as f:
        img = discord.File(f)

    await ctx.send("Organic trash is trash that originates from a living thing like a plant or animal.")
    await ctx.send(file=img)


@bot.command("inorganictrash")
async def inorganic_trash(ctx):
    inorganic = ("exhibit1.jpg", "exhibit2.jpg", "exhibit3.jpg")
    with open(f"inorganic/{random.choice(inorganic)}", "rb") as f:
        img = discord.File(f)

    await ctx.send("Inorganic trash is trash that originates from a non-living thing like a mineral or artificial thing.")
    await ctx.send(file=img)


@bot.command("toxicgasses")
async def toxic_gasses(ctx):
    await ctx.send("These are gasses released through pollution which ruin the atmosphere and may cause lung cancer and other diseases.")
    await ctx.send("Some examples include carbon dioxide (CO2), sulfur dioxide (SO2), nicotine (C10H14N2), carbon monoxide (CO), and more. These gasses can also trigger acid rain by converting the water (H2O) into acids such as sulfuric acid and carbonic acid.")


@bot.command("recyclingtips")
async def recycle(ctx):
    await ctx.send("""Paper Power: Recycling paper means we can use it again to make new paper. So, don't throw away those old drawings, school papers, or newspapers. Put them in the recycling bin!
                    Clever Cans: Aluminum cans, like soda cans, are like superheroes of recycling. They can be turned into new cans really easily. So, collect them and put them in the recycling bin.
                    Plastic Love: Some plastic bottles and containers can be recycled, but not all of them. Look for a recycling symbol on the bottom with a number inside. If it's a 1, 2, or 5, you can recycle it. If not, it goes in the regular trash.
                    Glass Goodness: Glass bottles and jars are strong and can be recycled over and over. So, when you're done with a glass jar of peanut butter or a glass bottle of juice, rinse it out and recycle it.
                    Cardboard Fun: Big cardboard boxes from packages or pizza can be recycled. Flatten them and put them in the recycling bin. It's like giving them a second life!
                    No Greasy Stuff: Things covered in food or grease, like pizza boxes, can't be recycled because they make the other stuff dirty. So, it's better to put them in the trash.
                    Battery Care: Batteries from toys or gadgets can be harmful if not recycled properly. Look for special drop-off spots for old batteries or electronic waste.
                    Reduce and Reuse: Try to use less stuff that needs to be recycled. Reuse items when you can, like turning an old jar into a pencil holder instead of buying a new one.
                    Paper vs. Plastic: At the store, choose reusable bags or paper bags instead of single-use plastic bags. This helps reduce plastic waste.
                    Learn and Teach: Share what you know about recycling with your friends and family. The more people know, the better we can take care of our planet!
                    Remember, recycling is like giving things a second chance to be useful. It's a great way to help the environment and make the world a cleaner, better place.
                  """)
    await ctx.send(file="recycle.jpg")


bot.run("MTEzMDUwOTg2MTI0ODA0NTA5MA.G6cDSP.APlR_khn8QBmDZseQAKfeiUY2UQsyJMjKA-Eqg")
