# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import	QApplication, QMainWindow
import sys



class Window(object):
	def __init__(self, widget, *config):
		'''
		: app: main widget
		'''
		self.widget = widget
		self.config = config or []

	def _build_window(self):
		pass

	def view(self, v, **options):
		def decorator(f):
			print(options)
			return f
		return decorator

	def show(self):
		qapp = QApplication(sys.argv)
		if self.widget:
			app = self.widget()
			app.show()
			sys.exit(qapp.exec_())
