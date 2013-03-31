from Tkinter import *
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from primitives.circle import Circle
from primitives.rectangle import Rectangle 
from primitives.line import Line

class Drawing_Plate:
	""" A class that represents the drawing plate on which the obejects will be drawn. """

	# Selected primitive to be drawn
	__primitive = ""

	# A dictionary which holds the draging coords of the selected item
	__drag_data = {"x" : 0, "y" : 0, "item" : None}

	def __init__(self, root):
		""" Initializing the drawing plot and binding the mouse events. """

		self.__drawing_plate = Canvas(root, bg="white")
		self.__drawing_plate.pack(side=BOTTOM, fill="both", expand=True)

		self.__drawing_plate.bind("<ButtonPress-1>", self.__on_left_button_press)
		self.__drawing_plate.bind("<ButtonRelease-1>", self.__on_left_button_release)
		self.__drawing_plate.bind("<B3-Motion>", self.__on_motion)
		self.__drawing_plate.bind("<ButtonPress-3>", self.__on_right_button_press)
		self.__drawing_plate.bind("<ButtonRelease-3>", self.__on_right_button_release)
		self.__drawing_plate.bind("<ButtonPress-2>", self.__on_middle_button_press)

	def __on_left_button_press(self, event):
		""" Mouse left-button press. Checks the selected primitive and creates an object of it. """

		if self.__primitive == "line":
			self.__object = Line(self.__drawing_plate, event)
		elif self.__primitive == "circle":
			self.__object = Circle(self.__drawing_plate, event)
		elif self.__primitive == "rect":
			self.__object = Rectangle(self.__drawing_plate, event)
		else:
			pass
		
	def __on_left_button_release(self, event):
		""" Mouse left-button release. Invokes the draw method of the primitive object and draws it. """
		
		if self.__primitive != "":
			self.__object.draw(event)
		else:
			pass

	def __on_right_button_press(self, event):
		""" Mouse right-button press. Finds the closest item and selects it. """

		if len(self.__drawing_plate.find_closest(event.x, event.y)) > 0:
			obj = self.__drawing_plate.find_closest(event.x, event.y)[0]

			self.__drag_data["item"] = obj
			self.__drag_data["x"] = event.x
			self.__drag_data["y"] = event.y

	def __on_right_button_release(self, event):
		""" Mouse right-button release. When the moving process is finished, nullifies the drag_data dictionary. """

		self.__drag_data["item"] = None
		self.__drag_data["x"] = 0
		self.__drag_data["y"] = 0

	def __on_motion(self, event):
		""" Mouse right-button on motion. Moving the object on the new coords given by the mouse motion event. """

		if self.__drag_data["item"] != None:
			delta_x = event.x - self.__drag_data["x"]
			delta_y = event.y - self.__drag_data["y"]

			self.__drawing_plate.move(self.__drag_data["item"], delta_x, delta_y)

			self.__drag_data["x"] = event.x
			self.__drag_data["y"] = event.y

	def __on_middle_button_press(self, event):
		""" Mouse middle-button press. Deletes the closest object. """

		obj = self.__drawing_plate.find_closest(event.x, event.y)
		self.__drawing_plate.delete(obj)

	def clear(self):
		""" Clears the whole drawing_plate. """

		self.__drawing_plate.delete(ALL)

	def set_primitive(self, primitive):
		""" Setting up the primitive that will be drawn. """

		self.__primitive = primitive