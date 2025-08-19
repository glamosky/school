"""
This script randomizes price and quantity for items in the aviation store inventory.

Note: For the exam, I kept the required structure in my main file as instructed (hopefully).
I considered making this into a separate helper file and importing it (to show
a more scalable and modular approach), but since the instructions were strict,
I decided to keep it self-contained here to maintain integrity. I want to personalize everything on this exam but maybe my ideas are overkill.
"""


import random

# base inventory
item_list = [
    {"id": 1, "name": "GeminiJets Boeing 777-300ER Emirates 1/400"},
    {"id": 2, "name": "GeminiJets Airbus A350-900 Qatar Airways 1/400"},
    {"id": 3, "name": "NG Models Boeing 737-800 American Airlines 1/400"},
    {"id": 4, "name": "Phoenix Models Boeing 787-9 All Nippon Airways 1/400"},
    {"id": 5, "name": "JC Wings Airbus A321neo easyJet 1/400"},
    {"id": 6, "name": "NG Models Boeing 757-200 Delta Air Lines 1/400"},
    {"id": 7, "name": "Herpa Boeing 747-400 Lufthansa 1/500"},
    {"id": 8, "name": "AeroClassics Airbus A310-300 Air France 1/400"},
    {"id": 9, "name": "Phoenix Models Airbus A380-800 Emirates 1/400"},
    {"id": 10, "name": "GeminiJets Boeing 767-300ER Japan Airlines 1/400"},
    {"id": 11, "name": "NG Models Boeing 787-10 United Airlines 1/400"},
    {"id": 12, "name": "JC Wings Airbus A350-1000 British Airways 1/400"},
    {"id": 13, "name": "Phoenix Models Airbus A330-300 Cathay Pacific 1/400"},
    {"id": 14, "name": "NG Models Boeing 737 MAX 8 Southwest 1/400"},
    {"id": 15, "name": "Herpa Airbus A321neo Lufthansa 1/500"},
    {"id": 16, "name": "AeroClassics McDonnell Douglas DC-10-30 KLM 1/400"},
    {"id": 17, "name": "GeminiJets Boeing 737-700 Southwest Canyon Blue 1/400"},
    {"id": 18, "name": "JC Wings Boeing 777-9X Lufthansa 1/400"},
    {"id": 19, "name": "GeminiJets Airport Ground Service Set 1/400"},
    {"id": 20, "name": "GeminiJets Airport Terminal Set 1/400"},
    {"id": 21, "name": "Revell Boeing 747-8 Lufthansa 1/144 Plastic Kit"},
    {"id": 22, "name": "Airfix Supermarine Spitfire Mk.IXc 1/48 Plastic Kit"},
    {"id": 23, "name": "Tamiya F-16C Block 50 Fighting Falcon 1/48 Plastic Kit"},
    {"id": 24, "name": "Hasegawa F-14D Tomcat 1/72 Plastic Kit"},
    {"id": 25, "name": "Zvezda Airbus A320neo 1/144 Plastic Kit"},
    {"id": 26, "name": "Italeri Lockheed Martin F-35A Lightning II 1/48 Plastic Kit"},
    {"id": 27, "name": "Trumpeter Sukhoi Su-27 Flanker B 1/72 Plastic Kit"},
    {"id": 28, "name": "Academy Boeing B-17G Flying Fortress 1/72 Plastic Kit"},
    {"id": 29, "name": "Eduard Messerschmitt Bf 109G-6 ProfiPACK 1/48 Plastic Kit"},
    {"id": 30, "name": "Revell Airbus A380-800 Emirates 1/144 Plastic Kit"},
    {"id": 31, "name": "Airfix Hawker Hurricane Mk.I 1/72 Plastic Kit"},
    {"id": 32, "name": "Tamiya North American P-51D Mustang 1/48 Plastic Kit"},
    {"id": 33, "name": "Hasegawa F/A-18E Super Hornet 1/72 Plastic Kit"},
    {"id": 34, "name": "Zvezda Boeing 777-300ER 1/144 Plastic Kit"},
    {"id": 35, "name": "Italeri Lockheed C-130H Hercules 1/72 Plastic Kit"},
    {"id": 36, "name": "Trumpeter Mikoyan MiG-29 9-13 1/72 Plastic Kit"},
    {"id": 37, "name": "Academy SR-71A Blackbird 1/72 Plastic Kit"},
    {"id": 38, "name": "Eduard Spitfire Mk.Vb Weekend Edition 1/48 Plastic Kit"},
    {"id": 39, "name": "Kinetic F-16I Sufa 1/48 Plastic Kit"},
    {"id": 40, "name": "Hobby Boss A-10C Thunderbolt II 1/48 Plastic Kit"},
    {"id": 41, "name": "Revell Condor Airbus A320"},
    {"id": 42, "name": "GeminiJets Airport Terminal Set 1/400 Scale"},
    {"id": 43, "name": "GeminiJets 1/400 Scale Airport Mat"},
    {"id": 44, "name": "Herpa Antonov Airlines AN-225 1/500 Scale"},
    {"id": 45, "name": "JetHut All Nippon Airways 787-9 Dreamliner JA873A (R2-D2 SW) 1/400 Scale"},
    {"id": 46, "name": "JC Wings EasyJet Airbus A321neo G-UZME 1/400 Scale"},
    {"id": 47, "name": "Phoenix Virgin Atlantic Boeing 787-9 G-VBOW 1/400"},
    {"id": 48, "name": "Icelandair A321neo 1/200"},
    {"id": 49, "name": "USAF B-52H 1/400"},
    {"id": 50, "name": "Icelandair A321neo 1/200"},
    {"id": 51, "name": "Antonov 225 Mriya 1/400"},
    {"id": 52, "name": "American Eagle Saab 340B 1/200"},
    {"id": 53, "name": "TUI 737 MAX 8 1/200"},
    {"id": 54, "name": "Helvetic E190-E2 1/200"},
    {"id": 55, "name": "Aerolineas Argentinas 737M8 1/200"},
    {"id": 56, "name": "Eastern 727-100 1/200"},
    {"id": 57, "name": "jetBlue A321neo 1/200"},
    {"id": 58, "name": "US Navy F/A-18C Hornet 1/72"},
    {"id": 59, "name": "Pan Am 757-200 1/200"},
    {"id": 60, "name": "Pan Am 757-200 1/400"},
    {"id": 61, "name": "USAF C-130 Montana ANG 1/200"},
    {"id": 62, "name": "Cubana ATR-72 1/200"},
    {"id": 63, "name": "United 777-200 Star Alliance 1/400"},
    {"id": 64, "name": "British Airways A380 1/400"}
]

# possible prices
price_choices = [20, 40, 60, 100]

# assign random price and quantity
for item in item_list:
    item["price"] = random.choice(price_choices)
    item["quantity"] = random.randint(10, 100)

# show result
for item in item_list:
    print(item)
