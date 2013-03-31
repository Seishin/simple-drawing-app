class Circle():

	def __init__(self, root, event):
		self.__root = root
		self.__x = event.x
		self.__y = event.y

		self.__bg = "red"

	def set_color(self, color):
		self.__bg = color

	def draw(self, event):
		self.__circle = self.__root.create_oval(self.__x, self.__y, event.x, event.y, fill=self.__bg)
