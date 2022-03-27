import argparse
from passet_bot import PassetBot

parser = argparse.ArgumentParser()
parser.add_argument('--start_url', '-s', type=str, required=True)
parser.add_argument('--first_name', '-f', type=str, required=True)
parser.add_argument('--last_name', '-l', type=str, required=True)
parser.add_argument('--email', '-e', type=str, required=True)
parser.add_argument('--phone', '-p', type=str, required=True)
parser.add_argument('--latest_date', '-d', type=str, required=True)
parser.add_argument('--driver_path', '-dr', type=str, required=True)

# parse arguments
args = vars(parser.parse_args())
bot = PassetBot(**args)
try:
    bot.start_session()
except Exception as e:
    print(e)
    print('Retrying...')
    bot.start_session()
