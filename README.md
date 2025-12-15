# Descarga datos económicos de Costa Rica 📊
### Librería Open Source que facilita la descarga y manejo de datos económicos públicados en la página del Banco Central De Costa Rica

🚨 Este es un proyecto personal para facilitar tareas de manejo de datos, no está afiliada al BCCR por lo que es sensible a cambios y mejoras que realicen en el sitio web. Cualquier sugerencia o pull request será muy bienvenida y ayudará a mejorar la herramienta.

---

# ¿Qué hace?
Entrar al sitio web del BCCR, descargar el Excel de los datos, subirlos a Python y manejarlos puede ser un proceso un poco repetitivo, en lo personal tener esta herramienta me pemite con 3 lineas de código tener indicadores económicos del BCCR en un dataframe de pandas en segundos

# ¿Cómo la uso?
Es muy sencillo, simplemente se debe escribir las siguientes lineas de código en un entorno .py o .ipynb

```python
conn = BCCR(indicator='TPM', start='', end='')
df = conn.download()
print(df)
```

`conn` es el conector con el sitio del BCCR  y la instancia de la clase, pide ciertos párametros:
- `indicator`: Hay varios. Tales como: `EMPLEO`, `TIPO_DE_CAMBIO`, `TPM`. De momento me encuentro trabajando en añadir más y esperando poder tener soporte para todos los indicadores económicos disponibles en el sitio web
- `start` (Opcional) este permite ponerle un mínimo de fecha a los datos para obtener el dataframe filtado por fechas, *importante*: Las fechas deben estar en formáto: YYYY-MM-DD, en caso no indicar una, se descargarán los datos con la fecha que se selecciona por defecto, la cual tiende a ser la mas vieja registrada
- `start` (Opcional) este permite ponerle un máximo de fecha a los datos para obtener el dataframe filtado por fechas, *importante*: Las fechas deben estar en formáto: YYYY-MM-DD, en caso no indicar una, se descargarán los datos con la fecha que se selecciona por defecto, la cual tiende a ser la mas reciente registrada

`df` es la variable que contiene lo que el método `download()` devuelve, que es un dataframe con los datos listo para usarse

Actualmente continúo trabajando en la librería, pronto la subiré a pip para poder ser descargada de la manera mas breve y sencilla posible desde cualquier entorno de Python. Esta librería necesita Python >= 3.10 y las siguientes librerías:
`pandas`  
`playwright`    

Se pueden instalar ejecutando el siguiente cómando en su consola:
`pip install pandas playwright`
o si usa un notebook como el de Google Colab:
`!pip install pandas playwright`

Véase un ejemplo de su uso:

```python
conn = BCCR(indicator='TPM', start='', end='')
df = conn.download()
print(df)
```

Salida:  
<img width="447" height="348" alt="image" src="https://github.com/user-attachments/assets/4dc48211-8d59-4712-abf0-7b2dedb52477" />

Como mencioné, esta librería no está afiliada al BCCR, es un proyecto personal y de código abierto, si encuentra un fallo por favor contácteme para solucionarlo lo más breve posible:  
Email: josuearias.crc@gmail.com  
Linkedin: https://www.linkedin.com/in/josu%C3%A9-arias-gauna-835bb1342/

