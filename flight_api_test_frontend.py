from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search_same_from_to(driver):
    try:
        # İlk input'u bul
        from_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "headlessui-combobox-input-:Rq9lla:")))

        # İkinci input'u bul
        to_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "headlessui-combobox-input-:Rqhlla:")))

        # İki input'taki değerleri kontrol et
        from_value = from_input.get_attribute("value").strip()
        to_value = to_input.get_attribute("value").strip()

        if from_value and to_value:
            if from_value == to_value:
                error_message = 'Aynı şehir seçilemez!'
                error_div = driver.find_element(By.CLASS_NAME, "mt-24")
                driver.execute_script("arguments[0].innerHTML = arguments[1];", error_div, error_message)
            elif from_value != to_value:
                # Uçuşları listele ve gelen değerleri ekrana yazdır
                flights_list = get_flights_list(from_value, to_value)
                if not flights_list:
                    error_message = 'Bu iki şehir arasında uçuş bulunmuyor. Başka iki şehir seçmeyi deneyebilirsiniz.'
                    error_div = driver.find_element(By.CLASS_NAME, "mt-24")
                    driver.execute_script("arguments[0].innerHTML = arguments[1];", error_div, error_message)
                else:
                    print(f'Uçuşlar: {flights_list}')

                    found_items_element = driver.find_element(By.CLASS_NAME, "mb-10")
                    found_items_text = found_items_element.text
                    found_items_count = int(found_items_text.split()[1])  # Extracting the number from the text

                    flights_list = driver.find_elements(By.XPATH, "//ul[@class='grid grid-cols-1 gap-x-6 gap-y-8 lg:grid-cols-3 xl:gap-x-8']/li")
                    actual_number_of_flights = len(flights_list)

                    if found_items_count == actual_number_of_flights:
                        print(f'Found {actual_number_of_flights} items: Test Passed')
                        found_items_element = driver.find_element(By.CLASS_NAME, "mb-10")
                        found_items_text = f'Found {actual_number_of_flights} items: Test Passed'
                        driver.execute_script("arguments[0].innerHTML = arguments[1];", found_items_element, found_items_text)

                    else:
                        print(f'Found {found_items_count} items, expected {actual_number_of_flights}: Test Failed')
                        found_items_element = driver.find_element(By.CLASS_NAME, "mb-10")
                        found_items_text = f'Found {found_items_count} items, expected {actual_number_of_flights}: Test Failed'
                        driver.execute_script("arguments[0].innerHTML = arguments[1];", found_items_element, found_items_text)

                        
        else:
            print("Uyarı: Her iki input da başlangıçta boş veya yalnızca bir tanesi dolu!")

    except Exception as e:
        print(f'Hata: {str(e)}')

def get_flights_list(from_city, to_city):
    # Bu fonksiyon gelen şehirler arasındaki uçuşları listeleyerek döner (örneğin bir API çağrısı yapabilirsiniz)
    # Bu fonksiyonu ihtiyacınıza göre özelleştirebilirsiniz
    # Burada basit bir örnek olarak iki şehir arasındaki uçuşları içeren bir liste dönüyorum
    flights_list = [
        f'Uçuş 1: {from_city} to {to_city}',
        f'Uçuş 2: {from_city} to {to_city}',
        f'Uçuş 3: {from_city} to {to_city}'
    ]
    return flights_list

def main():
    try:
        # ChromeOptions oluştur
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = r'C:\Users\Ensar\Desktop\case_study\chrome-win64\chrome.exe'

        # ChromeDriver'ı başlat
        driver = webdriver.Chrome(options=chrome_options)

        # Uygulamanın ana sayfasına git
        driver.get("https://flights-app.pages.dev/")

        while True:
            # Input'lar seçildikçe fonksiyonu çağır
            test_search_same_from_to(driver)

    finally:
        # Tarayıcıyı kapat
        driver.quit()

# Ana fonksiyonu çağır
if __name__ == "__main__":
    main()
