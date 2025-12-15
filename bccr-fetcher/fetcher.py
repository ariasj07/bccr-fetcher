from playwright.sync_api import sync_playwright
import pandas as pd
from utils import XPATH_DOWNLOAD, XPATH_PREDOWNLOAD, URLS, XPATH_FULL_INDICATORS_SELECT

def download_data(indicator: str, start, end):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()
        page.goto(URLS[f"{indicator}"])


        page.wait_for_selector(f'xpath={XPATH_FULL_INDICATORS_SELECT}')
        page.locator(f'xpath={XPATH_FULL_INDICATORS_SELECT}').check()

        page.wait_for_selector(f'xpath={XPATH_PREDOWNLOAD}')
        page.locator(f'xpath={XPATH_PREDOWNLOAD}').click()

        page.wait_for_selector(f'xpath={XPATH_DOWNLOAD}')
        
        with page.expect_download() as d:
            page.locator(f'xpath={XPATH_DOWNLOAD}').click()

        download = d.value

        excel_path = download.path()
        df = pd.read_excel(excel_path, skiprows=4)
        if start.strip() != '' and end.strip() != '':
            df = df[(df["Fecha"] >= start) & (df["Fecha"] <= end)].reset_index(drop=True)

        browser.close()
        return df