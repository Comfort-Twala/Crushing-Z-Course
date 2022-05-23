from app_ui import AppUI

class Menu:
	def __init__(self):
		self.ui = AppUI()
	
	def introduction(self):
		self.ui.console.print("hello")
		pass

	def understandingQuestion(self):
		pass

	def obtainingInput(self):
		pass

	def munipulatingData(self):
		pass

	def applyingFormula(self):
		pass

	def outputtingData(self):
		pass

	def extras(self):
		pass


if __name__ == "__main__":
	menu = Menu()
	menu.introduction()
