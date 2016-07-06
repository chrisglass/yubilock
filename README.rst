Yubilock
==============


Yubilock is a simple program that will lock your screen if a Yubikey is removed from the computer.

Why?
----

First of all: why not? :)

I find myself working from cybercafes/coworking spaces quite often, and realized
whenever I had to leave my computer, I systematically did two things:

    1. Remove my Yubikey from the USB port it's plugged into
    2. Lock my screen

This program is a simple attempt at optimising this aspect of my life. Removing
the Yubikey now triggers a screen lock!

Simple!

Dependencies
------------

Yubilock is currently thought to be run on Ubuntu, using python3. As such, the
following (system) dependencies are required::

    sudo apt-get install python3 python3-pyudev python3-dbus

This program depends on DBus's system and session busses to be available to the
running user. Therefore, it needs a working DBus environment. Normal logged in
users on a default Ubuntu install should have this, but i.e. containers won't
by default.

Instructions
------------

Simply run the ``./yubilock.py`` script as a normal logged in user from a terminal.

It doesn't do anything fancy yet, and will simply log information about Yubikeys on
stdout.
