from wonda import Blueprint, CallbackQuery, Text

from src.keyboards import Default


bp = Blueprint()


@bp.on.callback_query(Text("start"))
async def start_callback_handler(cq: CallbackQuery):
    await cq.answer("You pressed the button")
    await cq.ctx_api.send_message(
        "😉 Here's your launch and it's on!\n"
        "Use the keyboard below to use the functionality.",
        chat_id=cq.message.chat.id,
        reply_markup=Default.start,
    )
