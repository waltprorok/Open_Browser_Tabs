#!/usr/bin/python3

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


if __name__ == "__main__":
    ubif_sites_browser()
    open_phpstorm()
    open_slack()
    open_phpstorm()
    exit()
