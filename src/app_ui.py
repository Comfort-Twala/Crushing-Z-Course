# Imports
import questionary, os, time, datetime, random, string
from rich.console import Console
from rich.progress import track

class AppUI:
	def __init__(self):
		self.console = Console()
		self.clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

	def header(self, topic: str):
		self.console.print("##############################", style="green")
		self.console.print(topic.center(30), style="bold cyan")
		self.console.print("##############################", style="green")

	def choices(self, query: str, choices: list):
		return questionary.select(
			query, choices=choices
		).ask()

	def progressBar(self, duration: int, description: str):
		for progress in track(range(duration * 4), description=description):
			time.sleep(0.25)
