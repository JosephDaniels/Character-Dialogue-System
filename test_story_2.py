from character_dialogue import DialogueNode as DN

# create a simple story
# (it's incomplete but it gives the gist of how the data structure works- AW)


a = DN()
a.node_id = 1
a.name = "Once upon a time"
a.text = """
Once upon a time a litle girl was walking through the woods,
and she stumbled upon  house made of gingerbread
"""

# branches are a pair of tuples consisting of ("choice_text", and the story_node_id it leads to)
a.branches = [("She took a bite out of the house", 2),
              ("She knocked on the door", 3),
              ("'Oy! what am I supposed top do?", 4)]

b = DN()
b.node_id = 2
b.name = "It's poison you dolt!"
b.text = """
Alas, the little girl forgot the teachings of he mother and
she suffer gastroenteris from eating raw cookie dough"""
b.branches = [("She sticks a finger down he throat", 5),
              ("She crys for help"), 5]

c = DN()
c.node_id = 5
c.name = "Game over man!"
c.text = "Too late, she's dead"
c.branches = []
