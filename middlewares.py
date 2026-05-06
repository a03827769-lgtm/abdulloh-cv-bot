from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from cachetools import TTLCache

class AntiFloodMiddleware(BaseMiddleware):
    """Middleware to prevent spamming the bot."""
    
    def __init__(self, time_limit: int = 2) -> None:
        self.limit = TTLCache(maxsize=10000, ttl=time_limit)
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        if isinstance(event, Message):
            user_id = event.from_user.id
            if user_id in self.limit:
                return await event.answer("⚠️ Iltimos, juda tez xabar yubormang. Biroz kuting.")
            self.limit[user_id] = True
            
        return await handler(event, data)
