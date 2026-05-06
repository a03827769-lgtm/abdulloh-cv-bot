import time
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject
from data.database import log_message

class ThrottlingMiddleware(BaseMiddleware):
    """Simple rate-limiting middleware to prevent spam."""
    def __init__(self, limit: float = 0.8):
        self.limit = limit
        self.last_handled: Dict[int, float] = {}
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        if not isinstance(event, Message):
            return await handler(event, data)

        user_id = event.from_user.id
        current_time = time.time()

        if user_id in self.last_handled:
            if current_time - self.last_handled[user_id] < self.limit:
                return # Drop the message silently or send alert

        self.last_handled[user_id] = current_time
        return await handler(event, data)

class LoggingMiddleware(BaseMiddleware):
    """Middleware for logging every interaction."""
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        # Before handler
        res = await handler(event, data)
        # After handler - analytics can be added here
        return res
