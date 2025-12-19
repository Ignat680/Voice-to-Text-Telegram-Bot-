🎤 Voice-to-Text-Telegram-BotA Telegram bot designed to automatically convert incoming voice messages into text messages. The bot utilizes a selected Speech Recognition API (e.g., Google Speech Recognition or OpenAI Whisper) for processing.✨ FeaturesAutomatic Recognition: Transcribes voice messages sent in private chats or groups where the bot is active.Language Support: Possibility to configure the recognition language (e.g., Russian, English).Ease of Use: Users simply need to send a voice message to receive the transcription.🛠 Installation and Setup

1. Cloning the RepositoryBashgit clone https://github.com/YOUR_USERNAME/Voice-to-Text-Telegram-Bot.git
cd Voice-to-Text-Telegram-Bot

2. Setting up the Environment and DependenciesNote: The pydub library requires FFmpeg to be installed on your system.Bashpython -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate     # Windows
pip install -r requirements.txt

3. ConfigurationCreate a config.py file and add your Telegram Bot Token and any necessary Speech API keys. Make sure this file is listed in .gitignore!Python# config.py
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
# SPEECH_API_KEY = "YOUR_API_KEY"

4. Running the BotBashpython bot.py
📝 Key Files (for Reference)File NamePurposebot.pyMain bot logic (handling messages, downloading, converting audio, and transcription).config.pyStores secret credentials (Bot Token).requirements.txtLists all Python dependencies (python-telegram-bot, pydub, SpeechRecognition)..gitignoreEnsures that the virtual environment and config.py are not uploaded to GitHub.

4. Running the BotBashpython bot.py
📝 Key Files (for Reference)File NamePurposebot.pyMain bot logic (handling messages, downloading, converting audio, and transcription).config.pyStores secret credentials (Bot Token).requirements.txtLists all Python dependencies (python-telegram-bot, pydub, SpeechRecognition)..gitignoreEnsures that the virtual environment and config.py are not uploaded to GitHub.
