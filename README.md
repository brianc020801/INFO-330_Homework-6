# Greetings!

In this homework assignment, you must write some code (either Python or Java) to access the SQLite database and work with it.

## Background

Professor Oak had another problem.

![](https://archives.bulbagarden.net/media/upload/1/17/Professor_Oak_BW_anime.png)

After Misty had managed to rebuild the relational database from the CSV file, Professor Oak had restarted his research on some of the newest Pokemon discovered yet, the Huskychu and Cougarite. However, he was finding that working with the database directly was problematic--he kept making errors that violated the database's relational integrity constraints.

Thus, when Ash came by the next day, Professor Oak was in a pretty bad mood.

![](Images/Ash-Ketchum.png)

"Professor!" Ash could see Professor Oak was upset. "What's wrong?"

"Oh, hello Ash. It's this Python code. It just doesn't seem..."

"Python?" Ash's face screwed up in concentration. "Isn't that some kind of snake?"

"Well, yes, but--"

"And a snake... Professor! It's Team Rocket! I'd recognize their Ekans anywhere!"

![](Images/Ekans.png)


"But Ash, I--"

"No time to talk, Professor! Let's go, Pikachu! I choose--"

Ash's voice faded as he ran down the path to go find Team Rocket.

Professor Oak sighed, and turned his attention back to the Python code in front of him. "Hmmm.... maybe if I use Java instead...." Then, sipping from his coffee cup, he chuckled at his bad joke and wondered what to do next.

## Goals

You need to write some Java or Python code to access the SQLite Pokemon database in pokemon.db. Your program will help build out Pokemon teams, by helping trainers choose which Pokemon are good against which other kinds of Pokemon they face.

This program must take a set of six command-line parameters, which will be Pokedex numbers, and analyze how well they do against all the different types of Pokemon. It will then ask the user if this team is worth saving, and if so, write the contents to the "teams" table. For example:

```
% python3 TeamAnalyzer.py 1 2 3 4 5 6
Analyzing 1
Bulbasaur (grass poison) is strong against ['fire', 'flying', 'ice', 'psychic'] but weak against ['electric', 'fairy', 'fight', 'grass', 'water']
Analyzing 2
Ivysaur (grass poison) is strong against ['fire', 'flying', 'ice', 'psychic'] but weak against ['electric', 'fairy', 'fight', 'grass', 'water']
Analyzing 3
Venusaur (grass poison) is strong against ['fire', 'flying', 'ice', 'psychic'] but weak against ['electric', 'fairy', 'fight', 'grass', 'water']
Analyzing 4
Charmander (fire ) is strong against ['ground', 'rock', 'water'] but weak against ['bug', 'fairy', 'fire', 'grass', 'ice', 'steel']
Analyzing 5
Charmeleon (fire ) is strong against ['ground', 'rock', 'water'] but weak against ['bug', 'fairy', 'fire', 'grass', 'ice', 'steel']
Analyzing 6
Charizard (fire flying) is strong against ['electric', 'rock', 'water'] but weak against ['bug', 'fairy', 'fight', 'fire', 'grass', 'ground', 'steel']
Would you like to save this team? (Y)es or (N)o: Y
Enter the team name: Team SpaceX
Saving Team SpaceX ...
```

A Pokemon is "good" against another type if its "against_" column is greater than 1; it is "weak" to that type if that column is less than 1.

Note that this version of the Pokemon databases has a few views that you may find helpful.

You are free to use either Python or Java for this assignment; a Python starter is in the Python directory, and a Java starter is in the Java directory. (Python is recommended.)

> **HINT (Java):** Remember, if you use Java, you must have the SQLite driver on the *classpath* when you run the code; use the following to make that happen: `java -classpath .:sqlite-jdbc-3.41.2.1.jar TeamAnalyzer` for macOS or Linux, `java -classpath .;sqlite-jdbc-3.41.2.1.jar TeamAnalyzer` for Windows. (You can also use the more modern `java -classpath sqlite-jdbc-3.41.2.1.jar TeamAnalyzer.java` and pretend Java is a source-interpreted language like Python, but doing so means you will have to learn how to use compiled code some other day.)

## Extra credit

* **Flexible input (1 pt):** Accept either Pokedex numbers *or* Pokemon names at the command line, so that `python3 TeamBuilder.py Bulbasaur Ivysaur Venusaur 4 5 6` works (and generates the same input as above).


## Attributions
Images are from <a href='https://www.pngmart.com' target="_blank">PNGMart</a>.

