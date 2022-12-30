import logging
import os
from datetime import datetime

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] %(message)s')


def config():
    print('LOGGING START TIME: ' + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
    print('LOG DIRECTORY: ' + str(os.path.dirname(__file__)))


def debug(message):
    logging.debug(message)


def info(message):
    logging.info(message)


def warning(message):
    logging.warning(message)


def exception(message):
    logging.exception(message)


def critical(message):
    logging.critical(message)
