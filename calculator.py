#!/usr/bin/python3

import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GLib

mainloop = None

class Calculator(dbus.service.Object):
	#constructor
	def __init__(self, bus):
		self.path = '/com/example/calculator'
		dbus.service.Object.__init__(self, bus, self.path)

	@dbus.service.method("com.example.calculator_interface",
			in_signature='ii',
			out_signature='i')
	def Add(self, a1, a2):
		sum = a1 + a2
		print(a1, " + ", a2, " = ", sum)
		return sum
	@dbus.service.method("com.example.calculator_interface",
			in_signature='ii',
			out_signature='i')
	def Substract(self, b1, b2):
		rest = b1 - b2
		print(b1, " - ", b2, " = ", rest)
		return rest
	@dbus.service.method("com.example.calculator_interface",
			in_signature='ii',
			out_signature='i')
	def Multiply(self, c1, c2):
		mult = c1 * c2
		print(c1, " * ", c2, " = ", mult)
		return mult
	@dbus.service.method("com.example.calculator_interface",
			in_signature='ii',
			out_signature='d')
	def Divide(self, d1, d2):
		div = d1/d2
		print(d1, " / ", d2, " = ", div)
		return float(div)

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SystemBus()

calc = Calculator(bus)

mainloop = GLib.MainLoop()
print("waiting for some calculations to do ...")

mainloop.run()
