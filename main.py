from scraper import get_html, parse_tools, save_to_csv  # Importa funciones del módulo scraper

URL = "https://www.synthesia.io/post/ai-tools"  # Define la URL de la página a scrapear

def main():  # Función principal que controla el flujo del scraper
    html = get_html(URL)  # Obtiene el contenido HTML de la página
    tools = parse_tools(html)  # Extrae las herramientas de IA del HTML
    if tools:  # Verifica si se encontraron herramientas
        save_to_csv(tools)  # Guarda las herramientas en un archivo CSV
    else:
        print("No se encontró ninguna herramienta.")  # Mensaje si no se encontró nada

if __name__ == "__main__":  # Ejecuta main() solo si el archivo se ejecuta directamente
    main()
