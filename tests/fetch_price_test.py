from avanza import Avanza, TimePeriod, InstrumentType, OrderType, TransactionType, ChannelType
import json
import base64
import getpass
import pickle
import asyncio
import logging
import sys

from datetime import date, datetime
# from dateutil.relativedelta import relativedelta

# Load credentials from secure storage

import keyring

user = 'purrepirre'
pwd=keyring.get_password('AVANZA_PASSW','purrepirre')
totp= keyring.get_password('AVANZA_KEY','purrepirre')

avanza = Avanza({
    'username': user,
    'password': pwd,
    'totpSecret': totp
})

def callback(data):
    # Do something with the quotes data here
    print('---------------  callback data: ')
    print(data)

async def subscribe_to_channel(avanza: Avanza):
    await avanza.subscribe_to_id(
        ChannelType.ORDERDEPTHS,
        "1019879",
        callback
    )

def main():
    loglevel = logging.DEBUG
    logging.basicConfig(stream=sys.stdout, level=loglevel, format='%(asctime)s %(levelname)s:%(name)s:%(funcName)s:%(message)s')

    asyncio.get_event_loop().run_until_complete(
        subscribe_to_channel(avanza)
    )
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()