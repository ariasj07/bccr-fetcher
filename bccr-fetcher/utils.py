URLS = {
    "TIPO_DE_CAMBIO": "https://sdd.bccr.fi.cr/es/IndicadoresEconomicos/Inicio/Contenedor/6?Cuadro=1",
    "EMPLEO": "https://sdd.bccr.fi.cr/es/IndicadoresEconomicos/Inicio/Contenedor/539?Cuadro=172",
    "TPM": "https://sdd.bccr.fi.cr/es/IndicadoresEconomicos/Inicio/Contenedor/358?Cuadro=223"
}

# XPATHS:

XPATH_PREDOWNLOAD = (
    '/html/body/div[8]/main/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div[3]/div/div[1]/div/button[1]'
)

# Boton para descargar los datos seleccionados
XPATH_DOWNLOAD = (
    '/html/body/div[8]/main/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[7]/div/div/div/div[3]/div/button[2]'
)

XPATH_FULL_INDICATORS_SELECT = (
    '/html/body/div[8]/main/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/thead/tr/th[2]/input'
)



# TIPO DE CAMBIO (TC_...)
# Checkbox para seleccionar datos de tipo de cambio
