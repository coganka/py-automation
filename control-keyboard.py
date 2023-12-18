import pyautogui
import time

pyautogui.doubleClick(114, 438)
time.sleep(1)
pyautogui.move(200,0)
pyautogui.click()

pyautogui.press('down')
pyautogui.press('enter')

pyautogui.write('automated text\n')

pyautogui.hotkey('command', 'a')
pyautogui.hotkey('command', 'c')
pyautogui.press('down')
pyautogui.hotkey('command', 'v')