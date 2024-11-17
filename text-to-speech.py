import pyttsx3

# Инициализация движка
engine = pyttsx3.init()

# Текст для синтеза
text = "Привет, как дела?"

# Синтез речи
engine.say(text)
engine.runAndWait()