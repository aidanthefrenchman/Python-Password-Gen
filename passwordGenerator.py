import random

# © 2024 aidanthefrenchman | This password generator for the express purpose of creating passwords for new users at work

library = {
    # 5 Letter Words
    "Grain":"Noun", "Braid":"Noun", "Relax":"Verb", "Table":"Noun", "Enter":"Verb","Penny":"Noun", "Forge":"Verb", "Apple":"Noun", "Study":"Verb", "Solve":"Verb",
    "Storm":"Noun", "Serve":"Verb", "Touch":"Verb", "Beard":"Noun", "Allow":"Verb", "Suite":"Noun", "Patch":"Noun, Verb", "Order":"Verb", "Angle":"Verb", "Hover":"Verb",
    "First":"Number", "Panel":"Noun", "Score":"Noun", "Abbey":"Noun", "Ditch":"Verb", "Build":"Verb", "Catch":"Verb", "Cabin":"Noun", "Flood":"Noun, Verb", "Cause":"Noun, Verb",
    "Queen":"Noun", "Clean":"Noun, Verb", "Great":"Noun", "Fraud":"Noun", "Ghost":"Noun, Verb", "Tribe":"Noun", "Fleet":"Noun", "Spell":"Noun, Verb", "Class":"Noun", "Knife":"Noun",
    "Limit":"Noun, Verb", "Glide":"Verb", "Front":"Noun, Verb", "Cheap":"Noun", "Agent":"Noun", "Horse":"Noun", "Enemy":"Noun", "Prove":"Verb", "Sweet":"Adjective", "Truth":"Noun",

    # 6 Letter Words
    "Pierce":"Verb", "Salmon":"Noun", "Energy":"Noun", "Stitch":"Noun", "Mobile":"Adjective", "Scrape":"Verb", "Attack":"Verb", "Island":"Noun", "Tactic":"Noun", "Safari":"Noun",
    "Suntan":"Noun", "Nature":"Noun", "Trance":"Noun", "Clinic":"Noun", "Ground":"Noun", "Detail":"Noun", "Forbid":"Verb", "Health":"Noun", "Driver":"Noun", "Flower": "Noun",
    "Patrol":"Noun", "Porter":"Noun", "Figure":"Noun", "Lounge":"Verb", "Center":"Noun", "Sodium":"Noun", "Active":"Noun", "Relief":"Noun", "Border":"Noun", "Grudge":"Noun",
    "Person":"Noun", "Player":"Noun", "Devote":"Verb", "Morsel":"Noun", "Expand":"Verb", "Delete":"Verb", "Tender":"Adjective", "Silver":"Noun", "Appeal":"Noun", "Filter":"Noun",
    "Matrix":"Noun", "Redeem":"Verb", "Excuse":"Verb", "Cellar":"Noun", "Gutter":"Noun", "Mother":"Noun", "Murder":"Noun", "Oppose":"Verb", "Garlic":"Noun", "Square":"Noun",

    # 7 Letter Words
    "Bathtub":"Noun", "Pursuit":"Noun", "Physics":"Noun", "Channel":"Noun", "Student":"Noun", "Maximum":"Noun", "Perfume":"Noun", "Academy":"Noun", "Compose":"Verb", "Venture":"Noun",
    "Monster":"Noun", "Meaning":"Noun", "Comfort":"Verb", "Serious":"Adjective", "Replace":"Verb", "Gesture":"Noun", "Inspire":"Verb", "Tribute":"Noun", "Kinship":"Noun", "Emotion":"Noun",
    "Process":"Noun", "Plaster":"Noun", "Drawing":"Noun", "Gravity":"Noun", "Persist":"Verb", "Mention":"Verb", "Fiction":"Noun", "Silence":"Noun", "Provoke":"Verb", "Wording":"Noun",
    "Project":"Noun", "Extinct":"Noun", "Command":"Verb", "Protest":"Noun", "Trolley":"Noun", "Pottery":"Noun", "Benefit":"Noun", "Drawing":"Noun", "Uniform":"Noun", "Quarter":"Noun",
    "Chapter":"Noun", "Warrant":"Noun", "Welcome":"Interjection", "Combine":"Verb", "Certain":"Adjective", "Concept":"Noun", "Default":"Noun", "Current":"Adjective", "Counter":"Noun", "Context":"Noun",
}

#there are .keys and there are .items in a dictionary. the former is the first value and the latter is both the firat and second values.
def create_password():
    characters = random.choice(list(library.keys())) , random.choice(list(library.keys())) , random.randrange(000, 999, 1)
    return (characters)

password = create_password()
print("Hello! Welcome to your new password!")
print(".")
print(password)
print(".")
print(".")
print("Combine the two words and three digit number as so:")
print("e.g. ('Grand', 'Show', 100) becomes GrandShow100")
print("This password will be used for all of the accounts associated with your SSO email.")
print(".")
print(".")
print(".")
print("This password generator for the express purpose of creating passwords for new users.")
print("© 2024 aidanthefrenchman")
input()