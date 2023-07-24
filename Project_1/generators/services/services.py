from Project_1.generators.handlers.handlers import handling
import logging
from fastapi import APIRouter
user = APIRouter()
class item:
    def create_an_item(entry):
        """A function to create a new item """
        try:
            resp = handling.new_param(entry)
            return (entry)
        except Exception as e:
            logging.exception(e)

    def create_an_entry(entry):
        """A function to create a new entry """
        try:
            resp = handling.new_entry(entry)
            return (entry)
        except Exception as e:
            logging.exception(e)

@user.get('/jsonfile')
def download_file():
    """A function to download the data from database in json format """
    try:
        resp  = handling.get_file()
        return resp
    except Exception as e:
        logging.exception(e)
