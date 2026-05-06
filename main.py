import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, ErrorEvent
from config import BOT_TOKEN
from handlers import router
from data.database import init_db
from middlewares import AntiFloodMiddleware


async def set_bot_commands(bot: Bot):
    """Register bot commands so they appear when user types '/'."""
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="help", description="Buyruqlar ro'yxati"),
        BotCommand(command="about", description="Men haqimda"),
        BotCommand(command="portfolio", description="Portfolio"),
        BotCommand(command="contact", description="Aloqa ma'lumotlari"),
        BotCommand(command="language", description="Tilni o'zgartirish"),
    ]
    await bot.set_my_commands(commands)


async def main():
    """Main function to run the bot."""
    # Logging (before everything else)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stdout
    )

    # Initialize database
    await init_db()

    # Initialize Bot and Dispatcher
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Register Middlewares
    dp.message.middleware(AntiFloodMiddleware(time_limit=1))

    # Register router
    dp.include_router(router)

    # Global Error Handler
    @dp.error()
    async def error_handler(event: ErrorEvent):
        logging.error(f"Unhandled error: {event.exception}", exc_info=True)
        return True

    # Register bot commands (shows in "/" menu)
    await set_bot_commands(bot)

    logging.info("Bot is starting...")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped by user.")
