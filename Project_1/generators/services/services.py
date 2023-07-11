from Project_1.generators.handlers.handlers import handling
import logging
from fastapi import APIRouter
user = APIRouter()
class item:
    def create_an_item(entry):
        try:
            resp = handling.new_param(entry)
            return (entry)
        except Exception as e:
            logging.exception(e)

    def create_an_entry(entry):
        try:
            resp = handling.new_entry(entry)
            return (entry)
        except Exception as e:
            logging.exception(e)

@user.get('/jsonfile')
def download_file():
    try:
        resp  = handling.get_file()
        return resp
    except Exception as e:
        logging.exception(e)
