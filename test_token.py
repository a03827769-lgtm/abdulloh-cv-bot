import asyncio
from aiogram import Bot

async def test():
    token = "8610845449:AAGr1BXXsyFE9IW0j0PAV1cQBKYX0pqdgBI"
    bot = Bot(token=token)
    try:
        me = await bot.get_me()
        print(f"SUCCESS: Bot is working as @{me.username}")
    except Exception as e:
        print(f"ERROR: {str(e)}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(test())
