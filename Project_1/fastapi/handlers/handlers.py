import logging
from Project_1.fastapi.DB.createdb import postgres
from Project_1.fastapi.DB.db import SessionLocal
import json
from fastapi import APIRouter
from datetime import datetime
import pandas as pd
from fastapi.DB.db import engine
from fastapi.responses import FileResponse
db=SessionLocal()
user = APIRouter()

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
    
    
    def new_entry(random_parameters):
        try:
            data_list = json.loads(random_parameters)
            dictionary = {}
            [dictionary.update({each_parameter["Parameters"]:each_parameter["random_parameters"]})
              for each_parameter in data_list]
          
            new_parameter=postgres(
                date_time = datetime.now(),
                kw=dictionary["kw"],
                kwh=dictionary["kwh"],
                current=dictionary["current"],
                voltage=dictionary["voltage"],
            )
            

            db.add(new_parameter)
            db.commit()
            return new_parameter
        except Exception as e:
            logging.exception(e)
    
    
    # df.to_csv(r'C:\Users\Ron\Desktop\export_dataframe.csv', index=False, header=True)
    def generate_report():
        try:
            df = pd.read_sql('select * from \"numbers\"',engine )
            df.to_json('C:\\Users\\ishikapradeep.bhagat\\Desktop\\Project\\scripts\\fastapi\\handlers\\handlers.json', index=False, header=True)
        except Exception as e:
            logging.exception(e)

    def get_file():
         try:
            file_path = r"C:\\Users\\ishikapradeep.bhagat\\Desktop\\Project\\scripts\\fastapi\\handlers\\handlers.json"
            
            response = FileResponse(file_path, media_type="application/json")
            return response
         except Exception  as e:
           print(e)
