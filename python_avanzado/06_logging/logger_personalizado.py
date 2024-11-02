import logging

# logger = logging.getLogger("logger personalizado")
logger = logging.getLogger(__name__) # con __name__ conseguimos que se muestre el metodo donde se produce
print(logger)

logger.warning("log de advertencia")