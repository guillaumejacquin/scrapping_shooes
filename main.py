import discord
from discord.ext import commands
import urllib.request
import requests
import asyncio


import os
from datetime import datetime
import threading
from datetime import datetime

shooes_list = []

bot = commands.Bot(command_prefix ="!", description = "yolooooooooooooooooooooooooooooo")

@bot.event
async def on_ready():
    print("prêt!")

go = True

async def my_task(ctx, username):
    while go == True:
        # await ctx.send("tic tac boum")

        now = datetime.now().time() # time object

        date = str(now)
        date = (date[:-7])
        
        if (date == "09:00:00"):
                try:
                    i = shooes_list[0]
                    for j in range(len(shooes_list)):
                        title = "k"
                        paire = shooes_list[j]
                        number = int(j) + 1
                        
                        embed = discord.Embed(title = "paire numéro " + str(number), color=0x2C75FF)
                        embed.add_field(name = "paire " + str(number), value = paire, inline = True)

                        await ctx.send(embed = embed)
                except Exception:
                    await ctx.send("Aucun élément n'a encore été ajouté, pensez a ajouter une paire avec la commande !add(paire)")


        await asyncio.sleep(1)


@bot.command()
async def infoo(ctx, username):
    bot.loop.create_task(my_task(ctx, username))

@bot.command()
async def stop(ctx):
    #ici
    #want to stop this fcking function
    print("alaid")


@bot.command()
async def coucou(ctx):
    await ctx.send("yo c est le test")

#on peut faire taille par taille normalement si besoin


@bot.command()
async def add(ctx, *paire):
    paire = "".join(paire)
    paire = str(paire)
    string = "\n**" + paire + "** a bien été ajoutée à la liste.\n si vous voulez consulter la liste, tapez !show_list. \n si vous voulez supprimer un élement tapez !remove_shooes(paire)"
    await ctx.send(string)
    shooes_list.append(paire)
    await ctx.send(shooes_list)
    embed = discord.Embed(title = "Une nouvelle paire a ete ajoutée!", color=0x2C75FF)
    # embed.set_thumbnail(url= image)
    # embed.set_image(url= image)

    embed.add_field(name = "nouvel element ajouté", value = string , inline = False)
    await ctx.channel.send(embed=embed)


    
@bot.command()
async def show_list(ctx): 
    try:
        i = shooes_list[0]
        for j in range(len(shooes_list)):
            title = "k"
            paire = shooes_list[j]
            number = int(j) + 1
            
            embed = discord.Embed(title = "paire numéro " + str(number), color=0x2C75FF)
            embed.add_field(name = "paire " + str(number), value = paire, inline = True)

            await ctx.send(embed = embed)
    except Exception:
        await ctx.send("Aucun élément n'a encore été ajouté, pensez a ajouter une paire avec la commande !add(paire)")

@bot.command()
async def remove(ctx, *paire):
    paire = "".join(paire)
    remove = []

    for j in shooes_list:
        if (str(paire) == j):
            remove.append(j)
            break

    if (len(remove) == 0):
        await (ctx.send("La paire que vous indiquez n'est pas dans la liste"))
        return(0)


    shooes_list.remove(j)
    await ctx.send("La paire **" + paire + "** a bien été supprimée")


@bot.command()
async def info(ctx, *paire):
    paire = "-".join(paire)
    url = "https://stockx.com/"
    suite_url = paire.lower()
    url = url + suite_url
    await ctx.send(url)

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "fr-fr,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    response = requests.get(url, headers=headers)

    scrapping_string = str(response.content)
    splitted = scrapping_string.split(',')
    i = 0

    last_sale = []
    last_sale_bool = 0

    change_value = []
    change_value_bool = 0

    change_percentage = []
    change_percentage_bool = 0

    lowest_ask = []
    lowest_ask_bool = 0


    highest_Bid = []
    highest_Bid_bool = 0

    stock_sold = []
    stock_sold_bool = 0

    price_premium = []
    price_premium_bool = 0

    sales_last_72_hours = []
    sales_last_72_hours_bool = 0

    lowest_ask_flow = []
    lowest_ask_flow_bool = 0

    image = []
    image_bool = 0

    for word in splitted:
        i += 1
        if (i < 50_000):
            if("lastSale" in word and last_sale_bool == 0):
                last_sale_bool = 1
                last_sale.append(word)
            
            if ("changeValue" in word and change_value_bool == 0):
                change_value_bool = 1
                change_value.append(word)

            if ("changePercentage" in word and change_percentage_bool == 0):
                change_percentage_bool = 1
                change_percentage.append(word)

            if ("lowestAsk" in word and lowest_ask_bool == 0):   #a corriger, si besoin, il suffit d'incrementer jusqu a avoir le plus bas
                lowest_ask_bool = 1
                lowest_ask.append(word)

            if ("highestBid" in word and highest_Bid_bool == 0):
                highest_Bid.append(word)

            if ("deadstockSold" in word and stock_sold_bool == 0):
                stock_sold_bool = 1
                stock_sold.append(word)

            if ("pricePremium" in word and price_premium_bool == 0):
                price_premium_bool = 1
                # tmp = 10 * float(word)
                price_premium.append(word)
            
            if ("salesLast72Hours" in word and sales_last_72_hours_bool == 0):
                sales_last_72_hours_bool = 1
                sales_last_72_hours.append(word)

            if ("lowestAskFloat" in word and lowest_ask_flow_bool == 0):
                lowest_ask_flow_bool = 1
                lowest_ask_flow.append(word)

            if ("media" in word):
                image_bool += 1
                if (image_bool == 40):
                    image.append(word)






    last_sale = last_sale[0]
    last_sale = last_sale.split(':')
    last_sale = last_sale[1]

    change_value = change_value[0]
    change_value = change_value.split(':')
    change_value = change_value[1]

    change_percentage = change_percentage[0]
    change_percentage = change_percentage.split(':')
    change_percentage = change_percentage[1]

    stock_sold = stock_sold[0]
    stock_sold = stock_sold.split(':')
    stock_sold = stock_sold[1]

    price_premium = price_premium[0]
    price_premium = price_premium.split(':')
    price_premium = price_premium[1]
    price_premium = float(price_premium) * 100

    sales_last_72_hours = sales_last_72_hours[0]
    sales_last_72_hours = sales_last_72_hours.split(':')
    sales_last_72_hours = sales_last_72_hours[1]

    lowest_ask_flow = lowest_ask_flow[0]
    lowest_ask_flow = lowest_ask_flow.split(':')
    lowest_ask_flow = lowest_ask_flow[1]

    # image = image[0]
    # image = image.split('"')
    # print (image)
    # # image =  (image[5])

    
    place = ""


    embed = discord.Embed(title = paire, color=0x2C75FF)
    # embed.set_thumbnail(url= image)
    # embed.set_image(url= image)

    embed.add_field(name = "Prix moyen", value = lowest_ask_flow + " $US", inline = False)
    embed.add_field(name = "Derniere vente:", value = last_sale + " euros", inline = False)
    embed.add_field(name = "Change Value:", value = change_value + "%", inline = False)
    embed.add_field(name = "Nombres de paires vendues", value = stock_sold + " ventes", inline = False)
    embed.add_field(name = "Plus value", value = str(price_premium) + "%",  inline = False)
    embed.add_field(name = "Nombres de ventes ces derniers 3 jours", value = sales_last_72_hours + " ventes", inline = False)
    embed.add_field(name = '\u200b', value = '\u200b' , inline = False)


    await ctx.channel.send(embed=embed)





bot.run("ODAwMzQ3OTI2MjQwNDI4MDQz.YAQ0Fw.pcxQtt2AfZHAjf9Vyz-rJvLZ0g0")

