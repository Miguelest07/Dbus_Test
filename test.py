#! /usr/bin/python
#https://www.freedesktop.org/software/systemd/man/org.freedesktop.hostname1.html

import dbus

bus = dbus.SystemBus()
proxy = bus.get_object('org.freedesktop.hostname1','/org/freedesktop/hostname1')
interface = dbus.Interface(proxy, 'org.freedesktop.DBus.Properties')
print("---------ALL PROPERTIES-------------")
all_props = interface.GetAll('org.freedesktop.hostname1')
print(all_props)

print("---------HOSTNAME------------")
hostname = interface.Get('org.freedesktop.hostname1','Hostname')
print("The hostname is ", hostname)

