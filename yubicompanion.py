#!/usr/bin/python3
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

    # The monitor will offer a generator that will wake up only on kernel
    # events, but will block the thread. Since this program is donig nothing
    # else, it's fine.
    for device in iter(monitor.poll, None):

        # Only consider devices with a device node, since we'll get two
        # matching devices for each even.
        if not device.device_node:
            continue

        # Make sure it's a Yubikey.
        if device["ID_MODEL_FROM_DATABASE"] != "Yubikey":
            continue
        if device["ID_VENDOR_FROM_DATABASE"] != "Yubico.com":
            continue

        # Lock the screen if the key was removed.
        if device["ACTION"] == "remove":
            print("Yubikey removed - locking screen")
            do_lock_session()
            continue
        # Just print if it was added.
        if device["ACTION"] == "add":
            print("New Yubikey added!")
            continue
