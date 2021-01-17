import discord
from discord.ext import commands
import urllib.request
import requests

import os



bot = commands.Bot(command_prefix ="!", description = "yolooooooooooooooooooooooooooooo")

@bot.event
async def on_ready():
    print("prêt!")

@bot.command()
async def coucou(ctx):
    await ctx.send("yo c est le test")

#on peut faire taille par taille normalement si besoin
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


    print ("last sale = ", last_sale)
    print ("change_value= ", change_value)
    print(change_percentage)
    print(stock_sold)
    print(price_premium)
    print(sales_last_72_hours)

    await ctx.send(last_sale)
    await ctx.send(change_value)
    await ctx.send(change_percentage)
    await ctx.send(stock_sold)
    await ctx.send(price_premium)
    await ctx.send(sales_last_72_hours)





    #print("lowestAsk = ", lowest_ask)
    #print("highestBid = ", highest_Bid)

    # with urllib.request.urlopen(url) as response:
    #     texte = response.read()

    # poste_string = str(texte)
    # splitted = poste_string.split()

    # for word in splitted:
    #     print (word)
     


bot.run("TOKEN")

