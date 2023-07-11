import logging
from Project_1.generators.services.services import item
import paho.mqtt.client as mqtt

class Publisher():
    def on_connect(client, userdata, flags, rc):
        """A function to connect the MQTT to the serever
            params:client,userdata,flags,rc
            return:prints  the connected result code"""
        try:
            logging.info(f"Connected with result code {str(rc)}")
        except Exception as e:
            logging.exception(e)

    def publish_a(message):
        """A function to publish the randomly generated energy parameters
            params:message
            return:returns the published message in VSMQTT """
        try:
            client = mqtt.Client()
            client.on_connect = Publisher.on_connect
            client.connect("localhost", 1883,61)
            client.loop_start()
            client.publish("random_numbers" , message)
            print("published",message,'\n')
            item.create_an_item(str(message))
        except Exception as e:
            logging.exception


    def publish_b(message):
        """A function to publish the randomly generated energy parameters
            params:message
            return:returns the published message in VSMQTT """
        try:
            client = mqtt.Client()
            client.on_connect = Publisher.on_connect
            client.connect("localhost", 1883,61)
            client.loop_start()
            client.publish("random_parameters" , message)
            print("published",message,'\n')
            item.create_an_(str(message))
        except Exception as e:
            logging.exception

