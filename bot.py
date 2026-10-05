import os
import re
import tempfile
import asyncio

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "هلا بيك 👋\n\n"
        "دزلي رابط فيديو TikTok أو Instagram عام، "
        "وأحاول أجهزلك الفيديو للتحميل.\n\n"
        "الأمر /help للمساعدة."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📥 طريقة الاستخدام:\n\n"
        "1. انسخ رابط فيديو TikTok أو Instagram.\n"
        "2. دزه هنا.\n"
        "3. البوت يعالج الرابط ويرسل الفيديو إذا كان متاحاً.\n\n"
        "ملاحظة: استخدم البوت للمحتوى الذي تملك حق تنزيله أو إعادة استخدامه."
    )


async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if not re.search(r"(tiktok\.com|instagram\.com)", text, re.IGNORECASE):
        await update.message.reply_text(
            "❌ دز رابط
