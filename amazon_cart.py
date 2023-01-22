import pyautogui
import time
import webbrowser

cart_position = 1662, 619
url = 'https://www.amazon.de/-/en/Weeknd/dp/B084XTMZVS/ref=sr_1_2?crid=3G0H4SQA4VZTI&keywords=after+hours+vinyl&qid=1674408728&sprefix=after+h%2Caps%2C361&sr=8-2'
webbrowser.open(url)
time.sleep(5)
pyautogui.click(cart_position)
