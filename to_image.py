import os
import sys
from playwright.sync_api import sync_playwright

if len(sys.argv) < 2:
    print("Bitte gib den Namen der HTML-Datei als Parameter an.")
    print("Beispiel: python to_image.py ananaskekse.html (optional Breite: 900)")
    sys.exit(1)

if sys.argv[1].lower().endswith(".html"):
	html_file = sys.argv[1]
else:
	html_file = sys.argv[1] + ".html" 

if not os.path.exists(html_file):
    print(f"Fehler: Datei '{html_file}' wurde nicht gefunden.")
    sys.exit(1)

output_file = html_file[:-5] + ".png"

viewport_width = int(sys.argv[2]) if len(sys.argv) > 2 else 1052

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": viewport_width, "height": 800})
    page.goto(f"file://{os.path.abspath(html_file)}")
    page.wait_for_timeout(1000)
    page.screenshot(path=output_file, full_page=True)
    browser.close()

print(f"Screenshot gespeichert als: {output_file}")