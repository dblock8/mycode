#!/usr/bin/env python3

    
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens    ", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

NE_animals= farms[0]["agriculture"]

for farms in farms:
    print("_", farms["name"])
    choice = input("Chose a farm!\n")

for farms in farms:
    if farms["name"].lower() == choice.lower():
        print(['agriculture'])
