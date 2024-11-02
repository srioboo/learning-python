import logging

# por defecto usa append "a"
# logging.basicConfig(level=logging.DEBUG, filename="ejemplo_log.log")
logging.basicConfig(level=logging.DEBUG, filename="ejemplo_log.log", filemode="w") # w sobreescribe los logs

logging.debug("Log de debugging")
logging.info("Log informativo")
logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error critico")