try:
	import sys
	import argparse
	from faker import Faker

	fake = Faker()
except (ImportError, ModuleNotFoundError) as e:
	print("Module error:", e)
	exit()

VERSION = "0.1.0"

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

	args = parser.parse_args()

	if not len(sys.argv) > 1:
		print("No arguments specified.")
		parser.print_help()
	elif args.info:
		print("This project built on other different projects. You can find them here:")
		print(" https://github.com/joke2k/faker")
	elif args.generate:
		print("Creating new identity...")

		profile = fake.profile()

		print("\nBasic information:")
		print(" Name:", profile["name"])
		print(" Sex:", "Male" if profile["sex"] == 'M' else 'Female' if profile["sex"] == 'F' else "Unknown")

		print("\nInternet:")
		print(" Username:", profile["username"])
		print(" Email:", '.'.join(profile["name"].lower().split(' ')) + "@example.com") # profile["mail"]

		print("\nDetails:")
		print(" Birthdate:", fake.date_of_birth(minimum_age=18, maximum_age=40)) # profile["birthdate"]
		print(" Blood group:", profile["blood_group"])
		print(" Address:", profile["address"].replace('\n', '; '))

		print("\nOther:")
		print(" SSN:", profile["ssn"])
		print(" Job:", profile["job"])
		print(" Residence:", profile["residence"].replace('\n', '; '))
	else:
		parser.print_help()