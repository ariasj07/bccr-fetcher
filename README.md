# Descarga datos económicos de Costa Rica
### Librería Open Source que facilita la descarga y manejo de datos económicos públicados en la página del Banco Central De Costa Rica

Este es un proyecto personal para facilitar tareas de manejo de datos, no está afiliada al BCCR por lo que es sensible a cambios y mejoras que realicen en el sitio web. Cualquier sugerencia o pull request será muy bienvenida y ayudará a mejorar la herramienta.

---

# ¿Qué hace?
Entrar al sitio web del BCCR, descargar el Excel de los datos, subirlos a Python y manejarlos puede ser un proceso un poco repetitivo, en lo personal tener esta herramienta me pemite con 3 lineas de código tener indicadores económicos del BCCR en un dataframe de pandas en segundos

# ¿Cómo la uso?

Es muy sencillo, simplemente se debe escribir las siguientes lineas de código en un entorno .py o .ipynb

`
conn = BCCR(indicator='TPM', start='', end='')
df = conn.download()
print(df)
`
