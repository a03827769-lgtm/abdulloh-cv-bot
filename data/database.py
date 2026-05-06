import aiosqlite
from config import DATABASE_PATH
import os

async def init_db():
    """Initializes the database and creates tables if they don't exist."""
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                full_name TEXT,
                language_code TEXT DEFAULT 'uz',
                joined_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                text TEXT,
                response TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        await db.commit()

async def log_message(user_id: int, text: str, response: str):
    """Logs user messages and AI responses for analytics."""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute('''
            INSERT INTO messages (user_id, text, response)
            VALUES (?, ?, ?)
        ''', (user_id, text, response))
        await db.commit()

async def add_user(user_id: int, username: str, full_name: str):
    """Adds a new user to the database."""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute('''
            INSERT OR IGNORE INTO users (user_id, username, full_name)
            VALUES (?, ?, ?)
        ''', (user_id, username, full_name))
        await db.commit()

async def get_user_count():
    """Returns the total number of users."""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute('SELECT COUNT(*) FROM users') as cursor:
            row = await cursor.fetchone()
            return row[0] if row else 0

async def set_user_language(user_id: int, lang_code: str):
    """Updates user language preference."""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute('UPDATE users SET language_code = ? WHERE user_id = ?', (lang_code, user_id))
        await db.commit()

async def get_user_language(user_id: int) -> str:
    """Returns user's selected language."""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute('SELECT language_code FROM users WHERE user_id = ?', (user_id,)) as cursor:
            row = await cursor.fetchone()
            return row[0] if row else 'uz'
async def get_all_users():
    """Returns all user IDs for broadcasting."""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute('SELECT user_id FROM users') as cursor:
            rows = await cursor.fetchall()
            return [row[0] for row in rows]

async def get_detailed_stats():
    """Returns comprehensive analytics for the admin."""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        # Total messages
        async with db.execute('SELECT COUNT(*) FROM messages') as c:
            msg_count = (await c.fetchone())[0]
        # AI specific questions (those starting with AI tag or from AI mode)
        async with db.execute('SELECT COUNT(*) FROM messages WHERE text NOT LIKE "/%"') as c:
            ai_count = (await c.fetchone())[0]
        return {
            "messages": msg_count,
            "ai_queries": ai_count
        }

async def get_recent_users(limit=10):
    """Returns the list of most recent users."""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute('SELECT user_id, full_name, username FROM users ORDER BY joined_at DESC LIMIT ?', (limit,)) as cursor:
            return await cursor.fetchall()
