from telegram import Update
from telegram.ext import Application, CommandHandler
import uuid


# Функция для генерации ссылки
def generate_brawlstar_link():
    unique_code = str(uuid.uuid4())
    url = f"https://link.brawlstars.com/?action=voucher&code={unique_code}"
    return url


# Команда /generate
async def generate(update: Update, context):
    link = generate_brawlstar_link()
    await update.message.reply_text(f"Вот твоя уникальная ссылка: {link}")


# Основная функция для запуска бота
def main():
    # Токен твоего бота
    TOKEN = "8182616774:AAHF_kHP6mJcfo0d6-MUJCvJWH0nQ14Oxo0"

    # Создаём приложение для бота
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчик команды /generate
    application.add_handler(CommandHandler("generate", generate))

    # Запускаем бота
    application.run_polling()


if __name__ == '__main__':
    main()
