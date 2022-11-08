#!/usr/bin/python3
__author__ = "Walter Prorok"
__date__ = "10-9-2020"
__email__ = "wprorok@ubreakifix.com"

import webbrowser
import os

ubif_urls = [
    "https://app.slack.com/client/T01645ULG86/C030G5MPRJ9",
    "https://www.pandora.com",
    "https://keep.google.com/u/0/",
    "https://laravel.com/docs/6.x",
    "https://ubreakifix.atlassian.net/wiki/home",
    "https://ubreakifix.atlassian.net/jira/your-work",
    "https://github.com/ubreakifix/biffy",
    "https://dev-prorok.ubif-nonprod.net/",
]


def ubif_sites_browser():
    """Open the browser and new tabs"""
    for url in ubif_urls:
        print(url)
        webbrowser.open(url, new=2)


def open_google():
    webbrowser.open('https://google.com')


def clear_screen():
    os.system('cls')


def menu():
    while True:
        print("\nMenu:\n\t1. Launch sites\n\t2. Exit")
        user_input = input("\nPlease select an option: ")

        # 1 open browser sites
        if user_input == str("1"):
            ubif_sites_browser()
            clear_screen()
        # 2 exit program
        elif user_input == str("2"):
            exit()
        else:
            print("\nSorry that is not a valid command. Please try again.\n")
            continue


if __name__ == "__main__":
    menu()
    exit()
