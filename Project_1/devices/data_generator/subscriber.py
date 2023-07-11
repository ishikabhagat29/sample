import paho.mqtt.client as mqtt
import psycopg2
import logging

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="project_db",
    user="postgres",
    password="1234"
)
client = mqtt.Client()
cursor = conn.cursor

class Subscriber:   
    def on_connect_a(client, userdata, flags, rc): 
        try:    
            if rc == 0:    
                print("Connected to broker")    
                global Connected                
                Connected = True                    
            else:   
                print("Connection failed")
        except Exception as e:
            logging.exception(e)    
    
    def on_message(client, userdata, message):
        print (f"Message received: "  + message.payload)
    Connected = False   
    client = mqtt.Client("random_numbers")                      
    client.subscribe("random_numbers")

    
    def on_connect_b(client, userdata, flags, rc):
        try:    
            if rc == 0:   
                print("Connected to broker")    
                global Connected               
                Connected = True                    
            else:    
                print("Connection failed")
        except Exception as e:
            logging.exception(e)    
    
    def on_message(client, userdata, message):
        print (f"Message received: "  + message.payload)    
    Connected = False   
    client.subscribe("random_parameters")
        