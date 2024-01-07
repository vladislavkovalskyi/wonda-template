from wonda import Blueprint, ABCMiddleware, Message

from src.database import User

bp = Blueprint()


class Registration(ABCMiddleware[Message]):
    async def pre(self, message: Message, ctx: dict) -> bool:
        user, _ = await User.get_or_create(uid=message.from_.id, username=message.from_.username)
        ctx["user"] = user

        return True


bp.dispatcher.message.middlewares.append(Registration())
