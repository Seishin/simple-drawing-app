from Tkinter import *
from gui.drawing_plate import Drawing_Plate
from gui.menu import Menu

class Main_App(Frame):

	def __init__(self):
		""" Initializing and configuring the main frame of the application. """

		Frame.__init__(self)
		self.master.geometry("800x600")
		self.master.title("Simple App")
		self.pack(expand=True, fill="both")

		self.__init_ui()

	def __init_ui(self):
		""" Initilizing the UI componenents. """

		self.__drawing_plate = Drawing_Plate(self)
		self.__menu = Menu(self, self.__drawing_plate)

def main():
	Main_App().mainloop()

if __name__ == "__main__":
	main()