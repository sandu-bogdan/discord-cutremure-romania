import discord
import requests
import datetime
from datetime import datetime
import time

channelId = 1053968541751185428
baseUrl = 'https://ask.sandu-bogdan.com/Git-SRobot-Cutremure/PHP-Server/index.php?'
clientToken = 'ODU3NjA2NjczODk0NzM1ODg2.GYcFCM.KqLm-OXWObh64TwH4fukFaA3cdtDqSK8cDJ0m0'


class MyClient(discord.Client): 
    async def on_ready(self):
        print('Logged on as', self.user)
        #SRobot seism-alert channel
        seismChannel = self.get_channel(channelId)

        initial = requests.get(baseUrl+'type=recent')
        if(initial.status_code == 200):
            split = initial.text.split(',')
            initialdateSeismic = split[0]
        else:
            initialdateSeismic = "error"

        initialEws = requests.get(baseUrl+'type=ews')
        if(initialEws.status_code == 200):
            splitEws = initialEws.text.split(',')
            initialdateSeismicEws = splitEws[1]
        else:
            initialdateSeismicEws = "error"

        while True:
            currentDateAndTime = datetime.now()
            requestEws = requests.get(baseUrl+'type=ews')
            splitEws = requestEws.text.split(',')
            if(requestEws.status_code == 200):
                if(splitEws[1] > initialdateSeismicEws and initialdateSeismicEws != "error"):
                    initialdateSeismicEws = splitEws[1]
                    try: 
                        await seismChannel.send("```LIVE! Mag:" + splitEws[0] + ", data: " + splitEws[1] + ", secunde:" + splitEws[2] + ", lat:" + splitEws[3] + ", lng: " + splitEws[4] + "🌋```")
                    except Exception as e:
                        print(e)
                        continue

            reguest = requests.get(baseUrl+'type=recent')
            split = reguest.text.split(',')
            if(reguest.status_code == 200):
                if(split[1] > initialdateSeismic and initialdateSeismic != "error"):
                    initialdateSeismic = split[0]
                    try:
                        await seismChannel.send("```A fost inregistrata o noua intrare. Data inregistrare: " + split[0] + ", magnitudine: " + split[1] + ", " + split[2] + " 🌋```")
                    except Exception as e:
                        print(e)
                        continue
            time.sleep(4)

client = MyClient()
client.run(clientToken)
