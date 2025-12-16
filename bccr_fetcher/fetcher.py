import pandas as pd
import asyncio

from .utils import XPATH_DOWNLOAD, XPATH_PREDOWNLOAD, URLS, XPATH_FULL_INDICATORS_SELECT

def download_data(indicator: str, start="", end="", rows_to_skip=0, is_colab=False):
    """    
    Parámetros:
    - indicator: nombre del indicador a descargar.
    - start: fecha de inicio (opcional).
    - end: fecha de fin (opcional).
    - rows_to_skip: filas iniciales a ignorar en el Excel.
    - is_colab: si True, usa API asíncrona para entornos como Google Colab.
    """
    print("BCCR_FETCHER ATENCIÓN: Los Excels brindados por el BCCR inician con un número x de filas con información no númerica, se recomienda usar el parámetro 'rows_to_skip'.")
    print("BCCR_FETCHER: La información se está empezando a descargar...")

    if is_colab:
        # Versión asíncrona para Colab
        from playwright.async_api import async_playwright

        async def async_download():
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                context = await browser.new_context(accept_downloads=True)
                page = await context.new_page()
                await page.goto(URLS[f"{indicator}"])

                print("BCCR_FETCHER: Información encontrada.")
                await page.wait_for_selector(f'xpath={XPATH_FULL_INDICATORS_SELECT}')
                await page.locator(f'xpath={XPATH_FULL_INDICATORS_SELECT}').check()

                await page.wait_for_selector(f'xpath={XPATH_PREDOWNLOAD}')
                await page.locator(f'xpath={XPATH_PREDOWNLOAD}').click()

                await page.wait_for_selector(f'xpath={XPATH_DOWNLOAD}')

                async with page.expect_download() as d:
                    await page.locator(f'xpath={XPATH_DOWNLOAD}').click()
                download = await d.value
                excel_path = await download.path()

                df = pd.read_excel(excel_path, skiprows=rows_to_skip)

                await browser.close()
                return df

        df = asyncio.run(async_download())

    else:
        # Versión síncrona
        from playwright.sync_api import sync_playwright

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
            excel_path = download.path()

            df = pd.read_excel(excel_path, skiprows=rows_to_skip)
            browser.close()

    # Filtrado por fechas
    options = {
        (True, True): lambda df: df[(df["Fecha"] >= start) & (df["Fecha"] <= end)].reset_index(drop=True),
        (True, False): lambda df: df[df["Fecha"] >= start].reset_index(drop=True),
        (False, True): lambda df: df[df["Fecha"] <= end].reset_index(drop=True),
        (False, False): lambda df: df
    }
    df = options[bool(start.strip()), bool(end.strip())](df)

    print("BCCR_FETCHER: Consejo, si la librería devuelve Empty dataframe y uso un filtro de fechas 'start', puede que haya querido filtrar fechas muy prontas y todavía no hay datos disponibles ofrecidos en el sitio web del BCCR")
    return df
