import time
import pandas as pd
import numpy as np
import logging
import json
from Scripts.publisher.publisher import publisher
class data_generation:
    def simulation():
        """A function to simulate the given parameters and generate random values between the limits after every 10 secs
            and convert the dataframe to json file and then to a string
            params:none
            return:returns the randomly generated numbers in json string format every 10 secs """
        try:
            while True:
                df = pd.read_csv('Scripts/energy_parameters.csv')
                df['random_numbers'] = df.apply(lambda x: np.random.uniform(x.lower_limit, x.upper_limit), axis=1)
                df = df.iloc[:,[0,3]]
                # df = df.set_index('Parameter')
                df = df.to_json(orient = 'records')
                # df = json.dumps(df)
                (publisher.publish(json.dumps(df)))
                # print(df,"\n","---")
                time.sleep(10)
        except Exception as e:
            logging.exception(e)

        




















































































