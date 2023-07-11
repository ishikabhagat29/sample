import typer
from devices.data_generator.data_generator import Generation
import paho.mqtt.client as mqtt
from devices.data_generator.subscriber import Subscriber
import logging
from devices.data_generator.publisher import Publisher

app = typer.Typer()

@app.command()
def number_a(file: str = typer.Argument(..., help="Function to run")):
    try:
        Generation.simulation_a()
    except Exception as e:
        logging.exception(e)


@app.command()
def number_b(file: str = typer.Argument(..., help="Function to run")):
    try:
        Generation.simulation_b()
    except Exception as e:
        logging.exception(e)


@app.command()
def subscriber_a(file: str = typer.Argument(..., help="Function to run")):
    try:
        client = mqtt.Client()
        client.on_connect = Subscriber.on_connect_a
        client.on_message = Subscriber.on_message
        client.on_publish = Publisher.publish_a
        client.connect("localhost", 1883, 61)
        client.loop_forever()
    except Exception as e:
        logging.exception(e)

@app.command()
def subscriber_b(file: str = typer.Argument(..., help="Function to run")):
    try:
        client = mqtt.Client()
        client.on_connect = Subscriber.on_connect_b
        client.on_message = Subscriber.on_message
        client.on_publish = Publisher.publish_b
        client.connect("localhost", 1883, 61)
        client.loop_forever()
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    app()


















