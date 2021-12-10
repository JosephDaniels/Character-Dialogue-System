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
              ("She crys for help", 5)]

c = DN()
c.node_id = 5
c.name = "Game over man!"
c.text = "Too late, she's dead"
c.branches = []

scenes = {
    1: a,
    2: b,
    5: c
}


def test_1():
    current_id= 1
    curr_node = scenes[current_id]
    running = True
    while running == True:
        # display the current scene
        print(curr_node.name)
        print(curr_node.text)
        for i, branch in enumerate(curr_node.branches):
            print( "    ", i+1, branch[0]) # print the branch text
        response = input()
        if response in ["1", "2", "3", "4"]:
            current_id = curr_node.branches[int(response)-1][1]
            curr_node = scenes[current_id]

if __name__ == "__main__":
    test_1()