from wonda import LoopWrapper

from src.initialization import setup_bot, setup_db

bot = setup_bot()
bot.loop_wrapper = LoopWrapper(on_startup=[setup_db()])
