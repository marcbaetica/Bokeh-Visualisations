from flask import Flask, redirect
from random import randint
from threading import Thread
from time import sleep


def change_random_number():
    while True:
        sleep(1)
        global payload
        payload['y'].append(randint(1, 20))
        payload['y'].pop(0)
        print(payload['y'][-1])


random_num = 0
payload = dict()
payload['x'] = [0, 1, 2, 3, 4, 5]
payload['y'] = [12, 3, 5, 10, 8, 1]
change_num = Thread(target=change_random_number)
change_num.start()


app = Flask('data_streamer')


@app.route('/')
def index():
    return redirect('random-number-generator')


@app.route('/random-number-generator')
def generate_number():
    # return f"""<html><body>{randint(1, 20)}</body><html>"""
    # return f'{randint(1, 20)}'  # Same thing.
    # return randint(1, 20)  # Doesn't work.
    return f'{payload}'


app.run()
