import requests
import time
from datetime import datetime

# بياناتك كاملة
WHATSAPP_NUMBER = "+393667241790"  # رقم الواتساب الإيطالي
FULL_NAME = "NABILA SALEM SAYED AHMED MOHAMED"  # الاسم زي ما في الجواز

def send_whatsapp(msg):
    url = f"https://api.callmebot.com/whatsapp.php?phone={WHATSAPP_NUMBER}&text={msg}&apikey=5521588"
    try:
        requests.get(url, timeout=10)
    except:
        pass

print("البوت الذهبي شغال على السحابة 24/7 - ضم عائلي - القاهرة")

while True:
    try:
        r = requests.get("https://egy.almaviva-visa.it/", timeout=15)
        page = r.text.lower()
        
        if "non disponibili" not in page and "لا تتوفر مواعيد" not in page:
            print(f"المواعيد فتحت يا معلم!! {datetime.now()}")
            
            msg = f"🚨 تم فتح المواعيد دلوقتي يا معلم!%0A" \
                  f"الاسم: {FULL_NAME}%0A" \
                  f"ضم عائلي - القاهرة%0A" \
                  f"أقرب موعد متاح%0A" \
                  f"الحق افتح الموقع فورًا واخد الميعاد قبل ما يروح:%0A" \
                  f"https://egy.almaviva-visa.it/"
            
            # هيبعت 5 مرات عشان تتأكد إنها وصلت
            for _ in range(5):
                send_whatsapp(msg)
                time.sleep(2)
            
            print("تم الإرسال على الواتساب 5 مرات!")
            break
            
        else:
            print(f"لسه مقفول... {datetime.now().strftime('%H:%M:%S')}")
            
    except Exception as e:
        print(f"مشكلة اتصال: {e}")
    
    time.sleep(7)  # فحص كل 7 ثواني
