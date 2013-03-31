class Line():

	def __init__(self, root, event):
		self.__root = root
		self.__x = event.x
		self.__y = event.y

		self.__bg = "green"

	def set_color(self, color):
		self.__bg = color

	def draw(self, event):
		self.__rect = self.__root.create_line(self.__x, self.__y, event.x, event.y, fill=self.__bg)