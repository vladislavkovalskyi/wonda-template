from wonda.tools.keyboard import (
    ReplyKeyboardBuilder,
    InlineKeyboardBuilder,
    Callback,
    Button,
)


class Default:
    start = (
        ReplyKeyboardBuilder(resize_keyboard=True)
        .add(Button("I'm default button!"))
        .build()
    )


class Inline:
    start = (
        InlineKeyboardBuilder()
        .add(Callback("Click here to start", "start"))
        .build()
    )
