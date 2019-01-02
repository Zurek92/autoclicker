# Autoclicker
A simple project to auto control mouse.

#### Prepare and install whl file
1. ``make venv`` creates virtualenv which allow use autoclicker in developer mode.
2. ``make install_dependencies`` to install required dependencies in system linux
3. ``make create_whl`` creates whl file in ``dist/``
4. to install autoclicker just run: ``pip install <name>.whl``


#### Usage
``autoclicker scroll`` uses middle mouse button to scroll up or down

Options:
* -s (--scrolls) integer, required parameter which set how many times click middle button and in which direction, e.g.: ``-s 10``, ``-s -10``

``autoclicker click`` uses left mouse button

Options:
* -s (--screen_location) - by default if this option is not set location is taken from current mouse position e.g.: ``-s 500 450``
* -r (--repeats) - how many times script should click, e.g.: ``-r 10``
* -t (--time_break) - average time breaks between clicks in seconds e.g.: ``-t 15``
* -d (--time_different) - time deviation from the average, e.g.: ``-t 10 -d 2``, real time will be between 8 and 12 seconds
