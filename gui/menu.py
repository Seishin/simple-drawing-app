from Tkinter import *

class Menu:

	def __init__(self, root, drawing_plate):
		""" Setting up the menu frame. """

		self.__drawing_plate = drawing_plate
		self.__btn_frame = Frame(root, borderwidth = 1)
		self.__btn_frame.pack(fill="x", side=TOP)

		self.__init_ui()
	
	def __init_ui(self):
		""" Initializing the UI components. """ 

		self.__btn = Button(self.__btn_frame, text="Line", command=self.__select_line)
		self.__btn.pack(side=LEFT)

		self.__btn = Button(self.__btn_frame, text="Circle", command=self.__select_circle)
		self.__btn.pack(side=LEFT)

		self.__btn = Button(self.__btn_frame, text="Rectangle", command=self.__select_rect)
		self.__btn.pack(side=LEFT)

		self.__btn = Button(self.__btn_frame, text="Clear", command=self.__clear)
		self.__btn.pack(side=RIGHT)

	# Buttons events
	def __select_line(self):
		self.__drawing_plate.set_primitive("line")

	def __select_circle(self):
		self.__drawing_plate.set_primitive("circle")

	def __select_rect(self):
		self.__drawing_plate.set_primitive("rect")

	def __clear(self):
		self.__drawing_plate.clear()