from telegram import Update

def get_callback_query_string(update: Update) -> str:
    res = update.callback_query.data.split("#")[1]
    return res
