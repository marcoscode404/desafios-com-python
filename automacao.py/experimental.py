# uv add pyautogui
# xhost +SI:localuser:$(whoami) -- terminal
# sudo apt-get install python3-tk python3-dev

import pyautogui as pa
import time
pa.PAUSE = 1

pa.press('win')
pa.write("chrome")
pa.press('ENTER')
pa.write("youtube.com")
pa.press('ENTER')