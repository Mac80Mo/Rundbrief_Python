names = [
    "Moritz Mueller",
    "Erika Mustermann",
    "Tobias M."
]

#text = "Ich bin ein Text"

for name in names:
    print("Einladung an: " + name + "\n\n")
    text = f"Hallo {name}, \n\n" + \
        "Ich möchte Dich gerne zu meinem Geburtstag einladen.\n\n" + \
        "Viele Grüße\n\n" + \
        "Marcus"
    print(text)
    print("----------------")