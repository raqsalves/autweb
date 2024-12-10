from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# Iniciando o web driver
driver = webdriver.Chrome()  # utilizei o chrome pq é oq mais uso

try:
    # acessar o link solicitado
    driver.get("https://g1.globo.com/")

    # espera alguns segundos pra barra de buscar ficar visivel
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Inteligência Artificial")
    search_box.send_keys(Keys.RETURN)

    time.sleep(10)  # aguarda 10 segundos pra carregar os resultados da busca

    # extrai os titulos das noticias 
    news_items = driver.find_elements(By.CSS_SELECTOR, "div.feed-post")
    news_data = []

    for item in news_items:
        try:
            title = item.find_element(By.CSS_SELECTOR, "h2.feed-post-link").text
            date = item.find_element(By.CSS_SELECTOR, "span.feed-post-datetime").text
            news_data.append(f"{date} - {title}")  # exibe a data e o titulo da noticia
        except Exception as e:  # tratando exceção
            continue  # Caso algum item não seja encontrado 

    # salvando oq encontrou num arquivo txt
    with open("noticias_ia_g1.txt", "w", encoding="utf-8") as file:   
        file.write("\n".join(news_data))
        print("Os dados foram salvos em 'noticias_ia_g1.txt' com sucesso!") 

finally:
    driver.quit()