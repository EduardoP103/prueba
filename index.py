from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura el driver para Chrome
driver = webdriver.Chrome()

# Abre la página web del anime
driver.get('https://animenix.com/ver/spyxfamily-1x1/')

try:
    # Cambia al contexto del iframe si existe
    try:
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
        )
        driver.switch_to.frame(iframe)
    except:
        pass

    # Espera explícita hasta que el botón de reproducción esté presente y sea clicable
    play_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".jw-svg-icon-play"))
    )

    # Simula presionar la tecla de espacio en el botón de reproducción
    play_button.send_keys(Keys.SPACE)
    print("Se simuló presionar la tecla de espacio en el botón de reproducción.")

except Exception as e:
    print("No se pudo simular presionar la tecla de espacio en el botón de reproducción o ocurrió un error.")
    print(e)

finally:
    # Cierra el navegador
    driver.quit()
