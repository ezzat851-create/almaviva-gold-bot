import requests
import time
from datetime import datetime
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ====================================================
# بياناتك الشخصية
# ====================================================
WHATSAPP_NUMBER = "+393667241790"
FULL_NAME = "NABILA SALEM SAYED AHMED MOHAMED"

# ====================================================
# دالة إرسال واتساب
# ====================================================
def send_whatsapp(msg):
    url = f"https://api.callmebot.com/whatsapp.php?phone={WHATSAPP_NUMBER}&text={msg}&apikey=5521588"
    try:
        requests.get(url, timeout=10)
        print("✔ رسالة واتساب اتبعت")
    except:
        print("✖ فشل إرسال الواتساب")

# ====================================================
print("البوت الذهبي شغال على السحابة 24/7 - ضم عائلي - القاهرة")

# ====================================================
# إعداد المتصفح
# ====================================================
options = uc.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920,1080')
driver = uc.Chrome(options=options)

# ====================================================
# بدء التكرار لفحص المواعيد
# ====================================================
while True:
    try:
        driver.get("https://egy.almaviva-visa.it/")
        time.sleep(8)

        if "non disponibili" not in driver.page_source.lower():
            print(f"المواعيد فتحت!! {datetime.now()}")

            # 1. اضغط Prenota
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Prenota')]"))
            ).click()
            time.sleep(3)

            # 2. ضم عائلي
            driver.find_element(By.XPATH, "//option[contains(text(),'Ricongiungimento familiare')]").click()
            driver.find_element(By.XPATH, "//button[contains(text(),'Avanti')]").click()
            time.sleep(3)

            # 3. القاهرة + خدمة عادية
            driver.find_element(By.XPATH, "//option[contains(text(),'Il Cairo')]").click()
            driver.find_element(By.XPATH, "//button[contains(text(),'Avanti')]").click()
            time.sleep(3)

            # 4. أقرب يوم
            driver.find_element(By.XPATH, "(//div[contains(@class,'available')]//a)[1]").click()
            time.sleep(2)

            # 5. أقرب ساعة
            driver.find_element(By.XPATH, "(//button[contains(@class,'time-slot') and not(contains(@class,'disabled'))])[1]").click()
            time.sleep(3)

            # 6. ملء الاسم لو مطلوب
            try:
                name_field = driver.find_element(
                    By.XPATH,
                    "//input[@name='full_name' or @id='full_name' or contains(@placeholder,'Name')]"
                )
                name_field.clear()
                name_field.send_keys(FULL_NAME)
            except:
                pass

            # إرسال التنبيه
            msg1 = (
                f"🔥 تم حجز الموعد!%0A"
                f"ضم عائلي - القاهرة%0A"
                f"الاسم: {FULL_NAME}%0A"
                f"ادخل ادفع فوراً قبل ما يطير:%0A"
                f"https://egy.almaviva-visa.it/"
            )

            send_whatsapp(msg1)
            send_whatsapp("‼️ اسرع وادفع قبل ما الموعد يضيع!")

            print("✔ الموعد اتاخد واترسل على الواتساب")
            break

        # ====================================================
        # فحص سريع بدون Selenium (أسرع)
        # ====================================================
        r = requests.get("https://egy.almaviva-visa.it/", timeout=15)
        page = r.text.lower()

        if "non disponibili" not in page and "لا تتوفر مواعيد" not in page:
            print(f"المواعيد فتحت يا معلم!! {datetime.now()}")

            msg = (
                f"🚨 تم فتح المواعيد الآن!%0A"
                f"الاسم: {FULL_NAME}%0A"
                f"ضم عائلي - القاهرة%0A"
                f"ادخل فوراً واحجز قبل ما يقفل:%0A"
                f"https://egy.almaviva-visa.it/"
            )

            for _ in range(5):
                send_whatsapp(msg)
                time.sleep(2)

            print("✔ تم إرسال 5 رسائل واتساب")
            break

        else:
            print(f"لسه مقفول... {datetime.now().strftime('%H:%M:%S')}")

    except Exception as e:
        print(f"خطأ أثناء الفحص: {e}")

    time.sleep(7)
