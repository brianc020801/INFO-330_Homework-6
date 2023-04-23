# Greetings!

In this homework assignment, you must write some code (either Python or Java) to access the SQLite database and work with it.

## Background

Professor Oak had another problem.

(Prof Oak pic)

After Misty had managed to rebuild the relational database from the CSV file, Professor Oak had restarted his research on some of the newest Pokemon discovered yet, the Huskychu and Cougarite. However, he was finding that working with the database directly was problematic--he kept making errors that violated the database's relational integrity constraints.

Thus, when Ash came by the next day, Professor Oak was in a pretty bad mood.

(Ash pic)

"Professor!" Ash could see Professor Oak was upset. "What's wrong?"

"Oh, hello Ash. It's this Python code. It just doesn't seem..."

"Python?" Ash's face screwed up in concentration. "Isn't that some kind of snake?"

"Well, yes, but--"

"And a snake... Professor! It's Team Rocket! I'd recognize their Ekans anywhere!"

(Ekans pic)

"But Ash, I--"

"No time to talk, Professor! Let's go, Pikachu! I choose--"

Ash's voice faded as he ran down the path to go find Team Rocket.

Professor Oak sighed, and turned his attention back to the Python code in front of him. "Hmmm.... maybe if I use Java instead...." Then, sipping from his coffee cup, he chuckled at his bad joke and wondered what to do next.

## Goals

You need to write some Java or Python code to access the SQLite Pokemon database in pokemon.db. Your program will help build out Pokemon teams, by helping trainers choose which Pokemon are good against which other kinds of Pokemon they face. An example session looks like this:

```
$ java TeamBuilder
Hello! What would you like to do:
(B)uild a new team
--> B
Excellent! What would you like to name this team?
--> Team SpaceX
Very good! What kind of Pokemon will you be facing, Team SpaceX?:
(B)ug, (G)rass, (F)ighting, F(L)ying, ...
--> B
Hmm. It looks like the following Pokemon would be good against Bug:
(1) Bulbasaur
(2) Ivysaur
(3) ...
Which would you like to add to your team?
--> 1
You now have a Bulbasaur on your team.
Very good! What kind of Pokemon will you be facing, Team SpaceX?:
(B)ug, (G)rass, (F)ighting, F(L)ying, ...
--> L
Hmm. It looks like the following Pokemon would be good against Bug:
(1) Pikachu
(2) ...
(3) ...
Which would you like to add to your team?
--> 1
You now have Bulbasaur, Pikachu on your team.
Very good! What kind of Pokemon will you be facing, Team SpaceX?:
(B)ug, (G)rass, (F)ighting, F(L)ying, ...
...
You now have Bulbasaur, Pikachu, Mew, Charizard, Meowth, Mewtwo on your team.
Your team is now full! Would you like to save your team, (Y)es or (N)o?
--> Y
Saved! Goodbye.
```

Must have a "trainers" table with a name column and six pokemon_id columns.

* 
