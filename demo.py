from Visa_eligibility.logger  import logging
from Visa_eligibility.exception import USvisaException
import sys


logging.info("WElcome to our custom log") 

try :
    a= 2/0
except Exception as e:
    raise USvisaException(e,sys)  