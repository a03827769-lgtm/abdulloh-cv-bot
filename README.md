# Elite CV Ecosystem: Abdulloh Muhammadjonov

This is a professional AI-powered Telegram Bot and Portfolio Mini App ecosystem.

## 🚀 Quick Start

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment:**
   - Copy `.env.example` to `.env`
   - Fill in your `BOT_TOKEN` from @BotFather.
   - Fill in your `GROQ_API_KEY` from Groq Cloud.
   - Set your `ADMIN_ID`.

3. **Run the Bot:**
   ```bash
   python main.py
   ```

## 🛠 Features

- **AI Strategist:** Multilingual AI chat with voice message support (Whisper).
- **Portfolio Mini App:** Modern, high-end web portfolio integrated into Telegram.
- **Lead Scoring:** Automatically evaluates potential clients based on project details.
- **PDF CV Generator:** Generates a professional resume on the fly.
- **Admin Panel:** /admin command for stats and broadcasting to all users.

## 🌐 Deployment

### Bot (Railway/Heroku)
- Uses the provided `Procfile`.
- Ensure all environment variables from `.env` are set in your platform's dashboard.

### Website (Vercel)
- Connect your repository to Vercel.
- It will automatically use `index.html` and `vercel.json`.
- Update `WEB_APP_URL` in your `.env` to the deployed Vercel URL.

## 👨‍💻 Author
**Abdulloh Muhammadjonov**
- Telegram: @abdulloh_ai
- Web: abdullohvfx.online
