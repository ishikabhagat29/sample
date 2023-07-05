import paho.mqtt.client as mqtt
import logging
class subscriber:
    def on_connect(client, userdata, flags, rc):
        try:
            print(f"Connected with result code {str(rc)}")
            client.subscribe("random_numbers")
        except Exception as e:
            logging.exception(e)

    def on_message(client,userdata, msg):
        try:
            print(f"Received message: {str(msg.payload.decode())}")
        except Exception as e:
            logging.exception(e)

client = mqtt.Client()
client.on_connect = subscriber.on_connect
client.on_message = subscriber.on_message

client.connect("localhost", 1883, 61)
client.loop_forever()
