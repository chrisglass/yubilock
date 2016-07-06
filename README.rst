Yubilock
==============


Yubilock is a simple program that will lock your screen if a Yubikey is removed from the computer.

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
