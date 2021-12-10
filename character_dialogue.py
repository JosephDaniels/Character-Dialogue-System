""" A system that handles character interactions and allows for intricate dialogue interaction trees.

The dialogue system although named after a conversation of two people, is designed to handle storytelling for a
single player that might involve one ore more NPC characters.

I would love to make a version in the future that allows multiple characters to respond but for now it's basically
a visual novel with the inclusion of characters. I also thought of having certain moodles attached to certain nodes,
but that's a future improvement...

-JV

"""

class Dialogue_System(object):
    def __init__(self):
        self.scenes = []  ## A list of all scenes loaded into the manager
        self.characters = []  # A list of all relevant characters who are in the current scene

    def add_scene(self, scene):
        self.scenes.append(scene)

    def remove_scene(self, scene):
        try:
            self.scenes.remove(scene)
        except ValueError:
            print ("Scene %s couldn't be removed, it doesn't exist!" % (scene))

    def add_character(self, character):
        self.characters.append(character)

    def remove_character(self, character):
        self.characters.remove(character)

class Scene(object):
    def __init__(self):
        self.title = ""  ## Name of the scene e.g "Together at grandma's house"
        self.description = ""  ## Brief summary of the scene "You are making cookies at Grandma's house"
        self.characters = []  ## All the characters in the current scene
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

class DialogueNode(object):
    def __init__(self, node_id = ""):
        self.text = ""  ## What the character is currently saying
        self.character = ""  ## Has a name if this line is spoken by a specific character
        if node_id:  #Initialize a non-blank node id
            self.node_id = node_id
            self.load()
        elif node_id == "":  # Default
            self.node_id = -1  ## Defaults to -1 for an uninitialized Dialogue Nodule
        self.branches = {}  ## possible outcomes based on what you say linked to the node they bring you to

    def load(self):
        filename = "scenes/%s.txt" % (self.node_id)
        f = open(filename, mode='r')
        _data = ""
        for line in f:
            _data = _data+line
        #print ("data = %s" % (_data))
        self.set_text(_data)

    def set_text(self, words):
        for line in words:
            self.text = self.text+line

    def add_branch(self, response, outcome_node):
        self.branches[response] = outcome_node

    def print_text(self):
        print (self.text)

def test_1():
    dnode = DialogueNode(node_id="node-00-00-00-01")
    dnode.print_text()

if __name__ == "__main__":
    test_1()