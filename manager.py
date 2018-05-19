#!/usr/bin/python
# -*- coding: utf-8 -*-

from tabulate import tabulate

teams = [
    {
        "id": 1,
        "name": u"Sopocka Akademia Piłkarska"
    },
    {
        "id": 2,
        "name": u"Pomorze Akademia Sportowa"
    },
    {
        "id": 3,
        "name": u"Portowiec II Gdańsk"
    },
    {
        "id": 4,
        "name": u"Zaspa Gdańsk"
    },
    {
        "id": 5,
        "name": u"KKS Koleczkowo"
    },
    {
        "id": 6,
        "name": u"AP KP Gdynia"
    },
    {
        "id": 7,
        "name": u"Oruński KP"
    },
    {
        "id": 8,
        "name": u"Morena Gdańsk"
    },
    {
        "id": 9,
        "name": u"Pomorzanin Gdynia"
    },
    {
        "id": 10,
        "name": u"KP Gdynia"
    },
    {
        "id": 11,
        "name": u"UKS 82 Klukowo"
    }
]

leagues = [
    {
        "id": 1,
        "name": u"B-Klasa Gdańsk II",
        "teams": [1,2,3,4,5,6,7,8,9,10,11]
    }
]

quit = False

def print_help():
    print("Available commands:")
    print("help exit table")

def show_table(team_list):
    position = 1
    teams_table = []
    for team in team_list:
        teams_table.append([
            position, team["name"], 0, 0, 0, 0, 0, 0, 0
        ])
        position += 1
    print(tabulate(teams_table, headers=["Pos", "Name", "Games", "Wins", "Draws", "Losses", "Scr", "Con", "Pts"]))

while quit != True:
    command = raw_input("> ")
    if command == "help":
        print_help()
    elif command == "exit":
        quit = True
    elif command == "table":
        show_table(teams)
    else:
        print_help()