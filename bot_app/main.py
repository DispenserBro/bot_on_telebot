from starters.register_bot import bot
from starters.register_commands import register_all_handlers

bot = register_all_handlers(bot)
bot.infinity_polling(skip_pending=True)
