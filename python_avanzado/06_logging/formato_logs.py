import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
) # w sobreescribe los logs

nombre = "Salva"
logging.error(f"{nombre} creó el error")
logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error critico")

try:
    division = 2 / 0
except:
    # logging.error("División por cero")
    logging.exception("División por cero")