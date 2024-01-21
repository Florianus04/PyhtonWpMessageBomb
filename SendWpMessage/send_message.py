#bu bir whatsapp mesaj botudur
#oncelikle terminale "pip install pyautogui" komutunu yazıp paketi yukluyoruz
#kodu calistirdiktan sonra hemen whatsapp webe gelip yollayacagimiz kisi ile olan sohbet bolumunu acin

import pyautogui
import time

time.sleep(3)#whatsapp web acmamız icin gereken sure

for i in range(100):#mesaji kac kere yollayacagiz
    mesaj = f"{i} yollanacak mesaj"#yollanacak mesaj
    pyautogui.typewrite(mesaj)#yazdir
    pyautogui.press("enter")#yolla


