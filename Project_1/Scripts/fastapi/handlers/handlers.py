import logging
from Project_1.Scripts.fastapi.DB.createdb import postgres
from Project_1.Scripts.fastapi.DB.db import SessionLocal
import json
from datetime import datetime
db=SessionLocal()
class handling:
    def new_param(random_numbers):
        try:
            data_list = json.loads(random_numbers)
            dictionary = {}
            # for item in data_list:
            #     key = item["Parameters"]
            #     value = item["random_numbers"]
            #     dictionary[key] =[] value
            [dictionary.update({each_parameter["Parameters"]:each_parameter["random_numbers"]})
              for each_parameter in data_list]
          
            new_item=postgres(
                date_time = datetime.now(),
                kw=dictionary["kw"],
                kwh=dictionary["kwh"],
                current=dictionary["current"],
                voltage=dictionary["voltage"],
            )
            

            db.add(new_item)
            db.commit()
            return new_item
        except Exception as e:
            logging.exception(e)