from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import time

def get_html(url, wait_time=5):
    """Abre la página con Selenium y devuelve el HTML después de cargar JS."""
    options = Options()
    options.add_argument("--headless")  # Ejecuta sin abrir ventana
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(wait_time)  # Espera a que cargue JS
    html = driver.page_source
    driver.quit()
    return html

def parse_tools(html):
    """Extrae los nombres de las herramientas desde el HTML."""
    soup = BeautifulSoup(html, "html.parser")
    container = soup.find("div", id="the-best-ai-tools-by-category")
    if not container:
        print("No se encontró el contenedor.")
        return []

    ul = container.find("ul")
    if not ul:
        print("No se encontró la lista <ul> dentro del contenedor.")
        return []

    items = ul.find_all("li")
    tools = [item.text.strip() for item in items]
    return tools

def save_to_csv(data, filename="output.csv"):
    """Guarda la lista de herramientas en un CSV."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Tool Name"])
        for tool in data:
            writer.writerow([tool])
    print(f"{len(data)} herramientas guardadas en {filename}")
