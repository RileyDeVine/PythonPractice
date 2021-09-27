#define function
def define(word):

    word = word.lower()

    #if statement for first word
    if word == "jaeger":
        return "Jaeger- The Russian term for hunter, Pacific rim reference :)"

    #elif statement for second word
    elif word == "kaiju":
        return "Kaiju-Japanese term for Giant Monster, commonly associated with fictional creatures such as Gojira(Godzilla)"

    #elif statement for third word
    elif word == "muto":
        return "MUTO- Massive Unidentified Terrestrial Organism"

    #elif statement for fourth word
    elif word == "drone":
        return "Drone- A term refering to an remote controlled mechanical device"
    
    #elif statement for fifth word
    elif word == "omnitrix":
        return "Omnitrix- A wrist mounted device capable of altering the user's DNA to match that of a requested species"
    
    #elif statement for sixth word
    elif word == "titan":
        return "Titan- A being of immense size, commonly refered to in greek mythology, essentially the Greek equivilent to Kaiju"

    #elif statement for seventh word
    elif word== "traction city":
        return "Traction City- A city or town which has either been converted or built to be on wheels, and is mobile"

    #else statement for unknown words
    else:
        return word + " is an unknown word, cannot retrieve definition!"


print(define("traction city"))





