#Thank you GPT
import datetime
import time

while True:
    current_time = datetime.datetime.now()
    clocktext = current_time.strftime("%H:%M:%S")
    print(clocktext, end="\r", flush=True)
    time.sleep(1)