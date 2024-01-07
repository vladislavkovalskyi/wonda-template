from wonda import Blueprint, Message, Command

from src.database import User
from src.keyboards import Inline

bp = Blueprint()


@bp.on.message(Command("start"))
async def start_handler(message: Message, user: User):
    await message.answer(
        f"👀 Hi, @{user.username}, i'm your bot written in wonda",
        reply_markup=Inline.start,
    )
