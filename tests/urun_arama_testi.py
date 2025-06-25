from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_urun_arama():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    
    # Arama kutusunu bul
    search_input = driver.find_element(By.ID, "search_product")
    
    # Arama kutusuna "T-shirt" yaz
    search_input.send_keys("T-shirt")
    
    # Arama butonuna tıkla
    search_btn = driver.find_element(By.ID, "submit_search")
    search_btn.click()

    # Sonuçların yüklenmesi için 2 saniye bekle
    time.sleep(2)
    
    # Sonuçlar var mı diye kontrol et (ürün bilgilerini gösteren class)
    results = driver.find_elements(By.CLASS_NAME, "productinfo")
    
    # En az bir sonuç gelmeli
    assert len(results) > 0
    
    driver.quit()
