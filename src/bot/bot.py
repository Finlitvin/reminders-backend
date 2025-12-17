# ruff: noqa

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
)

from settings import get_bot_settings
from database import (
    get_sections_by_list_id,
    get_reminder_list_name_by_list_id,
    get_reminders_by_section_id,
    get_section_name_by_list_id,
)
from keyboards import (
    reminder_list_keyboard,
    LIST_BUTTON_CALLBACK,
    section_list_keyboard,
    SECTION_BUTTON_CALLBACK,
    reminder_keyboard,
    REMINDER_BUTTON_CALLBACK,
    BACK_BUTTON_CALLBACK,
)
from handlers import error_handler
from utils import get_callback_query_string, send_message_with_reply


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        text="Привет!",
    )


async def show_sections_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    list_id = int(get_callback_query_string(update))
    list_name = get_reminder_list_name_by_list_id(list_id)
    sections: list[dict] = get_sections_by_list_id(list_id)

    context.user_data["list_id"] = list_id
    context.user_data["list_name"] = list_name

    reply_markup = section_list_keyboard(sections)

    await update.callback_query.edit_message_text(
        text=f"{list_name}:",
        reply_markup=reply_markup,
    )


async def show_reminders_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    list_id = context.user_data.get("list_id")
    list_name = context.user_data.get("list_name")

    section_id = int(get_callback_query_string(update))
    section_name = get_section_name_by_list_id(list_id, section_id)
    reminders = get_reminders_by_section_id(list_id, section_id)

    reply_markup = reminder_keyboard(reminders)

    await update.callback_query.edit_message_text(
        text=f"{list_name} -> {section_name}:",
        reply_markup=reply_markup,
    )


async def show_reminder_info_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    pass


async def show_reminder_list_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    
    text = "Мои списки:"

    reply_markup = reminder_list_keyboard()

    send_message = await send_message_with_reply(update)

    await send_message(text=text, reply_markup=reply_markup)


def get_bot():
    settings = get_bot_settings()

    application = ApplicationBuilder().token(settings.telegram_token).build()

    application.add_error_handler(error_handler)
    application.add_handler(CommandHandler("start", start))

    application.add_handler(CommandHandler("list", show_reminder_list_handler))
    application.add_handler(
        CallbackQueryHandler(
            show_reminder_list_handler, pattern=f"^{BACK_BUTTON_CALLBACK}#"
        )
    )

    application.add_handler(
        CallbackQueryHandler(
            show_sections_handler, pattern=f"^{LIST_BUTTON_CALLBACK}#"
        )
    )
    
    application.add_handler(
        CallbackQueryHandler(
            show_reminders_handler, pattern=f"^{SECTION_BUTTON_CALLBACK}#"
        )
    )

    application.add_handler(
        CallbackQueryHandler(
            show_reminder_info_handler, pattern=f"^{REMINDER_BUTTON_CALLBACK}#"
        )
    )

    return application


bot = get_bot()
bot.run_polling()
