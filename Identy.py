try:
	import argparse
	import sys
	import random
except (ImportError, ModuleNotFoundError) as e:
	print("Module error:", e)
	exit()
else:
	...
	# print("Modules imported successfully")

BOYS_NAMES_FILE = "data/boys.txt"
GIRLS_NAMES_FILE = "data/girls.txt"

SURNAMES_FILE = "data/surnames.txt"

COUNTRIES_FILE = "data/countries.txt"

POSSIBLE_AGE = range(16, 35)

VERSION = "0.0.0"

class Person():
	def __init__(self, name=None, surname=None, patronymic=None, nicknames=None, age=None, sex=None, married=None, nationality=None, email=None, characteristics=None, preferences=None):
		self.name = name
		self.surname = surname
		self.patronymic = patronymic
		self.nicknames = nicknames
		self.age = age
		self.sex = sex
		self.married = married
		self.nationality = nationality
		self.email = email
		self.characteristics = characteristics
		self.preferences = preferences
		# security level, passwords, favorite color, birth

	def Generate(self):
		# sex, age, name, surname, patronymic, phone, email, pets, preferences
		if not self.sex:
			self.sex = "man" if random.getrandbits(1) else "woman" # True/False?

		if not self.married:
			self.married = "yes" if random.getrandbits(1) else "no"

		if not self.age:
			self.age = random.randint(POSSIBLE_AGE.start, POSSIBLE_AGE.stop)
			# minimized = (POSSIBLE_AGE.stop - POSSIBLE_AGE.start) / 4
			# Maybe int instead of round?
			# self.age = round(self.age + round(random.randint(round(POSSIBLE_AGE.start + minimized), round(POSSIBLE_AGE.stop - minimized))) / 2)

		if not self.name:
			with open(BOYS_NAMES_FILE if self.sex == "man" else GIRLS_NAMES_FILE, 'r') as names:
				self.name = random.choice(names.read().split('\n'))

		if not self.surname:
			with open(SURNAMES_FILE, 'r') as surnames:
				self.surname = random.choice(surnames.read().split('\n'))

		if not self.nationality:
			with open(COUNTRIES_FILE, 'r') as countries:
				self.nationality = random.choice(countries.read().split('\n'))

		if not self.characteristics:
			self.characteristics = {}
			self.characteristics["psychological type"] = random.choice(["introvert", "extrovert"])
			self.characteristics["temperament"] = random.choice(["phlegmatic", "melancholic"]) if self.characteristics["psychological type"] == "introvert" \
				else random.choice(["chorelic", "sanguine"])

			goodTraits = ["generosity", "integrity", "loyalty", "devoted", "loving", "kindness", "sincerity", \
				"self-control", "peaceful", "faithful", "patience", "determination", "persistence", "open-minded", \
				"fair", "cooperative", "tolerant", "optimistic"]
			badTraits = ["dishonest", "disloyal", "unkind", "mean", "rude", "disrespectful", "impatient", "greed", \
				"abrasive", "pessimistic", "cruel", "unmerciful", "narcissistic", "obnoxious", "malicious", "pettiness", \
				"quarrelsome", "caustic", "selfish", "unforgiving"]

			self.characteristics["character"] = [random.choice(goodTraits), random.choice(goodTraits), \
				random.choice(badTraits), random.choice(badTraits)]

		if not self.preferences:
			self.preferences = {}
			self.preferences["color"] = random.choice(["red", "green", "blue", "orange", "white", "black", "yellow", "purple", "silver", \
				"gold", "pink", "violet", "cyan", "azure", "mint"])
			self.preferences["pet"] = random.choice(["dogs", "cats", "other"])

		if not self.nicknames:
			self.nicknames = [self.name + self.surname[0]]

		if not self.email:
			self.email = [self.name.lower() + self.surname.lower() + "@example.com"]

			# if random.getrandbits(1):
			self.email += [self.name.lower() + '.' + self.surname.lower() + "@example.com"]
			# if random.getrandbits(1):
			# 	self.email += [self.name.lower() + self.surname[0].lower() + "@example.com"]
			# if random.getrandbits(1):
			self.email += [self.name[0].lower() + self.surname.lower() + "@example.com"]
			# if random.getrandbits(1):
			# 	self.email += [self.name.lower() + '_' + self.surname.lower() + "@example.com"]

if __name__ == "__main__":
	print('''  ___    _            _         
 |_ _|__| | ___ _ __ | |_ _   _ 
  | |/ _` |/ _ \\ '_ \\| __| | | |
  | | (_| |  __/ | | | |_| |_| |
 |___\\__,_|\\___|_| |_|\\__|\\__, |
                          |___/ ''', "v" + VERSION, "\n")

	parser = argparse.ArgumentParser(description="Identy identity generator")
	parser.add_argument("--info", action="store_true", help="Show tool info")
	parser.add_argument("-g", "--generate", action="store_true", help="Generate indentity")
	# parser.add_argument("--seed", help="Generate indentity with custom random seed", metavar="SEED")

	# parser.add_argument("-n", help="Specify name", metavar="NAME")
	# parser.add_argument("-s", help="Specify surname", metavar="SURNAME")
	# parser.add_argument("-p", help="Specify patronymic", metavar="PATRONYMIC")
	# parser.add_argument("-x", help="Specify sex", metavar="SEX")

	args = parser.parse_args()

	if not len(sys.argv) > 1:
		print("No arguments specified.")
		parser.print_help()
	elif args.info:
		print("This project built on other different projects. You can find them here:")
		print("github.com")
	else:
		print("Creating new identity...")

		identity = Person()
		identity.Generate()

		print("Done!\n")

		print("Full name:", identity.name, identity.surname, identity.patronymic if identity.patronymic else "")
		print("Nicknames:", '; '.join(identity.nicknames))
		print("Age:", identity.age)
		print("Sex:", identity.sex)
		print("Married:", identity.married.capitalize())
		print("Nationality:", identity.nationality, "(might not fit with the name)")
		print("Email ideas:", '; '.join(identity.email))
		print("Character:")
		for spec in identity.characteristics:
			print('', spec.capitalize() + ':', identity.characteristics[spec] if type(identity.characteristics[spec]) is not list\
				else '; '.join(identity.characteristics[spec]))
		print("Personal preferences:")
		for spec in identity.preferences:
			print('', spec.capitalize() + ':', identity.preferences[spec])