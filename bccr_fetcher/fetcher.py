from playwright.sync_api import sync_playwright
import pandas as pd
from .utils import XPATH_DOWNLOAD, XPATH_PREDOWNLOAD, URLS, XPATH_FULL_INDICATORS_SELECT

def download_data(indicator: str, start, end, rows_to_skip=0):
    print("BCCR_FETCHER ATENCIÓN: Los Excels brindados por el BCCR inician con un número x de filas con información no númerica, se recomienda usar el parámetro 'rows_to_skip' en la instancia de clase BCCR e indicar rows_to_skip=4, así el dataframe ignorará las primeras 4 filas")
    print("BCCR_FETCHER: La información se está empezando a descargar...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()
        page.goto(URLS[f"{indicator}"])

        print("BCCR_FETCHER: Información encontrada.")
        page.wait_for_selector(f'xpath={XPATH_FULL_INDICATORS_SELECT}')
        page.locator(f'xpath={XPATH_FULL_INDICATORS_SELECT}').check()

        page.wait_for_selector(f'xpath={XPATH_PREDOWNLOAD}')
        page.locator(f'xpath={XPATH_PREDOWNLOAD}').click()

        page.wait_for_selector(f'xpath={XPATH_DOWNLOAD}')
        
        with page.expect_download() as d:
            page.locator(f'xpath={XPATH_DOWNLOAD}').click()

        download = d.value
        print("BCCR_FETCHER: Información descargándose...")
        excel_path = download.path()
        df = pd.read_excel(excel_path, skiprows=rows_to_skip)

        options = {
            (True, True): lambda df: df[(df["Fecha"] >= start) & (df["Fecha"] <= end)].reset_index(drop=True),
            (True, False): lambda df: df[df["Fecha"] >= start].reset_index(drop=True),
            (False, True): lambda df: df[df["Fecha"] <= end].reset_index(drop=True),
            (False, False): lambda df: df
        }
        
        df = options[bool(start.strip()), bool(end.strip())](df)


        browser.close()
        print("BCCR_FETCHER: Consejo, si la librería devuelve Empty dataframe y uso un filtro de fechas 'start', puede que haya querido filtrar fechas muy prontas y todavía no hay datos disponibles ofrecidos en el sitio web del BCCR")
        return df