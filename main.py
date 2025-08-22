from scraper import get_html, parse_tools, save_to_csv

URL = "https://www.synthesia.io/post/ai-tools"

def main():
    html = get_html(URL)
    tools = parse_tools(html)
    if tools:
        save_to_csv(tools)
    else:
        print("No se encontró ninguna herramienta.")

if __name__ == "__main__":
    main()
