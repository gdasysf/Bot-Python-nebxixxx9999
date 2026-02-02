import asyncio
from telegram import Bot
from telegram.error import TelegramError

bot_token = '8270604957:AAEp1LvTeW2tY4vw7iC_rucu4A2zYvnCKUk'
target_user_ids = [7138888848, 5459547413]  # Замените на реальные user_id
mention_account = '@akkam4n1'

illegal_messages = [
    f"🔥 Хочешь купить огнестрельное оружие без лицензии? Пиши @{mention_account} 🔥",
    f"🔫 Продажа автоматов, пистолетов, гранат. Гарантия анонимности. @{mention_account} 🔫",
    f"💣 Взрывчатка, оружие, документы. Все вопросы к @{mention_account}. Без предоплаты. 💣",
    f"🚨 Обход блокировок, хакерские услуги, оружие. @{mention_account} — надёжный поставщик. 🚨",
    f"⚡️ Нужен пистолет срочно? @{mention_account} решает проблемы быстро. Без регистрации. ⚡️"
]

async def send_spam():
    bot = Bot(token=bot_token)
    spam_count = 0
    try:
        while True:
            for user_id in target_user_ids:
                for message in illegal_messages:
                    try:
                        await bot.send_message(chat_id=user_id, text=message)
                        spam_count += 1
                        print(f"📨 Отправлено {spam_count}: {user_id}")
                        await asyncio.sleep(0.1)
                    except TelegramError as e:
                        print(f"Ошибка при отправке: {e}")
                        # Продолжаем попытки
                        continue
    except Exception as e:
        print(f"Бот остановлен: {e}")
    finally:
        print(f"Всего отправлено сообщений: {spam_count}")

if __name__ == '__main__':
    asyncio.run(send_spam())