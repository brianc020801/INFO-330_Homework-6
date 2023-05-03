import sqlite3  # This is the package for all sqlite3 access in Python
import sys      # This helps with command-line parameters

# All the "against" column suffixes:
types = ["bug","dark","dragon","electric","fairy","fight",
    "fire","flying","ghost","grass","ground","ice","normal",
    "poison","psychic","rock","steel","water"]

db = sqlite3.connect("../pokemon.sqlite")

def getInfo(dexnum): # Function to get neccessary data
    cur = db.cursor() # Open cursor
    if not dexnum.isnumeric(): # If input is not number get pokedex number using pokemon name
        cur.execute("SELECT pokedex_number FROM pokemon WHERE pokemon.name = ?;", (dexnum.lower().capitalize(),))
        dexnum = cur.fetchone()[0]
    cur.execute("SELECT p.name, a.* FROM pokemon_types_view AS t, pokemon AS p, pokemon_types_battle_view AS a " # Select necessary data using dex number
                "WHERE t.name = p.name AND p.pokedex_number = ? AND a.type1name = t.type1 AND a.type2name = t.type2;", (dexnum,))
    data = cur.fetchone()
    strong_against = []
    weak_against = []
    for i in range(len(types)): # Split the types into strong against and weak against
        if int(data[i + 3]) > 1:
            weak_against.append(types[i])
        elif int(data[i + 3]) < 1:
            strong_against.append(types[i])
    if data[2] == '': # Format variables for output
        type = "(" + str(data[1]) + ")"
    else:
        type = "(" + str(data[1] + " " + data[2]) + ")"
    pokemon = { # Store data in a dictionary
        "dex_num": dexnum,
        "name": str(data[0]),
        "type": type,
        "strong": strong_against,
        "weak": weak_against
    }
    cur.close() # Close the cursor
    return pokemon # Return dictionary
def printAnalysis(pokemon): # Prints the analysis
    print("Analyzing " + str(pokemon["dex_num"])) # Print analyzing + dex number
    name = pokemon["name"]
    type = pokemon["type"]
    strong = pokemon["strong"]
    weak = pokemon["weak"]
    print(name + " " + type + " is strong against " + str(strong) + " but weak against " + str(weak)) # prints output string
# Take six parameters on the command-line
if len(sys.argv) < 6:
    print("You must give me six Pokemon to analyze!")
    sys.exit()

team = []
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue
    # Analyze the pokemon whose pokedex_number is in "arg"
    if not arg.isnumeric():  # If input is not number get pokedex number using pokemon name
        cur = db.cursor()  # Open cursor
        cur.execute("SELECT pokedex_number FROM pokemon WHERE pokemon.name = ?;", (arg.lower().capitalize(),))
        team.append(cur.fetchone()[0])
        cur.close()
    else:
        team.append(arg) # add dex number to team
    printAnalysis(getInfo(arg)) # call function to print analysis
    # You will need to write the SQL, extract the results, and compare
    # Remember to look at those "against_NNN" column values; greater than 1
    # means the Pokemon is strong against that type, and less than 1 means
    # the Pokemon is weak against that type

answer = input("Would you like to save this team? (Y)es or (N)o: ")
if answer.upper() == "Y" or answer.upper() == "YES":
    teamName = input("Enter the team name: ")
    cur = db.cursor() # open cursor
    cur.execute("CREATE TABLE IF NOT EXISTS teams (" # create teams table
                "id INTEGER PRIMARY KEY,"
                "name TEXT,"
                "pokemon1 REFERENCES pokemon, "
                "pokemon2 REFERENCES pokemon, "
                "pokemon3 REFERENCES pokemon, "
                "pokemon4 REFERENCES pokemon, "
                "pokemon5 REFERENCES pokemon, "
                "pokemon6 REFERENCES pokemon);")
    cur.execute("INSERT INTO teams (name, pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6) " # insert team into teams
                "VALUES (?, ?, ?, ?, ?, ?, ?);", (teamName, team[0], team[1], team[2], team[3], team[4], team[5],))
    db.commit() # commit changes
    cur.close() # close cursor
    # Write the pokemon team to the "teams" table
    print("Saving " + teamName + " ...")
else:
    db.close() # close db
    print("Bye for now!")


