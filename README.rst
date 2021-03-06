Yubilock
==============


Yubilock is a simple program that will lock your screen if a `Yubikey <https://www.yubico.com/faq/yubikey/>`_ is removed from the computer.

A better solution
-------------------

As others have pointed out, it can be achieved more elegantly with a udev rule,
I'll keep this here for posterity and to serve as a reference for dbus/python3
stuff in case somebody needs it.

The udev rule in question is::

    ACTION=="remove", ATTRS{idVendor}=="1050", RUN+="/bin/loginctl lock-sessions"

Adding this to a /etc/udev/rules.d/80-yubilock.rules file should do the trick.

That will lock the screen for any USB device made by Yubico, you could add your
specifi device ID as ``ATTRS{idProduct}`` if you want to narrow that down further.

Thanks to `masta from reddit <https://www.reddit.com/r/yubikey/comments/4ri2by/a_small_utility_i_wrote_to_lock_your_screen_when/>`_!

Why?
----

First of all: why not? :)

I find myself working from cybercafes/coworking spaces quite often, and realized
whenever I had to leave my computer, I systematically did two things:

#. Remove my Yubikey from the USB port it's plugged into
#. Lock my screen

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

Simply run the ``./yubilock`` script as a normal logged in user from a terminal.

It doesn't do anything fancy yet, and will simply log information about Yubikeys on
stdout.

The future
----------

An applet? Who knows!
