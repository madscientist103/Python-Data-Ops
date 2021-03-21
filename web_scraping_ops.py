# This script will take a job title, city, and state as parameters. Then, using the 
# specified search engines, provide data on job listings using web scraping.
# The results will be stored in a csv file. The user can interact with the data by 
# performing search and receiving report on the most prevalent key words in the
# listings.

# work-in-progress

import requests
from bs4 import BeautifulSoup

def main():

    search_configuration = {"Title" : "IT", "City" : "Tampa" , "State" : "FL" , "File" : "result_file.csv"}

    menu(search_configuration)

def menu(search_configuration):

    while(True):

        print("\n**************MENU****************")
        print("1. Specify Search Configuration")
        print("2. Show Current Search Configuration")
        print("3. Execute Search Operation")
        print("4. Read Data File")
        print("5. Analyze Data")
        print("6. Quit\n")
        print("************************************\n")

        user_selection = int(input("\nPlease enter your selection\n"))

        if user_selection == 1:

            #Specify Search Configuration
            search_configuration = specify_search_configuration(search_configuration)

        elif user_selection == 2:

            #Show Current Search Configuration
            show_search_configuration(search_configuration)

        elif user_selection == 3:

            content = execute_search_operation(search_configuration)

            search_result = content.find_all("h2", {"class":"title"})

            with open("web_scrape_search_result.html", "w", encoding='utf-8') as file:
                file.write(str(search_result))
            

        elif user_selection == 6:

            quit()

        else:

            print("\nInvalid Selection! Please try again...\n")


def specify_search_configuration(search_configuration):

    print("\nEnter Search Configuration Options\n")

    title = input("\nPlease enter the position title to search (spaces will be replaced with \"+\"):\n")
    title = "+".join(title.split())
    city = input("\nPlease enter the city to search:\n")
    city = "+".join(city.split())
    state = state_search_validation()
    target_file = input("\nPlease specify the target data file, excluding file extension (file will be created as .csv):\n")
    target_file = target_file + ".csv"

    search_configuration = {"Title" : title , "City" : city , "State" : state , "File" : target_file}

    return search_configuration

def show_search_configuration(search_configuration):

    print("\nDisplaying Search Configuration Options\n")

    print("\nPosition Title:", search_configuration["Title"])
    print("City:", search_configuration["City"])
    print("State:", search_configuration["State"])
    print("Output File:", search_configuration["File"], "\n")

    return search_configuration

def execute_search_operation(search_configuration):

    search_url = "https://www.indeed.com/jobs?q=" + search_configuration["Title"] + "&l=" + search_configuration["City"] + "%2C+" + search_configuration["State"]

    print("The url for your search parameters is", search_url)

    output = requests.get(search_url)
    content = BeautifulSoup(output.text, 'lxml')

    return content

def state_search_validation():

    state_list = ["AL", "AK", "AS", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "GU", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", 
    "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "MP", "OH", "OK", "OR", "PA", "PR", "RI",
    "SC", "SD", "TN", "TX", "UT", "VT", "VA", "VI", "WA", "WV", "WI", "WY"]

    running = 1

    while(running == 1):

        state = input("\nPlease enter the two character abbreviation for state:\n")

        state = state.upper()

        if len(state) != 2:

            print("\nThe state abbreviation must be two characters")

        elif (state not in state_list):

            print("\nInvalid state abbreviation")

        else:

            return state




main()