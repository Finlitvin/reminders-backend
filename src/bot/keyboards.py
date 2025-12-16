from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from database import DATABASE


LIST_BUTTON_CALLBACK = "list_button"
SECTION_BUTTON_CALLBACK = "section_button"
REMINDER_BUTTON_CALLBACK = "reminder_button"


def reminder_list_keyboard() -> InlineKeyboardMarkup:
    buttons = []

    for list_value in DATABASE.get("reminder_list"):
        buttons.append(
            [
                InlineKeyboardButton(
                    f"{list_value.get("icon")} {list_value.get("name")}",
                    callback_data=f"{LIST_BUTTON_CALLBACK}#{list_value.get('id')}",
                )
            ]
        )
    inline_keyboard = InlineKeyboardMarkup(buttons)

    return inline_keyboard


def section_list_keyboard(sections: list) -> InlineKeyboardMarkup:
    buttons = []

    for section in sections:
        buttons.append(
            [
                InlineKeyboardButton(
                    section.get("name"),
                    callback_data=f"{SECTION_BUTTON_CALLBACK}#{section.get('id')}",
                )
            ]
        )

    inline_keyboard = InlineKeyboardMarkup(buttons)

    return inline_keyboard


def reminder_keyboard(reminders: list):
    buttons = []

    for reminder in reminders:
        buttons.append(
            [
                InlineKeyboardButton(
                    reminder.get("tittle"),
                    callback_data=f"{REMINDER_BUTTON_CALLBACK}#{reminder.get('id')}",
                )
            ]
        )

    inline_keyboard = InlineKeyboardMarkup(buttons)

    return inline_keyboard
