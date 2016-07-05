#!/usr/bin/python3

# dbus-send --type=method_call --dest=org.gnome.ScreenSaver /org/gnome/ScreenSaver org.gnome.ScreenSaver.Lock

import dbus
import pyudev

session = dbus.SessionBus()

screen_saver_proxy = session.get_object(
    "org.gnome.ScreenSaver", "/org/gnome/ScreenSaver")
screen_saver_interface = dbus.Interface(
    screen_saver_proxy, "org.gnome.ScreenSaver")

def do_lock_session():
    screen_saver_interface.get_dbus_method("Lock")()

if __name__ == "__main__":
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem="usb")
    monitor.start()
    for device in iter(monitor.poll, None):
        if device["ACTION"] != "remove":
            continue
        if device["ID_VENDOR_FROM_DATABASE"] != "Yubico.com":
            continue
        if device["ID_MODEL_FROM_DATABASE"] != "Yubikey":
            continue
        # We just removed a Yubikey. Kick a lock.
        do_lock_session()
