import bccr_fetcher
import pandas as pd

conn = bccr_fetcher.BCCR(
    indicator="EXPECTATIVAS_INFLACION",
    start="",
    end="",
    rows_to_skip=4
)

"""
# Ejemplo de uso: 
df = conn.download()
print(df)
"""