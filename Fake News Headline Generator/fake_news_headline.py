import random
subjects=[
    "Shakib Al Hasan",
    "Lionel Messi",
    "Habib Wahid",
    "Elon Musk",
    "A group of Cats",
    "Dr. Younus",
    "Tesla Drivers of Dhaka",
    "Christiano Ronaldo"
]
actions=[
    "Launces",
    "Cancel",
    "Dance",
    "Smokes",
    "Celebrates",
    "Stated War",
    "Wins the Election"
]
places=[
    "in Dhaka",
    "at the White House",
    "on the Moon",
    "in a Galaxy far far away",
    "at a secret location",
    "Buriganga River",
    "in Santiago Bernabeu",
    "in Camp Nou",
    "in Ganavaban"
]
#Stating headline generating

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place=random.choice(places)
    headline=f"Todays breaking news : {subject} {action} {place}"
    print("\n"+headline)
    
    user_input=input("\n Do you want to generate another headline? (yes/no): ").strip().lower()
    if user_input =="yes":
        continue
    elif user_input == "no":
        break
    else:
        print("Wrong input!")
        break
print("Thanks for using our program!")