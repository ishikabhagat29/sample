import time
import pandas as pd
import numpy as np
import logging
import json
from Project_1.Scripts.data_generator.publisher import Publisher

class Generation:
    def simulation_a():
        """A function to simulate the given parameters and generate random values between the limits after every 10 secs
            and convert the dataframe to json file and then to a string
            params:none
            return:returns the randomly generated numbers in json string format every 10 secs """
        try:
            while True:
                df = pd.read_csv('scripts/energy_parameters.csv')
                df['random_numbers'] = df.apply(lambda x: np.random.uniform(x.lower_limit, x.upper_limit), axis=1)
                df = df.iloc[:,[0,3]]
                df = df.to_json(orient = 'records')
                df = json.loads(df)
                (Publisher.publish_a(json.dumps(df)))
                time.sleep(10)
        except Exception as e:
            logging.exception(e)

    def simulation_b():
        """A function to simulate the given parameters and generate random values between the limits after every 10 secs
            and convert the dataframe to json file and then to a string
            params:none
            return:returns the randomly generated numbers in json string format every 10 secs """
        try:
            while True:
                df = pd.read_csv('scripts/speed_parameters.csv')
                df['random_numbers'] = df.apply(lambda x: np.random.uniform(x.lower_limit, x.upper_limit), axis=1)
                df = df.iloc[:,[0,3]]
                df = df.to_json(orient = 'records')
                df = json.loads(df)
                (Publisher.publish_b(json.dumps(df)))
                time.sleep(10)
        except Exception as e:
            logging.exception(e)
   




















































































