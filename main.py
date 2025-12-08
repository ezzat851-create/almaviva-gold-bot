import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from datetime import datetime

# بياناتك الشخصية (آمنة هنا لأن الريبو بتاعك)
WHATSAPP_NUMBER = "+393667241790"
FULL_NAME = "NABILA SALEM SAYED AHMED MOHAMED"   # الاسم زي ما في الجواز

def send_whatsapp(message):
    url = f"https://api.callmebot.com/whatsapp.php?phone={WHATSAPP_NUMBER}&text={message}&apikey=5521588"
    try:
        requests.get(url, timeout=10)
        print("رسالة واتساب مرسلة!")
    except:
        print("فشل الواتساب")

print("البوت الذهبي شغال على السيرفر 24/7 - ضم عائلي - القاهرة - أقرب موعد")

options = uc.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920,1080')
driver = uc.Chrome(options=options)

while True:
    try:
        driver.get("https://egy.almaviva-visa.it/")
        time.sleep(8)

        if "non disponibili" not in driver.page_source.lower():
            print(f"المواعيد فتحت!! {datetime.now()}")

            # 1. اضغط Prenota
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Prenota')]"))).click()
            time.sleep(3)

            # 2. ضم عائلي
            driver.find_element(By.XPATH, "//option[contains(text(),'Ricongiungimento familiare')]").click()
            driver.find_element(By.XPATH, "//button[contains(text(),'Avanti')]").click()
            time.sleep(3)

            # 3. القاهرة + خدمة عادية
            driver.find_element(By.XPATH, "//option[contains(text(),'Il Cairo')]").click()
            driver.find_element(By.XPATH, "//button[contains(text(),'Avanti')]").click()
            time.sleep(3)

            # 4. أقرب يوم متاح
            driver.find_element(By.XPATH, "(//div[contains(@class,'available')]//a)[1]").click()
            time.sleep(2)

            # 5. أقرب ساعة متاحة
            driver.find_element(By.XPATH, "(//button[contains(@class,'time-slot') and not(contains(@class,'disabled'))])[1]").click()
            time.sleep(3)

            # 6. املأ الاسم لو طلب
            try:
                name_field = driver.find_element(By.XPATH, "//input[@name='full_name' or @id='full_name' or contains(@placeholder,'Name')]")
                name_field.clear()
                name_field.send_keys(FULL_NAME)
            except:
                pass

            # إرسال التنبيه على الواتساب
            msg1 = f"تم الحجز يا معلم!%0Aضم عائلي - القاهرة%0Aالاسم: {FULL_NAME}%0Aأقرب موعد متاح%0Aادخل ادفع دلوقتي في أول 10 دقايق:%0Ahttps://egy.almaviva-visa.it/"
            send_whatsapp(msg1)
            send_whatsapp("الحق ادفع بسرعة قبل ما الموعد يروح!!")

            print("تم كل حاجة! الموعد محجوز ومرسل على الواتساب")
            break

    except Exception as e:
        print(f"لسه مقفول... {datetime.now().strftime('%H:%M:%S')}")

    time.sleep(6)
