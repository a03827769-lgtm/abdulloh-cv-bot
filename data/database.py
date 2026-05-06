import aiosqlite
import os
from datetime import datetime

DATABASE_PATH = 'data/analytics.db'

async def init_db():
    """Initializes the Master Analytics database."""
    if not os.path.exists('data'):
        os.makedirs('data')
        
    async with aiosqlite.connect(DATABASE_PATH) as db:
        # Users table with advanced tracking
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                full_name TEXT,
                language TEXT DEFAULT 'uz',
                last_active TIMESTAMP,
                joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        # Message and Action logs
        await db.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                action TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        # AI Conversations
        await db.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                role TEXT,
                text TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Migration: Add missing columns if they don't exist
        columns_to_add = [
            ('language', "TEXT DEFAULT 'uz'"),
            ('last_active', "TIMESTAMP"),
            ('joined_at', "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
        ]
        
        for col_name, col_type in columns_to_add:
            try:
                await db.execute(f'ALTER TABLE users ADD COLUMN {col_name} {col_type}')
            except:
                pass # Column already exists
            
        await db.commit()

async def add_user(user_id: int, username: str, full_name: str):
    """Adds or updates a user in the Master Database."""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        now = datetime.now().isoformat()
        await db.execute('''
            INSERT INTO users (user_id, username, full_name, last_active) 
            VALUES (?, ?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET 
                username=excluded.username, 
                full_name=excluded.full_name,
                last_active=excluded.last_active
        ''', (user_id, username, full_name, now))
        await db.commit()

async def log_action(user_id: int, action: str):
    """Logs every specific action for analytics (e.g., 'Clicked Portfolio')."""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute('INSERT INTO logs (user_id, action) VALUES (?, ?)', (user_id, action))
        await db.commit()

async def get_user_language(user_id: int) -> str:
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute('SELECT language FROM users WHERE user_id = ?', (user_id,)) as cursor:
            row = await cursor.fetchone()
            return row[0] if row else 'uz'

async def set_user_language(user_id: int, lang: str):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute('UPDATE users SET language = ? WHERE user_id = ?', (lang, user_id))
        await db.commit()

async def log_message(user_id: int, text: str, response: str):
    """Logs AI conversations for history and refinement."""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute('INSERT INTO messages (user_id, role, text) VALUES (?, ?, ?)', (user_id, 'user', text))
        await db.execute('INSERT INTO messages (user_id, role, text) VALUES (?, ?, ?)', (user_id, 'assistant', response))
        await db.commit()

async def get_user_count():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute('SELECT COUNT(*) FROM users') as cursor:
            return (await cursor.fetchone())[0]

async def get_all_users():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute('SELECT user_id FROM users') as cursor:
            rows = await cursor.fetchall()
            return [row[0] for row in rows]

async def get_detailed_stats():
    """Returns Master-level stats for admin."""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute('SELECT COUNT(*) FROM users') as c:
            u_count = (await c.fetchone())[0]
        async with db.execute('SELECT COUNT(*) FROM messages') as c:
            m_count = (await c.fetchone())[0]
        # Most popular action
        async with db.execute('SELECT action, COUNT(action) as c FROM logs GROUP BY action ORDER BY c DESC LIMIT 1') as c:
            pop = await c.fetchone()
            pop_action = f"{pop[0]} ({pop[1]})" if pop else "N/A"
            
        return {"users": u_count, "messages": m_count, "popular": pop_action}

async def get_recent_users(limit=10):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute('SELECT user_id, full_name, username FROM users ORDER BY last_active DESC LIMIT ?', (limit,)) as cursor:
            return await cursor.fetchall()
