import random

# © 2024 Aidan Kosak | This password generator for the express purpose of creating passwords for new users @ Bartle & Gibson Co Ltd.

thisdict = {
    # 5 Letter Words
    "Grain":"Noun", "Braid":"Noun", "Relax":"Verb", "Table":"Noun", "Enter":"Verb","Penny":"Noun", "Forge":"Verb", "Apple":"Noun", "Study":"Verb", "Solve":"Verb",
    "Storm":"Noun", "Serve":"Verb", "Touch":"Verb", "Beard":"Noun", "Allow":"Verb", "Suite":"Noun", "Patch":"Noun, Verb", "Order":"Verb", "Angle":"Verb", "Hover":"Verb",
    "First":"Number", "Panel":"Noun", "Score":"Noun", "Abbey":"Noun", "Ditch":"Verb", "Build":"Verb", "Catch":"Verb", "Cabin":"Noun", "Flood":"Noun, Verb", "Cause":"Noun, Verb",
    "Queen":"Noun", "Clean":"Noun, Verb", "Great":"Noun", "Fraud":"Noun", "Ghost":"Noun, Verb", "Tribe":"Noun", "Fleet":"Noun", "Spell":"Noun, Verb", "Class":"Noun", "Knife":"Noun",
    "Limit":"Noun, Verb", "Glide":"Verb", "Front":"Noun, Verb", "Cheap":"Noun", "Agent":"Noun", "Horse":"Noun", "Enemy":"Noun", "Prove":"Verb", "Sweet":"Adjective", "Truth":"Noun",

    # 6 Letter Words
    "Pierce":"Verb", "Salmon":"Noun", "Energy":"Noun", "Stitch":"Noun", "Mobile":"Adjective", "Scrape":"Verb", "Attack":"Verb", "Island":"Noun", "Tactic":"Noun", "Safari":"Noun",
    "Suntan":"Noun", "Nature":"Noun", "Trance":"Noun", "Clinic":"Noun", "Ground":"Noun", "Detail":"Noun", "Forbid":"Verb", "Health":"Noun", "Driver":"Noun", "Flower": "Noun",
    "Patrol":"Noun", "Porter":"Noun", "Figure":"Noun", "Lounge":"Verb",
    # 7 Letter Words
    "Bathtub":"Noun", "Pursuit":"Noun",

}

def generate_password():
    characters = random.choice(list(thisdict.keys())) , random.choice(list(thisdict.keys())) , random.randrange(000, 999, 1)
    return (characters)

password = generate_password()
print(password)
input()