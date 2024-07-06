from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

logging.info("welcome")

try:
    a=2/0
except Exception as e:
    logging.info("error occured")
    raise USvisaException(e,sys)
