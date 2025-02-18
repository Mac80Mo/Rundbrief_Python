import os

with open("gaeste.txt", "r", encoding="utf-8") as file:
    for name in file:
        name = name.strip()
        print("Einladung an: " + name + "\n\n")
        
        text = f"Hallo {name}, \n\n" + \
            "Ich möchte Dich gerne zu meinem Geburtstag einladen.\n\n" + \
            "Viele Grüße\n\n" + \
            "Marcus"
        
        pathToNewFile = os.path.join("einladungen", f"{name}.txt")
        with open(pathToNewFile, "w", encoding="utf-8") as outFile:
            outFile.write(text)
        
        
        print(text)



