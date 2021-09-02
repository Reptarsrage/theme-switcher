import logging
import logging.handlers as handlers

logger = logging.getLogger('theme-switcher')
logger.setLevel(logging.INFO)

## Here we define our formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logHandler = handlers.RotatingFileHandler('./logs/app.log', maxBytes=100000, backupCount=10)
logHandler.setLevel(logging.INFO)

## Here we set our logHandler's formatter
logHandler.setFormatter(formatter)

logger.addHandler(logHandler)
logger.addHandler(logging.StreamHandler())

def info(str):
    logger.info(str)

def warn(str):
    logger.warn(str)

def error(str):
    logger.error(str)