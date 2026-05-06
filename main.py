import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN
from handlers import router
from middlewares import ThrottlingMiddleware, LoggingMiddleware
from data.database import init_db

# Configure Professional Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("data/bot.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

async def main():
    """Entry point for the Master CV Bot."""
    # Initialize Database
    await init_db()
    
    # Initialize Bot & Dispatcher
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Register Middlewares (Anti-Spam & Analytics)
    dp.message.middleware(ThrottlingMiddleware())
    dp.update.outer_middleware(LoggingMiddleware())

    # Register Routers
    dp.include_router(router)

    logger.info("✦ MASTER CV BOT IS ONLINE ✦")
    
    try:
        # Start Polling
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        logger.error(f"Critical Error: {e}")
    finally:
        await bot.session.close()
        logger.info("✦ BOT SHUTDOWN ✦")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
