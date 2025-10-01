# The purpose of this code is to capture the essentials necessary to read and write
# data from csv and JSON file strucutres, using a dictionary within local memory.

import csv
import json
import csv_dict_object

def main():

	entry_list = dict()

	menu(entry_list)
	
def menu(entry_list):

	while(True):
	
		print("\n************")
		print("1. Add entry")
		print("2. Read data from csv")
		print("3. Write data to csv")
		print("4. Write data to JSON")
		print("5. Show entry list in memory")
		print("6. Quit")
		print("**************\n")
		
		selection = int(input("Please select option\n"))
		
		if selection == 1:
		
			entry_list = add_entry(entry_list)
			
		elif selection == 2:
		
			entry_list = read_data_from_csv(entry_list)
			
		elif selection == 3:
		
			write_data_to_csv(entry_list)

		elif selection == 4:

			write_data_to_JSON(entry_list)
			
		elif selection == 5:

			if len(entry_list) == 0:

				print("\nNo objects in memory...\n")

			else:
		
				for entry in entry_list:
		
					print("\nName:", entry_list[entry].name)
					print("Age:", entry_list[entry].age)
					print("Serial:", entry_list[entry].serial)
					print("\n")

		elif selection == 6:

			exit()
			
		else:
		
			print("Invalid choice\n")

def add_entry(entry_list):

	name = input("Enter the name:\n")
	age = input("Enter the age:\n")
	serial = input("Enter the serial no.:\n")
	
	entry = csv_dict_object.Csv_Dict_Object(name)
	entry.age = age
	entry.serial = serial
	entry_list[name] = entry
	
	return entry_list

def add_entry_from_reader(entry_list, name, age, serial):

	entry = csv_dict_object.Csv_Dict_Object(name)
	entry.age = age
	entry.serial = serial
	entry_list[name] = entry

	return entry_list	
	
def read_data_from_csv(entry_list):

	print("Reading data from csv file...")
	current_file = input("Please enter the filename, excluding extension:\n")
	current_file = current_file + ".csv"
	print("\nFound entries... Adding to dictionary\n")

	with open(current_file, newline='') as csvfile:

		reader = csv.DictReader(csvfile)

		for row in reader:
			name = row['name']
			age = row['age']
			serial = row['serial']
			print("\n******\nName:", name, "\nAge:", age, "\nSerial:", serial)
			entry_list = add_entry_from_reader(entry_list, name, age, serial)

	return entry_list
	
def write_data_to_csv(entry_list):

	print("\nWriting data to csv file with append method...\n")
	
	current_file = input("Please enter the filename, excluding extension:\n")
	current_file = current_file + ".csv"
	
	with open(current_file, 'a', newline='') as csvfile:
	
			fieldnames = ['name', 'age', 'serial']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
			writer.writeheader()
			
			for entry in entry_list:
				row = {'name' : entry_list[entry].name, 'age' : entry_list[entry].age, 'serial' : entry_list[entry].serial}
				writer.writerow(row)

def write_data_to_JSON(entry_list):

	print("\nWriting data to json file with append method...\n")
	
	current_file = input("Please enter the filename, excluding extension:\n")
	current_file = current_file + ".jl"

	json_entry_dict = {}

	with open(current_file, 'a') as jsonfile:

		for entry in entry_list:

			json_entry_dict.update({"name" : entry_list[entry].name, "age" : entry_list[entry].age, "serial" : entry_list[entry].serial})
			
			json.dump(json_entry_dict, jsonfile)

main()
