# Jubilant Robot

[![Codeship Status for matthewturner/jubilant-guide](https://app.codeship.com/projects/ccbbe790-78de-0137-931c-7abc16dc9d64/status?branch=master)](https://app.codeship.com/projects/350367) [![Maintainability](https://api.codeclimate.com/v1/badges/be4321a5fd161a1c2d8a/maintainability)](https://codeclimate.com/github/matthewturner/jubilant-guide/maintainability)

Based on the [Adafruit Metro M0 Express](https://www.amazon.co.uk/Adafruit-METRO-M0-Express-CircuitPython/dp/B071P145RG/ref=sr_1_1), the robot covers every part of the floor of a given room.

### Simulator
The simulator allows you to create an approximate map of the room and run the robot in that virtual world.

To run the simulator:

`python ./world.py`

### Deployment
To deploy to the Metro M0 Express:

Run the Visual Studio Code **build** task

_or_

Copy `main.py` and the `jubilant` folder to the Metro M0 Express
