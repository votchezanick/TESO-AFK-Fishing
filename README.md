# AFK Fishing TESO

Этот проект представляет собой скрипт для автоматизации процесса рыбалки в игре The Elder Scrolls Online (TESO). Проект разработан на Python 3.10 с использованием среды PyCharm 2023.2.1 (Community Edition). Программа осуществляет сканирование текста на экране, запускает и завершает процесс рыбалки, позволяя вам выполнять это длительное действие "в автоматическом режиме".

## Требования

Перед запуском программы убедитесь, что у вас установлены следующие пакеты Python:

- pyautogui
- pytesseract
- keyboard
- time
- tkinter
- threading
- pygame
- numpy

Также, удостоверьтесь, что у вас установлен Tesseract OCR и указанный путь к нему в программе верен.

```
# Указываем путь к исполняемому файлу Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
```

## Важные замечания перед использованием

1. Программа сканирует текст в определенной области экрана, предполагая, что экран имеет разрешение Full HD. Если ваш монитор отличается от этого, возможны проблемы с распознаванием текста.
2. Работоспособность программы настоятельно рекомендуется проверить на стандартном интерфейсе игры TESO без кастомных аддонов и изменений.
3. Программа рассчитана на работу с русской версией игры. Если вы используете английскую версию, удостоверьтесь, что у вас установлен соответствующий пакет языка для Tesseract и правильно указан параметр lang='eng'.
4. Проект предназначен для облегчения процесса рыбалки с целью заработка внутриигровой валюты. Он предоставляет возможность автоматизации, но не претендует на статус лучшей AFK рыбалки в TESO.
5. Завершение программы можно осуществить быстро нажатием F9 или соответствующей кнопкой в пользовательском интерфейсе.

## Инструкции по использованию

1. Запустите проект.
2. Откроется пользовательский интерфейс (UI). Нажмите "Начать сканирование".
3. Подходите к рыболовному месту в TESO, убедитесь, что камера удобно расположена, и дождитесь, когда программа обнаружит фразу "Ловить рыбу".
4. Программа автоматически управляет процессом рыбалки. Вы можете покинуть компьютер, и она уведомит вас о завершении сигналом или выключить звуковое уведомление в настройках.

## Завершение

Проект создан в любительских целях и предоставляется "как есть". Автор не несет ответственности за проблемы, возникшие в результате использования программы. Успешной рыбалки!