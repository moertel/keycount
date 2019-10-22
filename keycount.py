import logging
import os
import sys
import threading

from halo import Halo
from pynput.keyboard import Key, Listener


logging.basicConfig(level=os.getenv('KEYCOUNT_LEVEL', 'INFO'))

FILENAME = os.getenv('KEYCOUNT_FILENAME', 'counter.txt')
DELIMITER = os.getenv('KEYCOUNT_DELIMITER', ',')
SEQUENCE = os.getenv('KEYCOUNT_SEQUENCE', 'Key.cmd,z').split(DELIMITER)

matcher = 0

def on_release(key):
    global matcher
    key = str(key).strip("'")
    logging.debug(f'Key pressed: {key}')

    if key in SEQUENCE and SEQUENCE[matcher] == key:
        logging.debug('Key matched in a streak')
        matcher += 1
    else:
        logging.debug('No match, reset the streak')
        matcher = 0

    if matcher == len(SEQUENCE):
        logging.debug('Entire combination matched')
        try:
            with open(FILENAME, 'r+') as counter_file:
                current_count = int(counter_file.readline())
        except (FileNotFoundError, ValueError):
            current_count = 0
        with open(FILENAME, 'w+') as counter_file:
            counter_file.write(str(current_count + 1))

    matcher = matcher % len(SEQUENCE)


with Halo(text='Watching...', spinner='dots'):
    try:
        with Listener(on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        print('\nStopped')
        sys.exit(0)
