import json
import random
import time

def write_array_to_json(array, file_path):
    # Array in JSON konvertieren und in Datei schreiben
    with open(file_path, 'w') as file:
        json.dump(array, file)

# Pfad zur JSON-Datei
json_file_path = 'C:/xampp/htdocs/ttt/spielfeld2.json'

while True:
    # Zufälliges Array mit Zahlen von 0 bis 2 generieren
    new_array = [[random.randint(0, 2) for _ in range(3)] for _ in range(3)]
    
    # Array in JSON-Datei schreiben
    write_array_to_json(new_array, json_file_path)

    print("Array wurde erfolgreich in die JSON-Datei geschrieben.")
    print(new_array)
    
    # Eine Sekunde warten, bevor das nächste Array geschrieben wird
    time.sleep(3)   