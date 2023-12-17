import pyautogui
import pytesseract
import keyboard
import time
import tkinter as tk
from threading import Thread
import pygame
import numpy as np


# Указываем путь к исполняемому файлу Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Определите координаты левого верхнего и правого нижнего углов области для поиска фразы "Клюёт"
x1_klyuet, y1_klyuet = 900, 190
x2_klyuet, y2_klyuet = 1040, 235

# Определите координаты левого верхнего и правого нижнего углов области для поиска фразы "Ловить рыбу"
x1_lovit_rybu, y1_lovit_rybu = 1078, 601
x2_lovit_rybu, y2_lovit_rybu = 1204, 629

# Фраза, которую мы ищем
target_phrase_klyuet = "Клюёт"
target_phrase_lovit_rybu = "Ловить рыбу"

# Флаг для отслеживания состояния работы
scanning = False

# Инициализация pygame
pygame.init()

# Параметры звукового сигнала
sample_rate = 44100  # Частота дискретизации (Гц)
duration = 5  # Продолжительность звука (секунды)
frequency = 440  # Частота (Гц)

# Создаем массив сэмплов для левого и правого каналов
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
left_signal = 0.5 * np.sin(2 * np.pi * frequency * t)
right_signal = 0.3 * np.sin(2 * np.pi * 2 * frequency * t)  # Второй гармонический сигнал

# Преобразуем сэмплы в формат, который можно воспроизвести с помощью pygame
stereo_signal = np.column_stack((left_signal, right_signal))
audio_data = np.int16(stereo_signal * 32767)

# Создаем аудиоканал и воспроизводим звук
pygame.mixer.init(frequency=sample_rate, size=-16, channels=2)
sound = pygame.sndarray.make_sound(audio_data)


# Функция для сканирования и поиска фраз
def scan_for_phrases():
    global scanning, attention
    while True:
        time.sleep(1)
        attention += 1
        print("Attention: ", attention)

        # Вырежем область с текстом для фразы "Ловить рыбу"
        screenshot = pyautogui.screenshot(region=(x1_lovit_rybu, y1_lovit_rybu, x2_lovit_rybu - x1_lovit_rybu, y2_lovit_rybu - y1_lovit_rybu))
        text_lovit_rybu = pytesseract.image_to_string(screenshot, lang='rus')

        # Проверим, содержит ли распознанный текст искомую фразу "Ловить рыбу"
        if target_phrase_lovit_rybu in text_lovit_rybu:
            attention = 0
            # Нажатие клавиши "E" (с явным указанием раскладки)
            keyboard.press_and_release("e")
            time.sleep(3)

        # Вырежем область с текстом для фразы "Клюёт"
        screenshot = pyautogui.screenshot(region=(x1_klyuet, y1_klyuet, x2_klyuet - x1_klyuet, y2_klyuet - y1_klyuet))
        text_klyuet = pytesseract.image_to_string(screenshot, lang='rus')

        # Проверим, содержит ли распознанный текст искомую фразу "Клюёт"
        if target_phrase_klyuet in text_klyuet:
            attention = 0
            # Последовательное нажатие клавиш "E" и "R" (с явным указанием раскладки)
            keyboard.press_and_release("e")
            time.sleep(1)
            keyboard.press_and_release("r")

        # Обновим статус работы
        status_label.config(text="В работе" if scanning else "Ожидание")

        # Проверяем, нажата ли клавиша F9 для завершения цикла
        if keyboard.is_pressed("F9"):
            break

        if attention >= 40:
            attention = 0
            sound.play()
            time.sleep(5)
            sound.stop()

# Функция для запуска сканирования
def start_scan():
    global scanning
    global attention
    attention = 0
    scanning = True
    scan_thread = Thread(target=scan_for_phrases)
    scan_thread.start()

# Функция для завершения работы программы
def stop_program():
    global scanning
    scanning = False

    # Завершаем pygame
    pygame.quit()

    root.destroy()

# Создание графического интерфейса
root = tk.Tk()
root.title("Сканер фразы")

# Устанавливаем флаг "-topmost" для окна, чтобы оно было поверх всех окон
root.attributes('-topmost', True)

start_button = tk.Button(root, text="Начать сканирование", command=start_scan)
start_button.pack()

stop_button = tk.Button(root, text="Завершить программу", command=stop_program)
stop_button.pack()

status_label = tk.Label(root, text="Ожидание")
status_label.pack()

root.mainloop()
