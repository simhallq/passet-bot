from passet_bot import PassetBot
bot = PassetBot(start_url='https://bokapass.nemoq.se/Booking/Booking/Index/uppsala', first_name='Simon',
                last_name='Hällqvist', email='hallqvist.simon@gmail.com', phone='0739609843', latest_date='2019-04-15', driver_path='/Users/simon/Downloads/chromedriver 3')
bot.start_session()
