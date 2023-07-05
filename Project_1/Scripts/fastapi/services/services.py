from Project_1.Scripts.fastapi.handlers.handlers import handling
import logging
class item:
    def create_an_item(entry):
        try:
            resp = handling.new_param(entry)
            return (entry)
        except Exception as e:
            logging.exception(e)
