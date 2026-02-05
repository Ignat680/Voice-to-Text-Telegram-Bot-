import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_BOT_TOKEN
import io
from pydub import AudioSegment
import speech_recognition as sr

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Инициализация распознавателя речи
r = sr.Recognizer()

# --- Обработчики команд ---

async def start_command(update: Update, context) -> None:
    """Отвечает на команду /start."""
    await update.message.reply_text(
        'Привет! Отправь мне голосовое сообщение, и я преобразую его в текст.'
    )

# --- Обработчик голосовых сообщений ---

async def voice_to_text(update: Update, context) -> None:
    """Обрабатывает голосовое сообщение, преобразует его в текст и отправляет обратно."""
    
    chat_id = update.message.chat_id
    voice = update.message.voice
    
    if not voice:
        return

    await context.bot.send_message(
        chat_id=chat_id,
        text="Получено голосовое сообщение. Начинаю обработку..."
    )

    try:
        # 1. Загрузка файла
        file_id = voice.file_id
        file = await context.bot.get_file(file_id)
        
        # Загрузка файла в память
        voice_data = io.BytesIO()
        await file.download_to_memory(voice_data)
        voice_data.seek(0)
        
        # 2. Конвертация (Telegram использует OGG, нужен WAV для SpeechRecognition)
        audio = AudioSegment.from_file(voice_data, format="ogg")
        
        wav_io = io.BytesIO()
        audio.export(wav_io, format="wav")
        wav_io.seek(0)
        
        # 3. Распознавание речи
        with sr.AudioFile(wav_io) as source:
            audio_data = r.record(source)
            
            # Используем Google Web Speech API (не требует ключа, но имеет ограничения)
            # Для коммерческих проектов или больших объемов лучше использовать платные API (Yandex, Google Cloud, Whisper)
            text = r.recognize_google(audio_data, language="ru-RU") 

        # 4. Отправка результата
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"**Распознанный текст:**\n\n_{text}_"
        )
        
    except sr.UnknownValueError:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Не удалось распознать речь. Попробуйте еще раз."
        )
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"Произошла техническая ошибка при обработке: {e}"
        )

# --- Главная функция запуска ---

def main() -> None:
    """Запуск бота."""
    
    # 1. Создание объекта Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # 2. Добавление обработчиков
    application.add_handler(CommandHandler("start", start_command))
    
    # Добавляем фильтр для голосовых сообщений
    application.add_handler(MessageHandler(filters.Voice(), voice_to_text))

    # 3. Запуск бота
    logger.info("Бот запущен!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
       # 3. Запуск бота
    logger.info("Бот запущен!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
       # 3. Запуск бота
    logger.info("Бот запущен!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


