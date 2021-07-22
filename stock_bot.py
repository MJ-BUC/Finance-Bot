"""Mark Bucaro / This is my discord bot to display stock 
information requests using the Yahoo Finance API"""
import discord
import logging
import yfinance as yf


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('$help'):
            await message.channel.send("Current commands: \n '$hello' \n " +
                                       "'$search' (Search for a stock) \n '$example' \n " +
                                       "'$pss' (popular stock symbols)")

        if message.content.startswith('$hello'):
            await message.channel.send("Hello! I'm Finance Bot! I'm currently under development.")

        if message.content.startswith('$pss'):
            await message.channel.send("Popular Stock Symbols:\nAMC inc: 'AMC'\nApple: 'AAPL'\nNVIDIA Corp: 'NVDA'\n" +
                                       "Moderna inc: 'MRNA'\nMicrosoft Corp: 'MSFT'\nTesla inc: 'TSLA'\nAmazon.com inc: 'AMZN'")

        if message.content.startswith('$example'):
            stock = yf.Ticker("AAPL")

            name = stock.info['longName']
            symbol = stock.info['symbol']
            exchange = stock.info['exchange']
            currentPrice = stock.info['currentPrice']
            previousClose = stock.info['previousClose']
            dayOpen = stock.info['open']
            bid = stock.info['bid']
            ask = stock.info['ask']
            dayLow = stock.info['dayLow']
            dayHigh = stock.info['dayHigh']
            volume = stock.info['volume']
            await message.channel.send(name + '--'+'\n' + 'Symbol : '+symbol+'\n' +
                                       'Exchange : '+exchange+'\n' + 'CurrentPrice : '+str(currentPrice)+'\n' +
                                       'PreviousClose : '+str(previousClose)+'\n' + 'DayOpen : '+str(dayOpen)+'\n' +
                                       'Bid : '+str(bid)+'\n' + 'Ask : '+str(ask)+'\n' + 'DayLow : '+str(dayLow)+'\n' +
                                       'DayHigh : '+str(dayHigh)+'\n' + 'Volume : '+str(volume))

        if message.content.startswith('$search'):
            await message.channel.send("Please enter a stock symbol to search.")

            def check(msg):
                return msg.author.id == message.author.id
            msgInfo = await client.wait_for('message', check=check)
            stockSymbol = msgInfo.content

            stock = yf.Ticker(str(stockSymbol))

            name = stock.info['longName']
            symbol = stock.info['symbol']
            exchange = stock.info['exchange']
            currentPrice = stock.info['currentPrice']
            previousClose = stock.info['previousClose']
            dayOpen = stock.info['open']
            bid = stock.info['bid']
            ask = stock.info['ask']
            dayLow = stock.info['dayLow']
            dayHigh = stock.info['dayHigh']
            volume = stock.info['volume']

            try:
                await message.channel.send(name + '--'+'\n' + 'Symbol : '+symbol+'\n' +
                                           'Exchange : '+exchange+'\n' + 'CurrentPrice : '+str(currentPrice)+'\n' +
                                           'PreviousClose : '+str(previousClose)+'\n' + 'DayOpen : '+str(dayOpen)+'\n' +
                                           'Bid : '+str(bid)+'\n' + 'Ask : '+str(ask)+'\n' + 'DayLow : '+str(dayLow)+'\n' +
                                           'DayHigh : '+str(dayHigh)+'\n' + 'Volume : '+str(volume))
            except KeyError:
                logging.exception('Incorrect Stock Symbol')


client = MyClient()

# bot TOKEN
client.run('TOKEN')
