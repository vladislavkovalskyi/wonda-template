from wonda import Bot
from tortoise import Tortoise

from src import blueprints, middlewares
from src.config import *


async def setup_db() -> None:
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={"models": ["src.database.user"]},
    )
    await Tortoise.generate_schemas()

    print("Database initialized successfully!")


def setup_blueprints(bot: Bot) -> None:
    for bp in blueprints.bps:
        bp.load_into(bot)

    print("Blueprints loaded successfully!")


def setup_middlewares(bot: Bot) -> None:
    for bp in middlewares.bps:
        bp.load_into(bot)

    print("Middlewares loaded successfully!")


def setup_bot() -> Bot:
    bot = Bot(token=BOT_TOKEN)
    setup_blueprints(bot=bot)
    setup_middlewares(bot=bot)
    return bot
