
Introduction
============

GPS parsing module.  Can parse simple NMEA data sentences from serial GPS
modules to read latitude, longitude, and more.

Installation
=============

On a LoPy, just put ``adafruit_gps.py`` into the ``lib/`` directory.

Dependencies
=============
This driver depends on:

* `MicroPython <https://github.com/micropython/micropython>`_

Usage Example
=============

See examples/simple.py for a demonstration of parsing and printing GPS location.
Please note that ``datalogging.py`` has not been ported from CircuitPython to
Micropython yet.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_gps/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
