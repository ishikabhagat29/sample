import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe("random_parameters")


def on_message(client,userdata, msg):
    print(f"Received message: {str(msg.payload.decode())}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 61)
client.loop_forever()

