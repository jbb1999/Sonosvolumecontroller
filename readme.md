SONOS volume controller
====

Sonos volume controller is a simple program to limit sonos volume. The max volume can be configured and what it should go to. This can bypass if someone has acces to the volume and is good if you dont trust your friends at your house. It is fully configurable. 

This program uses a python libary called SoCo to interact with sonos.


.. image:: https://img.shields.io/pypi/v/soco.svg?style=flat
    :target: https://github.com/SoCo/SoCo
    :alt: Latest PyPI version

Installation
------------

Sonos volume controller requires Python 3.6 or newer.

Use pip:

``pip install soco``
``pip install time``



Sonos volume controll has bugs and can require manual ip configuration if it cant discover it.

Basic Usage
-----------

You can start by configuring config.py to how you want it, changing the ip then running main.py



Support
-------

If you need support for CSGO TUG, contact me on discord. Jbb#0001



Features
--------

Sonos volume controll supports the following features:
 - volume max
 - volume damping
 - check interval
 

Features to come
--------

I am working on these atm and may come down the line.
 - more modes if it goes over
 - email support for commands like cutoff.
Note that i have no eta for these and might not add them at all.
