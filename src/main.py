import argparse
from passet_bot import PassetBot

args = argparse.ArgumentParser()
args.add_argument('--start_url', '-s', type=str, required=True)
args.add_argument('--latest_date', '-d', type=str, required=True)
# parse arguments
args = args.parse_args()
# get arguments
start_url = args.start_url
latest_date = args.latest_date

bot = PassetBot(start_url=start_url, first_name='Simon',
                last_name='Hällqvist', email='hallqvist.simon@gmail.com', phone='0739609843', latest_date=latest_date, driver_path='/Users/simon/Downloads/chromedriver 3')
bot.start_session()
