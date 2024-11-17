import googletrans
from vosk import Model, KaldiRecognizer  # оффлайн-распознавание от Vosk
import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)
import pyttsx3  # синтез речи (Text-To-Speech)
import wave  # создание и чтение аудиофайлов формата wav
import json  # работа с json-файлами и json-строками
import os  # работа с файловой системой
import webbrowser
from datetime import datetime
import time
import yandexGPT
import socket
import clipboard
import logging
import cv2cam
import face_model_test
from tkinter import *
from tkinter import ttk
import multiprocessing as mp
from pygame import mixer

class VoiceAssistant:
    """
    Настройки голосового ассистента, включающие имя, пол, язык речи
    """
    name = ""
    sex = ""
    speech_language = ""
    recognition_language = ""


def setup_assistant_voice():
    """
    Установка голоса по умолчанию (индекс может меняться в 
    зависимости от настроек операционной системы)
    """
    voices = ttsEngine.getProperty("voices")

    if assistant.speech_language == "en":
        assistant.recognition_language = "en-US"
        if assistant.sex == "female":
            # Microsoft Zira Desktop - English (United States)
            ttsEngine.setProperty("voice", voices[1].id)
        else:
            # Microsoft David Desktop - English (United States)
            ttsEngine.setProperty("voice", voices[2].id)
    else:
        assistant.recognition_language = "ru-RU"
        # Microsoft Irina Desktop - Russian
        ttsEngine.setProperty("voice", voices[0].id)


def play_voice_assistant_speech(text_to_speech):
    """
    Проигрывание речи ответов голосового ассистента (без сохранения аудио)
    :param text_to_speech: текст, который нужно преобразовать в речь
    """
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()


def record_and_recognize_audio(*args: tuple):
    """
    Запись и распознавание аудио
    """
    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        # использование online-распознавания через Google 
        # (высокое качество распознавания)
        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        # в случае проблем с доступом в Интернет происходит 
        # попытка использовать offline-распознавание через Vosk
        except speech_recognition.RequestError:
            print("Trying to use offline recognition...")
            recognized_data = use_offline_recognition()

        return recognized_data


def use_offline_recognition():
    """
    Переключение на оффлайн-распознавание речи
    :return: распознанная фраза
    """
    recognized_data = ""
    try:
        # проверка наличия модели на нужном языке в каталоге приложения
        if not os.path.exists("models/vosk-model-small-ru-0.4"):
            print("Please download the model from:\n"
                  "https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
            exit(1)

        # анализ записанного в микрофон аудио (чтобы избежать повторов фразы)
        wave_audio_file = wave.open("microphone-results.wav", "rb")
        model = Model("models/vosk-model-small-ru-0.4")
        offline_recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())

        data = wave_audio_file.readframes(wave_audio_file.getnframes())
        if len(data) > 0:
            if offline_recognizer.AcceptWaveform(data):
                recognized_data = offline_recognizer.Result()

                # получение данных распознанного текста из JSON-строки 
                # (чтобы можно было выдать по ней ответ)
                recognized_data = json.loads(recognized_data)
                recognized_data = recognized_data["text"]
    except:
        print("Sorry, speech service is unavailable. Try again later")

    return recognized_data







def search_for_term_on_yandex(*args: tuple):
    """
    Поиск видео на YouTube с автоматическим открытием ссылки на список результатов
    :param args: фраза поискового запроса
    """
    if not args[0]: return
    search_term = " ".join(args[0])
    url = "https://www.yandex.ru/search/?text=" + search_term
    webbrowser.get().open(url)

    # для мультиязычных голосовых ассистентов лучше создать 
    # отдельный класс, который будет брать перевод из JSON-файла
    play_voice_assistant_speech("Сейчас найду по запросу " + search_term)



def translate_google(*args: tuple):
    # Создаем переводчик
    translator = googletrans.Translator()

    # Задаем исходные язык и целевой язык
    src = 'en'
    dest = 'ru'

    # Задаем исходный текст
    if args[0]: 
        translate_term = " ".join(args[0])

    # Переводим текст
        translated_text = translator.translate(translate_term, src=src, dest=dest).text

        play_voice_assistant_speech("Сейчас")
        time.sleep(0.1)
        play_voice_assistant_speech("Перевожу")
        time.sleep(2)
        play_voice_assistant_speech(translated_text)
    else:
        play_voice_assistant_speech("Скажите что-нибудь")
        voice_input = record_and_recognize_audio()
        os.remove("microphone-results.wav")
        print(voice_input) 
        translate_google([voice_input])


def translate_google1(*args: tuple):
    # Создаем переводчик
    translator = googletrans.Translator()

    # Задаем исходные язык и целевой язык
    src = 'ru'
    dest = 'en'

    # Задаем исходный текст
    if args[0]: 
        translate_term = " ".join(args[0])

    # Переводим текст
        translated_text = translator.translate(translate_term, src=src, dest=dest).text

        play_voice_assistant_speech("Сейчас")
        time.sleep(0.1)
        play_voice_assistant_speech("Перевожу")
        time.sleep(2)
        play_voice_assistant_speech(translated_text)
    else:
        play_voice_assistant_speech("Скажите что-нибудь")
        voice_input = record_and_recognize_audio()
        os.remove("microphone-results.wav")
        print(voice_input) 
        translate_google([voice_input])


def translate_google2(*args: tuple):
    # Создаем переводчик
    translator = googletrans.Translator()

    # Задаем исходные язык и целевой язык
    src = 'ru'
    dest = 'en'
    text = clipboard.clip_board_text()
    # Задаем исходный текст
    if text: 

    # Переводим текст
        translated_text = translator.translate(text, src=src, dest=dest).text

        play_voice_assistant_speech("Сейчас")
        time.sleep(0.1)
        play_voice_assistant_speech("Перевожу")
        time.sleep(2)
        assistant.speech_language = "en"
        setup_assistant_voice()
        play_voice_assistant_speech(translated_text)
        assistant.speech_language = "ru"
        setup_assistant_voice()
    else:
        play_voice_assistant_speech("В буфере обмена нет текста")
        voice_input = record_and_recognize_audio()
        os.remove("microphone-results.wav")
        print(voice_input) 
        translate_google2([voice_input])


def translate_google3(*args: tuple):
    # Создаем переводчик
    translator = googletrans.Translator()

    # Задаем исходные язык и целевой язык
    src = 'en'
    dest = 'ru'
    text = clipboard.clip_board_text()
    # Задаем исходный текст
    if text: 

    # Переводим текст
        translated_text = translator.translate(text, src=src, dest=dest).text

        play_voice_assistant_speech("Сейчас")
        time.sleep(0.1)
        play_voice_assistant_speech("Перевожу")
        time.sleep(2)
        translate_term = " ".join(args[0])
        print(translated_text)
        play_voice_assistant_speech(translated_text)
    else:
        play_voice_assistant_speech("В буфере обмена нет текста")
        voice_input = record_and_recognize_audio()
        os.remove("microphone-results.wav")
        print(voice_input) 
        translate_google3([voice_input])


def talkingEnid(*args: tuple):
    if args[0]:
        translate_term = " ".join(args[0])
        play_voice_assistant_speech(translate_term)
    else:
        play_voice_assistant_speech("Скажите что-нибудь")
        voice_input = record_and_recognize_audio()
        talkingEnid([voice_input])


def music_start(*args: tuple):
    mixer.init()
    mixer.music.load(r"C:\Users\salim\GetFiles\Files\Musics\Eminem_-_Lose_Yourself_47829428.mp3")
    mixer.music.play()


def music_stop(*args: tuple):
    mixer.music.stop()



commands = {
    ("найди", "открой"): search_for_term_on_yandex,
    ("переведи", "перевети"): translate_google,
    ("повтори", "попробуй сказать"): talkingEnid,
    ("как будет", "как перевести"): translate_google1,
    ("буфер на английский", "буфер обмена на английский"): translate_google2,
    ("буфер с английского", "буфер обмена с английского"): translate_google3,
    ("включи музыку", "где музыка"): music_start,
    ("выключи музыку", "вырубай"): music_stop,
}


def execute_command_with_name(command_name: str, *args: list):
    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
        else:
            pass  # print("Command not found")

def starterE2():
    os.system(r"python Enid2.py")

if __name__ == "__main__":

    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    # инициализация инструмента синтеза речи
    ttsEngine = pyttsx3.init()

    # настройка данных голосового помощника
    assistant = VoiceAssistant()
    assistant.name = "Enid"
    assistant.sex = "female"
    assistant.speech_language = "ru"

    # установка голоса по умолчанию
    setup_assistant_voice()
    

    while True:
        
        count = 0
        res = cv2cam.camera_walk()
        if res:
            res = face_model_test.SalimID(r"C:\Users\salim\GetFiles\face_photo\now_photo\image.jpg")
            os.remove(r"C:\Users\salim\GetFiles\face_photo\now_photo\image.jpg")
            if not res:
                play_voice_assistant_speech("Лицо не распознано")
                print("Лицо не распознано")
                count += 1
                if count == 5:
                    
 
                    root = Tk()
                    root.title("FacaID")
                    root.geometry("250x200")
 
                    label = ttk.Label(text="Уходи", font=("Arial", 14))
                    label.pack()
 
                    root.mainloop()
                    time.sleep(2)
                    root.destroy()
            elif res:
                play_voice_assistant_speech("Лицо распознано")
                break
        
           

    if datetime.now().hour > 11 and datetime.now().hour < 18:
        play_voice_assistant_speech("Добрый день, Салим!")
    elif datetime.now().hour <= 11:
        play_voice_assistant_speech("Доброе утро, Салим!")
    elif datetime.now().hour >= 18:
        play_voice_assistant_speech("Добрый вечер, Салим!")

    

    print("post enid2")
    while True:
        # старт записи речи с последующим выводом распознанной речи
        # и удалением записанного в микрофон аудио
        
        voice_input = record_and_recognize_audio()
        if os.path.exists("microphone-results.wav"):
            os.remove("microphone-results.wav")
        print(voice_input)

        print("speaking START")
        voice_words = ""
    # отделение комманд от дополнительной информации (аргументов)
        if voice_input:
            voice_words = voice_input.split(" ")
    
        if voice_input == "привет":
            play_voice_assistant_speech("Здравствуй")

        if voice_input == "как дела":
            play_voice_assistant_speech("всё хорошо")
    
        if voice_input == "ты умная":
            play_voice_assistant_speech("нет конечно")
        
        if voice_input == "пока":
            play_voice_assistant_speech("досвиданье")

        if voice_input == "подбодри" or voice_input == "подбодрить":
            play_voice_assistant_speech("вы самое никчёмное, безполезное существо, которое я когда-либо видела")

        if voice_input == "как тебя зовут":
            play_voice_assistant_speech("меня зовут энид, я ваш виртуальный помошник")

        if voice_input == "энид":
            play_voice_assistant_speech("Да, я слушаю")
        

        if voice_input == "спасибо":
            play_voice_assistant_speech("пожалуйста")
        
    
        # отделение комманд от дополнительной информации (аргументов)
        for  i in list(commands.keys()):
            for j in i:
                if j in voice_input:
                    param = voice_input.split(j)[1].split(" ")
                    print("Я в экзекутере")
                    execute_command_with_name(j, param)


        wordy = yandexGPT.get_words(voice_input)
        print(wordy)
        play_voice_assistant_speech(wordy)
        


        
        

        
    
    
                        
        
        
        
        
