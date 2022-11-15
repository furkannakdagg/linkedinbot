#############
# LIBRARIES
#############
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# PATH OLARAK DRIVER KENDİ BİLGİSAYARINIZDA HANGİ PATHSE ONU VERMELİSİNİZ!!!
driver_path = "chromedriver_DOSYA_YOLU"
driver = webdriver.Chrome(driver_path)

#####################
# LINKED'INE BAĞLAN
#####################
driver.get("https://www.linkedin.com/")

#######################
# LINKEDIN'E GİRİŞ YAP
#######################
driver.find_element(by=By.XPATH, value="/html/body/nav/div/a[2]").click()  # Oturum Aç
mail = driver.find_element(by=By.NAME, value="session_key").send_keys("KENDİ MAİLİN")  # Maili gir
pw = driver.find_element(by=By.NAME, value="session_password").send_keys("KENDİ ŞİFREN")  # Şifreyi gir
driver.find_element(by=By.XPATH,
                    value="/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()  # Onaylama butonuna bas

# Arama yapmak istediğimiz sayfayı buraya ekleyebiliriz!
driver.get(
    'https://www.linkedin.com/search/results/people/?industry=%5B%2296%22%2C%224%22%2C%2243%22%5D&keywords=data&network=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=2&profileLanguage=%5B%22en%22%2C%22tr%22%5D&serviceCategory=%5B%22602%22%2C%2263%22%5D&sid=SN9'
)  # Gitmek istediğimiz sayfa

##################################################
# TAKİP ET VE BAĞLANTI KUR "BUTONLARINI" YAKALAMA
##################################################
submit_button = driver.find_elements(by=By.CSS_SELECTOR, value='button')  # CSS_SELECTOR ile yakalama
# submit_button = driver.find_elements(by=By.XPATH, value='//span[@class="artdeco-button__text"]')  # XPATH ile yakalama

"""
Yukarıdaki işlem sayfadaki tüm butonları getirecektir(arama butonu, üstteki iş ilanları, ağım vs. butonları). 
Bize sadece bunların içerisinde "Bağlantı kur" ve "Takip Et" yazan butonlar gerekli. 
Bulunan butonlar içerisindeki text'lere bakıp filtreleme yaparız. 
"""
for i in submit_button:
    if i.text == "Bağlantı kur" or i.text == "Takip Et":
        i.click()  # bunlardan biriyse tıkla

        # Arada karşımıza çıkan "Davetiyeye not ekleyerek kişiselleştirebilirsiniz" penceresindeki "Gönder" butonuna tıklamak için
        try:
            gonder = driver.find_elements(by=By.CSS_SELECTOR, value='button')
            for g in gonder:
                if g.text == "Gönder":
                    g.click()
        except:  # Eğer pencere açılmazsa koda devam et
            continue