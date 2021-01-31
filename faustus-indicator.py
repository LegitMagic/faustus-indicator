#!/usr/bin/python3

import signal
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3

class Indicator():
	def __init__(self):
		self.app = 'faustus-indicator'
		iconpath = ""
		self.indicator = AppIndicator3.Indicator.new(
			self.app, iconpath,
			AppIndicator3.IndicatorCategory.OTHER)
		self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)       
		self.indicator.set_menu(self.menu())

	def menu(self):
		menu = Gtk.Menu()

		quiet = Gtk.RadioMenuItem(label='Quiet')
		normal = Gtk.RadioMenuItem(label='Normal')
		turbo = Gtk.RadioMenuItem(label='Turbo')
		seperator = Gtk.SeparatorMenuItem()
		quit_button = Gtk.MenuItem(label='Quit')

		menu.append(quiet)
		menu.append(normal)
		menu.append(turbo)
		menu.append(seperator)
		menu.append(quit_button)

		quiet.connect('activate', self.quiet)
		normal.connect('activate', self.normal)
		turbo.connect('activate', self.turbo)
		quit_button.connect('activate', self.stop)

		quiet.join_group(turbo)
		normal.join_group(turbo)

		menu.show_all()
		return menu

	def quiet(self, source):
		#Set /sys/devices/platform/faustus/throttle_thermal_policy to 2
		#Set cpu govenor to powersave
		
		print("quiet")

	def normal(self, source):
		#Set /sys/devices/platform/faustus/throttle_thermal_policy to 0
		#Set cpu govenor to ondemand

		print("peformance")

	def turbo(self, source):
		#Set /sys/devices/platform/faustus/throttle_thermal_policy to 1
		#Set cpu govenor to performnance

		print("turbo")	

	def stop(self, source):
		Gtk.main_quit()

Indicator()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()