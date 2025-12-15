"""
Autor: Josué Arias Gauna
Email: josuearias.crc@gmail.com
Última actualización: 15 de diciembre de 2025
---

# Descripción de la Librería

Esta librería sirve como una herramienta práctica para interactuar con los datos disponibles en el sitio del Banco Central de Costa Rica.

⚠️ **Importante:** Esta librería es de desarrollo propio, de código abierto (*open source*), y **no está afiliada ni respaldada por el Banco Central de Costa Rica**.
Su propósito es facilitar la descarga y manejo de información de manera sencilla y automatizada.

Si encuentra algún problema o falla, por favor contacteme
"""
from typing import Literal
from playwright.sync_api import sync_playwright
import pandas as pd
from fetcher import download_data

URL = "https://sdd.bccr.fi.cr/es/IndicadoresEconomicos/Inicio/Contenedor/6?Cuadro=1"

class BCCR:
    def __init__(self, indicator: str, start: str, end: str):
        self.indicator = indicator
        self.start = start
        self.end = end

    def download(self):
        return download_data(indicator=self.indicator, start=self.start, end=self.end)



conn = BCCR(indicator='TPM', start='', end='')
df = conn.download()
print(df)
