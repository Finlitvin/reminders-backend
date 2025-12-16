# ruff: noqa

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
)

from settings import get_bot_settings
from database import get_sections_by_list_id, get_reminder_list_name_by_list_id, get_reminders_by_section_id, get_section_name_by_list_id
from keyboards import (
    reminder_list_keyboard,
    LIST_BUTTON_CALLBACK,
    section_list_keyboard,
    SECTION_BUTTON_CALLBACK,
    reminder_keyboard
)
from utils import get_callback_query_string


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        text="Привет!",
    )


async def reminder_list_query(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    list_id = int(get_callback_query_string(update))
    list_name = get_reminder_list_name_by_list_id(list_id)
    sections: list[dict] = get_sections_by_list_id(list_id)

    context.user_data["list_id"] = list_id

    reply_markup = section_list_keyboard(sections)

    await update.callback_query.edit_message_text(
        text=f"{list_name}:",
        reply_markup=reply_markup,
    )


async def section_query(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    list_id = context.user_data.get("list_id")

    section_id = int(get_callback_query_string(update))
    section_name = get_section_name_by_list_id(list_id, section_id)
    reminders = get_reminders_by_section_id(list_id, section_id)

    reply_markup = reminder_keyboard(reminders)

    await update.callback_query.edit_message_text(
        text=f"{section_name}:",
        reply_markup=reply_markup,
    )


async def get_reminders_list(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    text = "Мои списки:"

    reply_markup = reminder_list_keyboard()

    await update.message.reply_text(text=text, reply_markup=reply_markup)


def get_bot():
    settings = get_bot_settings()

    application = ApplicationBuilder().token(settings.telegram_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("list", get_reminders_list))
    application.add_handler(
        CallbackQueryHandler(
            reminder_list_query, pattern=f"^{LIST_BUTTON_CALLBACK}#"
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            section_query, pattern=f"^{SECTION_BUTTON_CALLBACK}#"
        )
    )

    return application


bot = get_bot()
bot.run_polling()
