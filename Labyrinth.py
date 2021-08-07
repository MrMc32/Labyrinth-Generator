import turtle, random

WinX = int(input("Screen resolution on X: "))
WinY = int(input("Screen resolution on Y: "))
List_Of_Cells = []

class Labyrinth:

	def __init__(self):
		self.main()

	def main(self):
		self.CreateScreen(WinX, WinY, "red")
		self.CreateBoundries()
		self.CreateCells()
		self.LoadCells()
		self.DrawLabyrinth()
		self.UpdateScreen()

	def CreateSingleCell(self, Posx, Posy, color):
		cell = turtle.Turtle()
		cell.hideturtle()
		cell.shape("square")
		cell.penup()
		cell.setheading(cell.towards(Posx, Posy))
		cell.forward(cell.distance(Posx, Posy))
		cell.color(color)
		cell.setheading(cell.towards(0, Posy))
		cell.showturtle()
		List_Of_Cells.append(cell)

	def LoadCells(self):
		print("Preparing cells, please wait...")
		for cell in List_Of_Cells:
			cell.hideturtle()
			cell.pendown()
			cell.shape("arrow")
			cell.shapesize(0.25, 0.25)
			cell.color("white")
		print("Cells are prepared!")

	def DrawLabyrinth(self):
		print("Creating labyrinth, please wait...")
		ID = 0
		for cell in List_Of_Cells:
			RandomPrefab = random.randint(1, 16)
			if RandomPrefab == 1:
				self.Prefab1(ID)
			elif RandomPrefab == 2:
				self.Prefab2(ID)
			elif RandomPrefab == 3:
				self.Prefab3(ID)
			elif RandomPrefab == 4:
				self.Prefab4(ID)
			elif RandomPrefab == 5:
				self.Prefab5(ID)
			elif RandomPrefab == 6:
				self.Prefab6(ID)
			elif RandomPrefab == 7:
				self.Prefab7(ID)
			elif RandomPrefab == 8:
				self.Prefab8(ID)
			elif RandomPrefab == 9:
				self.Prefab9(ID)
			elif RandomPrefab == 10:
				self.Prefab10(ID)
			elif RandomPrefab == 11:
				self.Prefab11(ID)
			elif RandomPrefab == 12:
				self.Prefab12(ID)
			elif RandomPrefab == 13:
				self.Prefab13(ID)
			elif RandomPrefab == 14:
				self.Prefab14(ID)
			elif RandomPrefab == 15:
				self.Prefab15(ID)
			elif RandomPrefab == 16:
				self.Prefab16(ID)
			
			ID += 1
		print("Labyrinth created!")

	def Prefab1(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.right(90)
		cell.forward(10)
		cell.right(180)
		cell.forward(20)
		cell.hideturtle()

	def Prefab2(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.left(90)
		cell.forward(10)
		cell.left(180)
		cell.forward(20)
		cell.hideturtle()

	def Prefab3(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.right(180)
		cell.forward(10)
		cell.left(180)
		cell.forward(20)
		cell.hideturtle()

	def Prefab4(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.forward(10)
		cell.left(180)
		cell.forward(20)
		cell.hideturtle()

	def Prefab5(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.right(90)
		cell.forward(10)
		cell.left(90)
		cell.forward(10)
		cell.hideturtle()

	def Prefab6(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.right(90)
		cell.forward(10)
		cell.right(90)
		cell.forward(10)
		cell.hideturtle()

	def Prefab7(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.left(90)
		cell.forward(10)
		cell.left(90)
		cell.forward(10)
		cell.hideturtle()

	def Prefab8(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.left(90)
		cell.forward(10)
		cell.right(90)
		cell.forward(10)
		cell.hideturtle()

	def Prefab9(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.right(180)
		cell.forward(10)
		cell.right(90)
		cell.forward(10)
		cell.hideturtle()

	def Prefab10(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.right(180)
		cell.forward(10)
		cell.left(90)
		cell.forward(10)
		cell.hideturtle()

	def Prefab11(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.forward(10)
		cell.left(90)
		cell.forward(10)
		cell.hideturtle()

	def Prefab12(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.forward(10)
		cell.right(90)
		cell.forward(10)
		cell.hideturtle()

	def Prefab13(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.right(90)
		cell.forward(10)
		cell.right(90)
		cell.forward(10)
		cell.right(180)
		cell.forward(20)
		cell.hideturtle()

	def Prefab14(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.left(90)
		cell.forward(10)
		cell.right(90)
		cell.forward(10)
		cell.right(180)
		cell.forward(20)
		cell.hideturtle()

	def Prefab15(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.right(180)
		cell.forward(10)
		cell.right(90)
		cell.forward(10)
		cell.right(180)
		cell.forward(20)
		cell.hideturtle()

	def Prefab16(self, ID):
		cell = List_Of_Cells[ID]
		cell.showturtle()
		cell.forward(10)
		cell.right(90)
		cell.forward(10)
		cell.right(180)
		cell.forward(20)
		cell.hideturtle()

	def CreateBoundries(self):

		print("Creating boundries, please wait...")

		arrow = turtle.Turtle()
		arrow.hideturtle()
		arrow.pensize(2)
		arrow.penup()
		arrow.color("white")
		arrow.setheading(arrow.towards(-WinX/2, WinY/2))
		arrow.forward(arrow.distance(-WinX/2, WinY/2))
		arrow.setheading(arrow.towards(WinX/2, WinY/2))
		arrow.showturtle()
		arrow.pendown()
		arrow.forward(arrow.distance(WinX/2+1, WinY/2))
		arrow.setheading(arrow.towards(WinX/2, -WinY/2))
		arrow.forward(arrow.distance(WinX/2, -WinY/2-1))
		arrow.setheading(arrow.towards(-WinX/2, -WinY/2))
		arrow.forward(arrow.distance(-WinX/2-1, -WinY/2))
		arrow.setheading(arrow.towards(-WinX/2, WinY/2))
		arrow.forward(arrow.distance(-WinX/2, WinY/2))
		arrow.setheading(arrow.towards(WinX/2, WinY/2))
		arrow.hideturtle()

		print("Boundries created!")

	def CreateCells(self):

		print("Creating cells, please wait...")

		LeftSideScreen	= -WinX/2 + 10
		UpSideScreen 	= WinY/2 - 10

		HowManyCellsOnX = WinX / 20
		HowManyCellsOnY = WinY / 20

		for i in range(int(HowManyCellsOnY)):
			for i in range(int(HowManyCellsOnX)):
				self.CreateSingleCell(LeftSideScreen, UpSideScreen, "black")
				LeftSideScreen += 20
			UpSideScreen -= 20
			LeftSideScreen = -WinX/2 + 10

		print(str(len(List_Of_Cells)) + " Cells created!")

	def CreateScreen(self, ScreenX, ScreenY, Color):
		Screen = turtle.Screen()
		Screen.setup(ScreenX, ScreenY)
		Screen.bgcolor(Color)
		print("Ctrl + C to exit program, in console!")

	def UpdateScreen(self):
		while True:
			turtle.Screen().update()

if __name__ == "__main__":
	Labyrinth()