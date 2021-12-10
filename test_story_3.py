from character_dialogue import DialogueNode as DN

# create a simple story
# (it's incomplete but it gives the gist of how the data structure works- AW)

# A modification of the original test story, now I'm just refactoring a bit - JV

a = DN()
a.node_id = 1
a.name = "Beginning of the Game"
a.character = "Narrator"
a.text = """
Hello there adventurer, welcome to Grassdale Village.
"""

# branches are a pair of tuples consisting of ("choice_text", and the story_node_id it leads to)
a.branches = [("Who are you?", 2),
              ("Where am I?", 3),
              ("What do I see?", 3)]

b = DN()
b.node_id = 2
b.character = "Narrator"
b.text = """
I am just a ghostly voice in your head.
"""
b.branches = [("Where am I?", 3),
              ("What do I see?", 3),]

c = DN()
c.node_id = 3
c.name = "Grassdale Village Description"
c.character = "Narrator"
c.text = """
You find yourself in the village of Grassdale. 

Laying on the gravel covered ground, you awaken staring up into the branches of a tree.
 
Everything swirls around you as you slowly awaken.
 
Your eyes slowly focus until you see the red orbs above you becoming juicy red apples.

They shifts as the tree branch sways in the breeze.
"""
c.branches = [("Continue...", 5)]

scenes = {
    1: a,
    2: b,
    3: c
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