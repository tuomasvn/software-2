class Publication:
	def __init__(self, name):
		self.name = name

class Book(Publication):
	def __init__(self, name, author, pages):
		super().__init__(name)
		self.author = author
		self.pages = pages

	def print_information(self):
		print(f'''
		---BOOK---
		Name: {self.name}
		Author: {self.author}
		Page count: {self.pages}
		''')

	
class Magazine(Publication):
	def __init__(self, name, chief):
		super().__init__(name)
		self.chief = chief

	def print_information(self):
		print(f'''
		---MAGAZINE---
		Name: {self.name}
		Chief editor: {self.chief}
		''')

donduc = Magazine("Donald Duck", "Aki Hyyppä")

cno6 = Book("Compartment No. 6", "Compartment No. 6", "192")

donduc.print_information()

cno6.print_information()