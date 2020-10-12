#!/usr/bin/python3
__author__ = "Walter Prorok"
__date__ = "10-9-2020"
__author__ = "wprorok@ubreakifix.com"

import webbrowser
import subprocess

ubif_urls = [
    "https://mail.google.com/mail/u/0/#inbox",
    "https://calendar.google.com/calendar/r",
    "https://keep.google.com/u/0/",
    "https://drive.google.com/drive/my-drive",
    "https://ubreakifix.atlassian.net/wiki/home",
    "https://ubreakifix.atlassian.net/jira/your-work",
    "https://github.com/",
    "https://console.aws.amazon.com/cloud9/ide/0be6d983072043d5b8f900c7909e8555",
    "https://dev-prorok.ubif.net/",
]


def ubif_sites_browser():
    for url in ubif_urls:
        print(url)
        webbrowser.open(url, new=2)


def open_phpstorm():
    subprocess.Popen(['C:\\Users\\walter.prorok\\AppData\\Local\\JetBrains\\PhpStorm 2020.1.2\\bin\\phpstorm64.exe'])


def open_slack():
    subprocess.Popen(['C:\\Users\\walter.prorok\\AppData\\Local\\slack\\slack.exe'])


def open_postman():
    subprocess.Popen(['C:\\Users\\walter.prorok\\AppData\\Local\\Postman\\Postman.exe'])


def menu():
    while True:
        print("\nMenu:\n\t1. Launch sites\n\t2. Launch programs\n\t3. Launch sites and programs\n\t4. Exit")
        user_input = input("\nPlease select an option: ")

        if user_input == str("1"):
            ubif_sites_browser()
        elif user_input == str("2"):
            open_phpstorm()
            open_slack()
            open_postman()
        elif user_input == str("3"):
            ubif_sites_browser()
            open_phpstorm()
            open_slack()
            open_postman()
        elif user_input == str("4"):
            exit()
        else:
            print("\nSorry that is not a valid command. Please try again.\n")
            continue


if __name__ == "__main__":
    menu()
    exit()
