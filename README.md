KeyCount
========

This script monitors keyboard input and increases a counter in a textfile whenever a specific key (or combination of keys) is pressed. The primary use case is an Undo counter for Twitch streams.


## Installation

You need a working Python 3 installation on your system. Then...

1. Checkout this repository
2. Open your Terminal and navigate to the repository's location
3. Install the dependencies:
```
pip install -r requirements.txt
```

## Usage

To get the count of "Undo" (`[Cmd]+[Z]`) in a text file `counter.txt`, run this in your Terminal:
```bash
KEYCOUNT_SEQUENCE='Key.cmd,z' python keycount.py
```
In case you don't know the exact names of the keys you want to monitor, you can enable debug logging, so pressing keys will be echoed to the Terminal:
```
KEYCOUNT_LEVEL=DEBUG python keycount.py
```
To stop the script, press `[Ctrl]+[c]` in the Terminal.

### Customisation

| Environment variable | Description |
| -------------------- | ----------- |
| `KEYCOUNT_LEVEL` | Level at which logs should be emitted. DEBUG will emit all keystrokes, INFO is the default. |
| `KEYCOUNT_FILENAME` | Name of the file where to store the counter |
| `KEYCOUNT_SEQUENCE` | Key or sequence of keys to monitor, delimited by `,` |
| `KEYCOUNT_DELIMITER` | Ok, so you want to monitor the `,` key being pressed? Then this value lets you customise the delimiter used in the `KEYCOUNT_SEQUENCE` |

## Known Issues

Here's a list of things that I can imagine could cause issues for you. They didn't play a role for my use case so I didn't bother implementing/fixing them but contributions are always welcome. :)

 * The script doesn't really monitor combinations, so if you press `[Cmd]`, release the key, and then press `[z]`, it would count as an undo although ideally you'd have to press both keys simultaneously.
 * On some systems, special keys such as `[Cmd]` appear not as `Key.cmd` but `Key.cmd_l` or `Key.cmd_r` depending on whether the left or right key is pressed on the keyboard. As there's no way to provide multiple sequences to a single script, some combinations pressed might go unnoticed.
