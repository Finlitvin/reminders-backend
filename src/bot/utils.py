from telegram import Update


def get_callback_query_string(update: Update) -> str:
    res = update.callback_query.data.split("#")[1]
    return res


async def send_message_with_reply(update: Update):
    sender = None
    if update.message:
        sender = update.message.reply_text
    elif update.callback_query:
        sender = update.callback_query.edit_message_text
    return sender
